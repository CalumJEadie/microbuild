from ... import microbuild

@microbuild.task()
def clean():
    pass
    
# Referring to clean by name rather than reference.
@microbuild.task("clean")
def html():
    pass
