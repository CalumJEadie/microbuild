from distutils.core import setup

setup(
   name="microbuild",
   version="0.3.2",
   author="Calum J. Eadie",
   author_email="calum@calumjeadie.com",
   url="https://github.com/CalumJEadie/microbuild",
   packages=["microbuild"],
   license="MIT License",
   description="Lightweight Python Build Tool.",
   long_description=open("README.rst").read()+"\n"+open("CHANGES.rst").read()
)
