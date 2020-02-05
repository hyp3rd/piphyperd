"""
THIS SOFTWARE IS PROVIDED AS IS
and under GNU General Public License. <https://www.gnu.org/licenses/gpl-3.0.en.html>
USE IT AT YOUR OWN RISK.

PipHyperd unit testing.

The module is published on PyPi <https://pypi.org/project/piphyperd/>.

The code is available on GitLab <https://gitlab.com/hyperd/piphyperd>.
"""

import unittest
import sys
import os

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not PATH in sys.path:
    sys.path.insert(1, PATH)
    from piphyperd import PipHyperd
del PATH


class TestMethods(unittest.TestCase):

    """
    PipHyperd unit testing class
    """

    def setUp(self):
        """
        tests setup
        """
        self.piphyperd = PipHyperd()

    def test_is_not_none(self):
        """
        Assert that PipHyperd is not None
        """
        self.assertIsNotNone(self.piphyperd)

    def test_wrong_python_path(self):
        """
        Raise a FileNotFoundError when initialized with a wrong python path
        """
        with self.assertRaises(FileNotFoundError):
            PipHyperd(python_path="/path/to/nothing").check()

    def test_list_outdated(self):
        """
        Assert that Latest is in the output
        """
        output = self.piphyperd.list(True)
        self.assertIn("Latest", output)


if __name__ == '__main__':
    unittest.main()
