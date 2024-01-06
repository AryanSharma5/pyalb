from importlib.metadata import version, PackageNotFoundError

from pyalb import main

try:
    __version__ = version("pyalb")
except PackageNotFoundError:
    # package is not installed
    pass
