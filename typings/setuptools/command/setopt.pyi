"""
This type stub file was generated by pyright.
"""

from setuptools import Command

def config_file(kind=...):
    """Get the filename of the distutils, local, global, or per-user config

    `kind` must be one of "local", "global", or "user"
    """
    ...

def edit_config(filename, settings, dry_run=...):
    """Edit a configuration file to include `settings`

    `settings` is a dictionary of dictionaries or ``None`` values, keyed by
    command/section name.  A ``None`` value means to delete the entire section,
    while a dictionary lists settings to be changed or deleted in that section.
    A setting of ``None`` means to delete that setting.
    """
    ...

class option_base(Command):
    """Abstract base class for commands that mess with config files"""
    user_options = ...
    boolean_options = ...
    def initialize_options(self):
        ...
    
    def finalize_options(self):
        ...
    


class setopt(option_base):
    """Save command-line options to a file"""
    description = ...
    user_options = ...
    boolean_options = ...
    def initialize_options(self):
        ...
    
    def finalize_options(self):
        ...
    
    def run(self):
        ...
    


