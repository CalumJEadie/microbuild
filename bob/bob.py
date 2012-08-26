"""
bob - Really simple Python build tool.
"""

import inspect
    
def task(func):
    """
    Decorator which marks a function as a build task.
    """
    func.is_task = True
    return func
    
def _get_functions(module):
    """
    Returns all functions for specified module.
    """
    return [member[1] for member in inspect.getmembers(module,inspect.isfunction)]
    
def _is_task(function):
    """
    Returns true iff a function is marked as a build task.
    """
    return hasattr(function,"is_task")
    
def _get_tasks(module):
    """
    Returns all functions marked as tasks.
    """
    return filter(_is_task,_get_functions(module))
