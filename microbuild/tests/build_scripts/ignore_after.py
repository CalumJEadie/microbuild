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
@microbuild.ignore
def images():
    """Prepare images. Should be ignored."""

    raise Exception("This task should have been ignored.")

@microbuild.task(clean,html,images)
def android():
    """Package Android app."""

    print "android"
    
if __name__ == "__main__":
    microbuild.build(sys.modules[__name__],sys.argv[1:])
