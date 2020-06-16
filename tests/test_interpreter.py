import unittest

from pytcl.interp import Interpreter


class TestInterp(unittest.TestCase):

    def test_set_and_get_variable(self):
        """
        Test that we can set and get a variable.
        """
        interp = Interpreter()

        interp.set('x', 5)

        self.assertEqual(interp.get('x'), 5)

    def test_get_undefined_variable(self):
        """
        Test that we can set and get a variable.
        """
        interp = Interpreter()

        self.assertEqual(interp.get('x'), None)

if __name__ == '__main__':
    unittest.main()