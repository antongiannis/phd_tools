"""
PhD Tools: A python package for tools and models used/developed during PhD
==========================================================================

Documentation is available in the docstrings.

Contents
--------


Subpackages
-----------
Using any of these subpackages requires an explicit import.  For example,
``import phdTools.graphs``.

::

 graphs                       --- Collection of useful graphs

Utility tools
-------------

::

 test              --- Run pytest (not yet)
 show_config       --- Show build configuration (not yet)
 __version__       --- phdTools version string

"""

# Import modules
from .graphs import *
from .prosody_tools import *
from .utils import *
from .dict_parse import *

name = "phdTools"
__version__ = "0.0.5"
