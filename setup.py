"""THIS SOFTWARE IS PROVIDED AS IS.

Released under GNU General Public License:
<https://www.gnu.org/licenses/gpl-3.0.en.html>

USE IT AT YOUR OWN RISK.

PipHyperd setup.
It can provide automation and dependencies control within your workflows.

The module is published on PyPi: <https://pypi.org/project/piphyperd/>.
The code is available on GitLab: <https://gitlab.com/hyperd/piphyperd>.
"""

from __future__ import (absolute_import, division, print_function)
import codecs
import os
import re
from typing import Any
import setuptools

entry_points: str = """\"""THIS SOFTWARE IS PROVIDED AS IS.

Released under GNU General Public License:
<https://www.gnu.org/licenses/gpl-3.0.en.html>

USE IT AT YOUR OWN RISK.

PipHyperd is a simple python object to leverage pip programmatically.
It can provide automation and dependencies control within your workflows.

The module is published on PyPi: <https://pypi.org/project/piphyperd/>.
The code is available on GitLab: <https://gitlab.com/hyperd/piphyperd>.
\"""
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type  # pylint: disable=invalid-name

__version__ = \"{version}\"
__author__ = \"Hyper(d)\"
"""


def envstring(var: str) -> str:
    """Return environment var as string."""
    return os.environ.get(var) or ""


def read(rel_path: str) -> Any:
    """Read file helper."""
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, rel_path), 'r') as file_path:
        return file_path.read()


try:
    __long_description = read("README.md")
except FileNotFoundError:
    __long_description = ""

if os.path.isfile("variables"):
    try:
        VARIABLES = read("variables").strip().split("\n")
        for v in VARIABLES:
            key, value = v.split("=")
            os.environ[key] = re.sub("['\"]", "", value)
    except FileNotFoundError:
        pass


setuptools.setup(
    name=envstring("NAME"),

    # Version SCM based.
    use_scm_version={
        'write_to': 'module/main/release.py',
        'write_to_template': entry_points,
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
        'version_scheme': 'python-simplified-semver',
        'local_scheme': 'no-local-version',
    },

    description=envstring("DESCRIPTION"),
    long_description=__long_description,
    long_description_content_type="text/markdown",

    license='GPLv3',

    author=envstring("AUTHOR"),
    author_email=envstring("AUTHOR_EMAIL"),

    url=envstring("URL"),

    project_urls={
        "Documentation": envstring("URL"),
        "Source": envstring("DOCUMENTATION_URL"),
    },

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Plugins',
    ],

    install_requires=[
        'pipdeptree==2.0.0',
    ],

    packages=[
        envstring("NAME"), envstring("NAME") + ".main",
        envstring("NAME"), envstring("NAME") + ".cli",
    ],

    entry_points={
        "console_scripts": [
            "piphyperd=piphyperd.cli.parser:run",
        ]
    },

    python_requires='>=3.5.*',
    zip_safe=False,
)
