#!/usr/bin/python

import sys
import subprocess

def apidoc():
    subprocess.call(["epydoc","--config","epydoc.config"])
    
def test():
    subprocess.call(["python","-m","bob.tests.bob"])
    
if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "apidoc":
        apidocs()
    elif args[0] == "test":
        test()
    else:
        print "_ apidoc"
