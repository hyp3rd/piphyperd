"""
THIS SOFTWARE IS PROVIDED AS IS
and under GNU General Public License. <https://www.gnu.org/licenses/gpl-3.0.en.html>
USE IT AT YOUR OWN RISK.

PipHyperd cli interface.

The module is published on PyPi <https://pypi.org/project/piphyperd/>.

The code is available on GitLab <https://gitlab.com/hyperd/piphyperd>.
"""

import sys
import argparse
import os
from typing import Optional, List, Any
from pathlib import Path

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if not PATH in sys.path:
    sys.path.insert(1, PATH)
    from piphyperd import PipHyperd
    from cmdproxy import CmdProxy
del PATH


def main(python_path: Optional[Path] = None, command: str = "") -> int:
    """
    This function is called when run as python3 -m ${MODULE}
    Parse any additional arguments and call required module functions.
    """

    if sys.argv:
        # called through CLI
        # module_name = __loader__.name.split('.')[0]
        parser = argparse.ArgumentParser(
            prog="piphyperd",
            description="piphyperd is a pip wrapper for packages management within your workflows.",
        )

        parser.add_argument('--python_path', action='store', nargs=1, required=False, type=str,
                            default=[sys.executable],
                            help="Path to a python binary different than the systmes'")

        parser.add_argument('command', nargs=1, type=str,
                            default=["list"],
                            help="Provide a valid pip command")

        parser.add_argument('--packages', action="store", nargs="+", required=False, type=str,
                            help="Provide a list of packages")

        # argparser provides us a list, even if only one argument
        args = parser.parse_args(sys.argv[1:])

        # check for alternative python path used to initialize the
        if args.python_path:
            if isinstance(args.python_path, list) and isinstance(args.python_path[0], str):
                python_path = Path(args.python_path[0])

        # check for alternative python path
        if args.command:
            if isinstance(args.command, list) and isinstance(args.command[0], str):
                command = args.command[0]

        command_args: List[str] = []
        if args.packages:
            command_args = list()
            if isinstance(args.packages, list) and isinstance(args.packages[0], str):
                command_args.clear()
                for package in args.packages:
                    command_args.append(package)

        switcher = {
            "freeze": CmdProxy.freeze,
            "list": CmdProxy.list_packages,
            "show": CmdProxy.show,
            "check": CmdProxy.check,
            "install": CmdProxy.install,
            "uninstall": CmdProxy.uninstall,
            "download": CmdProxy.download,
        }

        func: Any = switcher.get(command, lambda: 'Invalid pip command')

    instance = PipHyperd(python_path=python_path)

    _, _, exit_code = func(
        instance) if not command_args else func(instance, command_args)

    # _, _, exit_code = func(
    #     instance, command_args) if not command_args is not None else func(instance)

    return int(exit_code)
