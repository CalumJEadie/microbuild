from .. import bob

@bob.task()
def clean():
    """Clean build directory."""

    print "clean"

@bob.task(clean)
def html():
    """Generate HTML."""
    
    print "html"

@bob.task(clean)
def images():
    """Prepare images."""

    print "images"

@bob.task(clean,html,images)
def android():
    """Package Android app."""

    print "android"

@bob.task(clean,html,images)
def ios():
    """Package iOS app."""

    print "ios"
    
def some_utility_method():
    """Some utility method."""

    print "some utility method"
