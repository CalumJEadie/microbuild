#!/usr/bin/python

import sys
import subprocess
from bob import bob

@bob.task()
def apidoc():
    """
    Generate API documentation using epydoc.
    """
    subprocess.call(["epydoc","--config","epydoc.config"])
    
@bob.task()
def test():
    """
    Run unit tests.
    """
    subprocess.call(["python","-m","bob.tests.bob"])
    
if __name__ == "__main__":
    bob.build(sys.modules[__name__],sys.argv[1:])
