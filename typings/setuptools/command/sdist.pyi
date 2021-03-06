"""
This type stub file was generated by pyright.
"""

import distutils.command.sdist as orig
from .py36compat import sdist_add_defaults

_default_revctrl = list
def walk_revctrl(dirname=...):
    """Find all files under revision control"""
    ...

class sdist(sdist_add_defaults, orig.sdist):
    """Smart sdist that finds anything supported by revision control"""
    user_options = ...
    negative_opt = ...
    README_EXTENSIONS = ...
    READMES = ...
    def run(self):
        ...
    
    def initialize_options(self):
        ...
    
    def make_distribution(self):
        """
        Workaround for #516
        """
        ...
    
    def check_readme(self):
        ...
    
    def make_release_tree(self, base_dir, files):
        ...
    
    def read_manifest(self):
        """Read the manifest file (named by 'self.manifest') and use it to
        fill in 'self.filelist', the list of files to include in the source
        distribution.
        """
        ...
    
    def check_license(self):
        """Checks if license_file' or 'license_files' is configured and adds any
        valid paths to 'self.filelist'.
        """
        ...
    


