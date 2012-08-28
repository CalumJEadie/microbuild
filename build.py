#!/usr/bin/python

import sys
import subprocess
from microbuild import microbuild

@microbuild.task()
def apidoc():
    """
    Generate API documentation using epydoc.
    """
    subprocess.call(["epydoc","--config","epydoc.config"])
    
@microbuild.task()
def test():
    """
    Run unit tests.
    """
    subprocess.call(["python","-m","microbuild.tests.microbuild"])
    
if __name__ == "__main__":
    microbuild.build(sys.modules[__name__],sys.argv[1:])
