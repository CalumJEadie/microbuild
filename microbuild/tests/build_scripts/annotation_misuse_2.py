from ... import microbuild

@microbuild.task()
def clean():
    pass
    
# Should be marked as task.
def html():
    pass

# References a non task.
@microbuild.task(clean,html)
def android():
    pass
