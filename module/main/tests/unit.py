import unittest
import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not path in sys.path:
    sys.path.insert(1, path)
del path

try:
    from piphyperd import PipHyperd
except Exception as module_not_found:
    print("No module piphyperd found")


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.piphyperd = PipHyperd()

    def test_add(self):
        self.assertIsNotNone(self.piphyperd)


if __name__ == '__main__':
    unittest.main()
