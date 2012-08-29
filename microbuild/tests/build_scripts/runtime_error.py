"""
Build script with a runtime error.
"""

import sys
from ... import microbuild

@microbuild.task()
def clean():
    """Clean build directory."""

    print "clean"

@microbuild.task(clean)
def html():
    """Generate HTML."""
    
    print "html"

@microbuild.task(clean)
def images():
    """Prepare images. Raises IOError."""

    raise IOError

@microbuild.task(clean,html,images)
def android():
    """Package Android app."""

    print "android"

@microbuild.task(clean,html,images)
def ios():
    """Package iOS app."""

    print "ios"
    
def some_utility_method():
    """Some utility method."""

    print "some utility method"
    
if __name__ == "__main__":
    microbuild.build(sys.modules[__name__],sys.argv[1:])
