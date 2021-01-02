"""
This type stub file was generated by pyright.
"""

import re

"""
Filename globbing utility. Mostly a copy of `glob` from Python 3.5.

Changes include:
 * `yield from` and PEP3102 `*` removed.
 * Hidden files are not ignored.
"""
def glob(pathname, recursive=...):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    ...

def iglob(pathname, recursive=...):
    """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    ...

def glob1(dirname, pattern):
    ...

def glob0(dirname, basename):
    ...

def glob2(dirname, pattern):
    ...

magic_check = re.compile('([*?[])')
magic_check_bytes = re.compile(b'([*?[])')
def has_magic(s):
    ...

def escape(pathname):
    """Escape all special characters.
    """
    ...

