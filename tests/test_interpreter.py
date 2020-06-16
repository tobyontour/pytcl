import unittest

from pytcl.interp import Interpreter, IncorrectNumberOfArgumentsError


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
        Test that get None for an undefined variable.
        """
        interp = Interpreter()

        self.assertEqual(interp.get('x'), None)

    def test_simple_set_script(self):
        interp = Interpreter()

        interp.eval('set x 5')

        self.assertEqual(interp.get('x'), 5)

    def test_simple_set_script_incorrect_args(self):
        interp = Interpreter()

        with self.assertRaises(IncorrectNumberOfArgumentsError) as context:
            interp.eval('set x')

        self.assertTrue("set requires 2 arguments, 1 given." in str(context.exception))

    def test_simple_set_script_incorrect_args_excess(self):
        interp = Interpreter()

        with self.assertRaises(IncorrectNumberOfArgumentsError) as context:
            interp.eval('set x 5 4')

        self.assertTrue("set requires 2 arguments, 3 given." in str(context.exception))

if __name__ == '__main__':
    unittest.main()