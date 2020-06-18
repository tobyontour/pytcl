import unittest

from pytcl.interp import Interpreter, IncorrectNumberOfArgumentsError


class TestSetCommand(unittest.TestCase):
    def test_simple_set_script_integer(self):
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

    def test_simple_set_script_string(self):
        interp = Interpreter()

        interp.eval('set x "5"')

        self.assertEqual(interp.get('x'), '5')

    def test_string_set(self):
        interp = Interpreter()

        interp.eval('set x "This is a string"')

        self.assertEqual(interp.get('x'), 'This is a string')

    def test_string_starting_with_number_set(self):
        """ Not keen on this aspect of Tcl """
        interp = Interpreter()

        interp.eval('set x 123.4234excel')

        self.assertEqual(interp.get('x'), '123.4234excel')

    def test_float_set(self):
        interp = Interpreter()

        interp.eval('set x 12.34')

        self.assertEqual(interp.get('x'), 12.34)

    def test_float_with_exponent_set(self):
        interp = Interpreter()

        interp.eval('set x 12.34e-14')

        self.assertEqual(interp.get('x'), 1.234e-13)

if __name__ == '__main__':
    unittest.main()