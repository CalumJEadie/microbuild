"""
microbuild - Really simple Python build tool.
"""

import inspect
import argparse
import logging
import sys
import traceback

_CREDIT_LINE = "Powered by microbuild - A Lightweight Python Build Tool."
_LOGGING_FORMAT = "[ %(message)s ]"
    
def build(module,args):
    """
    Build the specified module.
    
    @type module: module
    @type args: list of arguments
    """
    
    # Build the command line.
    parser = _create_parser(module)

    # Parse arguments.
    args = parser.parse_args(args)

    # Run task and all it's dependancies.
    _run_from_task_name(module,args.task)
    
def _run_from_task_name(module,task_name):

    # Create logger.
    logging.basicConfig(level=logging.INFO,format=_LOGGING_FORMAT)
    logger = logging.getLogger(module.__name__)
    
    task = getattr(module,task_name)
    _run(module,logger,task,set([]))
    
def _run(module,logger,task,completed_tasks):
    """
    @type module: module
    @type logging: Logger
    @type task: Task
    @type completed_tasts: set Task
    @rtype: set Task
    @return: Updated set of completed tasks after satisfying all dependancies.
    """

    # Satsify dependancies recursively. Maintain set of completed tasks so each
    # task is only performed once.
    for dependancy in task.dependancies:
        completed_tasks = _run(module,logger,dependancy,completed_tasks)

    # Perform current task, if need to.
    if task not in completed_tasks:

        logging.info("Starting task \"%s\"" % task.__name__)

        try:
            # Run task.
            task()
        except:
            logging.critical("Error in task \"%s\"" % task.__name__)
            traceback.print_exc()
            logging.critical("Build aborted")
            sys.exit()
        
        logging.info("Completed task \"%s\"" % task.__name__)
        
        completed_tasks.add(task)
    
    return completed_tasks

def _create_parser(module):

    # Get all tasks.
    tasks = _get_tasks(module)
    
    # Get task names.
    task_names = [task.__name__ for task in tasks]
    
    # Build epilog to describe the tasks.
    epilog = "tasks:"
    name_width = _get_max_name_length(module)+4
    task_help_format = "\n  {0.__name__:<%s} {0.__doc__}" % name_width
    for task in tasks:
        epilog += task_help_format.format(task)
    epilog += "\n\n"+_CREDIT_LINE
    
    # Build parser.
    # Use RawDescriptionHelpFormatter so epilog is not linewrapped.
    parser = argparse.ArgumentParser(
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("task",help="perform specified task and all it's dependancies",choices=task_names,metavar="task")
    
    return parser

class TaskDecorationException(Exception):
    """
    Throw when task decoration is used incorrectly.
    """
    pass

class _TaskDecorator(object):
    
    def __init__(self,*decorator_args):
        """
        Performs validation on use of @task annotation and captures dependancies.
        
        This constructor is called immediately after decorated function is defined.
        
        To simply implementation of __call__ use of @task() when there a task
        has no dependancies instead of @task is enfored.
        
        This is neccessary because the use case for __call__ is very different depending
        on whether @task or @task() is used.
        
        See http://www.artima.com/weblogs/viewpost.jsp?thread=240845 for more information.
        
        @type decorator_args: tuple
        @param decorator_args: Three cases depending on which form of @task is used.
            - @task then expect (function)
            - @task() then expect ()
            - @task(task1,...,taskN) then expect (task1,...,taskN)
        @throws TaskDecorationException
        """
        
        # Validate arguments.
        # Need to check that either @task() or @task(task1,...,taskN) has been used.
        # If @task or @task(arg1,...,argN) where some arg is not a task then the build script
        # is poorly formed.
        
        # Iterate over by index so we can provide error messages appropriate to the
        # likely form of misuse.
        decorator_args = list(decorator_args)
        for i in range(0,len(decorator_args)):
            if not Task.is_task(decorator_args[i]):
                if inspect.isfunction(decorator_args[i]):
                    # Throw error specific to the most likely form of misuse.
                    if i == 0:
                        raise TaskDecorationException("Replace use of @task with @task().")
                    else:
                        raise TaskDecorationException("%s is not a task. Each dependancy should be a task." % decorator_args[i])
                else:
                    raise TaskDecorationException("%s is not a task." % decorator_args[i])
        
        # Capture dependancies.
        self.dependancies = decorator_args
        
    def __call__(self,func):
        """
        @type func: function
        @param func: Function being decorated.
        """
    
        return Task(func,self.dependancies)
        
# Abbreviate for convenience.
task = _TaskDecorator
        
class Task(object):
    
    def __init__(self,func,dependancies):
        """
        @type func: 0-ary function
        @type dependancies: list of Task objects
        """
        self.func = func
        self.__name__ = func.__name__
        self.__doc__ = inspect.getdoc(func)
        self.__module__ = func.__module__
        self.dependancies = dependancies
        
    def __call__(self): self.func.__call__()
    
    @classmethod
    def is_task(cls,obj):
        """
        Returns true is an object is a build task.
        """
        return isinstance(obj,cls)
    
def _get_tasks(module):
    """
    Returns all functions marked as tasks.
    """
    # Get all functions that are marked as task and pull out the task object
    # from each (name,value) pair.
    return [member[1] for member in inspect.getmembers(module,Task.is_task)]
    
def _get_max_name_length(module):
    """
    Returns the length of the longest task name.
    """
    return max([len(task.__name__) for task in _get_tasks(module)])
