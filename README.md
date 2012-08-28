# microbuild - Lightweight Python Build Tool.

Calum J. Eadie (www.calumjeadie.com)

## Features

* Really quick to learn.
* Manages dependancies between tasks.
* Automatically generates a command line interface.

## Example

The build script is written in pure Python and microbuild takes care of managing
any dependancies between tasks and generating a command line interface.

Tasks are just regular Python functions marked with the `@task` decorator. Dependancies
are specified with `@task` too.

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
        
    if __name__ == "__main__":
        build(sys.modules[__name__],sys.argv[1:])
            
The command line interface and help is automatically generated.
        
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
          
Dependancies between tasks are taken care of too.
    
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
