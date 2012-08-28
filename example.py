#!/usr/bin/python

import sys
from microbuild.microbuild import task,build

@task()
def clean():
    """Clean build directory."""
    print "Cleaning build directory..."

@task(clean)
def html():
    """Generate HTML."""
    print "Generating HTML..."

@task(clean)
def images():
    """Prepare images."""
    print "Preparing images..."

@task(html,images)
def android():
    """Package Android app."""
    print "Packaging android app..."
    
def some_utility_method():
    """Some utility method."""

    print "some utility method"
    
if __name__ == "__main__":
    build(sys.modules[__name__],sys.argv[1:])
