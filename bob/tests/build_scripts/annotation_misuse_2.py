from ... import bob

@bob.task()
def clean():
    pass
    
# Should be marked as task.
def html():
    pass

# References a non task.
@bob.task(clean,html)
def android():
    pass
