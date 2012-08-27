#!/usr/bin/python

import sys
from ... import bob

@bob.task()
def clean():
    """Clean build directory."""

    print "clean"

@bob.task()
def html():
    """Generate HTML."""
    
    print "html"

@bob.task()
def images():
    """Prepare images."""

    print "images"

@bob.task()
def android():
    """Package Android app."""

    print "android"

@bob.task()
def ios():
    """Package iOS app."""

    print "ios"
    
def some_utility_method():
    """Some utility method."""

    print "some utility method"
    
if __name__ == "__main__":
    bob.build(sys.modules[__name__],sys.argv[1:])
