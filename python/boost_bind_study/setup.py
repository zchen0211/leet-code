from distutils.core import setup
from distutils.extension import Extension


# distutil is used to distribute python modules

# Call python setup.py build
# To make a dir build, and generate .so file from .cpp
# change args in Extension(args) accordingly to run
setup(name="PackageName",
    ext_modules=[
        Extension("inheritance", ["inheritance.cpp"],
        libraries = ["boost_python"])
    ])
