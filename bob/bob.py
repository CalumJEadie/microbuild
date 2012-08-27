"""
bob - Really simple Python build tool.
"""

import inspect
    
#def task(func):
#    """
#    Decorator which marks a function as a build task.
#    """
#    func.is_task = True
#    return func

class task(object):
    """
    Task decorators. Marks a function as a build task.
    """
    
    def __init__(self,*args):
        print args
        
    def __call__(self,f):
        return f
    
def _is_task(function):
    """
    Returns true iff a function is marked as a build task.
    """
    return isinstance(function,task)
    
def _get_tasks(module):
    """
    Returns all functions marked as tasks.
    """
    # Get all functions that are marked as task and pull out the task object
    # from each (name,value) pair.
    return [member[1] for member in inspect.getmembers(module,_is_task)]
