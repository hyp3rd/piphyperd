"""
This type stub file was generated by pyright.
"""

import re

"""Wheels support."""
WHEEL_NAME = re.compile(r"""^(?P<project_name>.+?)-(?P<version>\d.*?)
    ((-(?P<build>\d.*?))?-(?P<py_version>.+?)-(?P<abi>.+?)-(?P<platform>.+?)
    )\.whl$""", re.VERBOSE).match
NAMESPACE_PACKAGE_INIT = "__import__('pkg_resources').declare_namespace(__name__)\n"
def unpack(src_dir, dst_dir):
    '''Move everything under `src_dir` to `dst_dir`, and delete the former.'''
    ...

class Wheel:
    def __init__(self, filename) -> None:
        ...
    
    def tags(self):
        '''List tags (py_version, abi, platform) supported by this wheel.'''
        ...
    
    def is_compatible(self):
        '''Is the wheel is compatible with the current platform?'''
        ...
    
    def egg_name(self):
        ...
    
    def get_dist_info(self, zf):
        ...
    
    def install_as_egg(self, destination_eggdir):
        '''Install wheel as an egg directory.'''
        ...
    

