#!/usr/bin/python

import sys
from ... import microbuild

@microbuild.task()
def clean():
    """Clean build directory."""

    print "clean"

@microbuild.task()
def html():
    """Generate HTML."""
    
    print "html"

@microbuild.task()
def images():
    """Prepare images."""

    print "images"

@microbuild.task()
def android():
    """Package Android app."""

    print "android"

@microbuild.task()
def ios():
    """Package iOS app."""

    print "ios"
    
def some_utility_method():
    """Some utility method."""

    print "some utility method"
    
if __name__ == "__main__":
    microbuild.build(sys.modules[__name__],sys.argv[1:])
