from ... import bob

@bob.task()
def clean():
    pass
    
# Referring to clean by name rather than reference.
@bob.task("clean")
def html():
    pass
