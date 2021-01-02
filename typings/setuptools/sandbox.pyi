"""
This type stub file was generated by pyright.
"""

import os
import sys
import operator
import functools
import contextlib
import org.python.modules.posix.PosixModule as _os
from distutils.errors import DistutilsError

if sys.platform.startswith('java'):
    ...
else:
    _os = sys.modules[os.name]
_open = open
@contextlib.contextmanager
def save_argv(repl=...):
    ...

@contextlib.contextmanager
def save_path():
    ...

@contextlib.contextmanager
def override_temp(replacement):
    """
    Monkey-patch tempfile.tempdir with replacement, ensuring it exists
    """
    ...

@contextlib.contextmanager
def pushd(target):
    ...

class UnpickleableException(Exception):
    """
    An exception representing another Exception that could not be pickled.
    """
    @staticmethod
    def dump(type, exc):
        """
        Always return a dumped (pickled) type and exc. If exc can't be pickled,
        wrap it in UnpickleableException first.
        """
        ...
    


class ExceptionSaver:
    """
    A Context Manager that will save an exception, serialized, and restore it
    later.
    """
    def __enter__(self):
        ...
    
    def __exit__(self, type, exc, tb):
        ...
    
    def resume(self):
        "restore and re-raise any exception"
        ...
    


@contextlib.contextmanager
def save_modules():
    """
    Context in which imported modules are saved.

    Translates exceptions internal to the context into the equivalent exception
    outside the context.
    """
    ...

@contextlib.contextmanager
def save_pkg_resources_state():
    ...

@contextlib.contextmanager
def setup_context(setup_dir):
    ...

_MODULES_TO_HIDE = 'setuptools', 'distutils', 'pkg_resources', 'Cython', '_distutils_hack'
def hide_setuptools():
    """
    Remove references to setuptools' modules from sys.modules to allow the
    invocation to import the most appropriate setuptools. This technique is
    necessary to avoid issues such as #315 where setuptools upgrading itself
    would fail to find a function declared in the metadata.
    """
    ...

def run_setup(setup_script, args):
    """Run a distutils setup script, sandboxed in its directory"""
    ...

class AbstractSandbox:
    """Wrap 'os' module and 'open()' builtin for virtualizing setup scripts"""
    _active = ...
    def __init__(self) -> None:
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    
    def run(self, func):
        """Run 'func' under os sandboxing"""
        ...
    
    if _file:
        _file = ...
    _open = ...


if hasattr(os, 'devnull'):
    _EXCEPTIONS = [os.devnull]
else:
    _EXCEPTIONS = []
class DirectorySandbox(AbstractSandbox):
    """Restrict operations to a single subdirectory - pseudo-chroot"""
    write_ops = ...
    _exception_patterns = ...
    def __init__(self, sandbox, exceptions=...) -> None:
        ...
    
    if _file:
        ...
    def tmpnam(self):
        ...
    
    def open(self, file, flags, mode=..., *args, **kw):
        """Called for low-level os.open()"""
        ...
    


WRITE_FLAGS = functools.reduce(operator.or_, [getattr(_os, a, 0) for a in "O_WRONLY O_RDWR O_APPEND O_CREAT O_TRUNC O_TEMPORARY".split()])
class SandboxViolation(DistutilsError):
    """A setup script attempted to modify the filesystem outside the sandbox"""
    tmpl = ...
    def __str__(self) -> str:
        ...
    


