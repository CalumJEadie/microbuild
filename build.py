#!/usr/bin/python

import sys
import subprocess

def apidocs():
    subprocess.call(["epydoc","--config","epydoc.config"])
    
if __name__ == "__main__":
    args = sys.argv[1:]
    if args[0] == "apidocs":
        apidocs()
    else:
        print "_ apidocs"
