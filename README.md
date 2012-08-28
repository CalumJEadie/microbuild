# microbuild - Lightweight Python Build Tool.

Calum J. Eadie (www.calumjeadie.com)

## Features

* Really quick to learn.
* Manages dependancies between tasks.
* Automatically generates command line options and help.

## Example

        # example.py
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
            
        
        
        $ ./example.py -h 
        usage: example.py [-h] task

        positional arguments:
          task        perform specified task and all it's dependancies

        optional arguments:
          -h, --help  show this help message and exit

        tasks:
          android     Package Android app.
          clean       Clean build directory.
          html        Generate HTML.
          images      Prepare images.
          
        $ ./example.py android
        
        Cleaning build directory...
        Generating HTML...
        Preparing images...
        Packaging android app...


## Installation

You can install microbuild from the Python Package Index (PyPI) or from source.

Using pip:

    $ pip microbuild

Using easy_install:

    $ easy_install microbuild
    
# License

microbuild is licensed under a MIT license. See LICENSE.txt.
