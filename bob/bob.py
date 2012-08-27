"""
bob - Really simple Python build tool.
"""

import inspect
import argparse

    
    
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



def _create_parser(module):

    parser = argparse.ArgumentParser(
        epilog="Powered by bob - a really simple Python build tool."
    )
        
    parser.add_argument("task",help="Build task.",choices=["clean","html","android"])
    
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
                        raise TaskDecorationException("%s is not a task. Every dependancy references by a task should be a task." % decorator_args[i])
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
        self.__doc__ = func.__doc__
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
