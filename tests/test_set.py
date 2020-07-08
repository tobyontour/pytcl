import unittest

from pytcl.interp import Interpreter
from pytcl.command import IncorrectNumberOfArgumentsError, VariableDoesNotExistError
from pytcl.stdlib import SetCommand


class TestSetCommand(unittest.TestCase):
    def test_metadata(self):
        cmd = SetCommand({})
        self.assertEqual(cmd.help(), "set: Read and write variables.")
        self.assertEqual(str(cmd), "<Command, set>")

    def test_invalid_name(self):
        interp = Interpreter()

        with self.assertRaises(Exception) as context:
            interp.eval('set 3 5')

        self.assertTrue('Invalid variable name "3"' in str(context.exception))

    def test_simple_set_script_integer(self):
        interp = Interpreter()

        interp.eval('set x 5')

        self.assertEqual(interp.get('x'), 5)

    def test_simple_set_script_incorrect_args(self):
        interp = Interpreter()

        with self.assertRaises(IncorrectNumberOfArgumentsError) as context:
            interp.eval('set')

        self.assertTrue("set: Expected 1 or 2 arguments but received 0" in str(context.exception))

    def test_simple_set_script_incorrect_args_excess(self):
        interp = Interpreter()

        with self.assertRaises(IncorrectNumberOfArgumentsError) as context:
            interp.eval('set x 5 4')

        self.assertTrue("set: Expected 1 or 2 arguments but received 3" in str(context.exception))

    def test_simple_set_script_string(self):
        interp = Interpreter()

        interp.eval('set x "5"')

        self.assertEqual(interp.get('x'), '5')

    def test_string_set(self):
        interp = Interpreter()

        interp.eval('set x "This is a string"')

        self.assertEqual(interp.get('x'), 'This is a string')

    def test_simple_set_script_string_single_quote(self):
        interp = Interpreter()

        interp.eval('set x \'5\'')

        self.assertEqual(interp.get('x'), '5')

    def test_string_set_single_quote(self):
        interp = Interpreter()

        interp.eval('set x \'This is a string\'')

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

    def test_simple_set_read(self):
        interp = Interpreter()

        interp.eval('set x "5"')
        result = interp.eval('set x')

        self.assertEqual(result.value, '5')
        self.assertEqual(interp.get('x'), '5')

    def test_simple_set_read_not_exist(self):
        interp = Interpreter()

        with self.assertRaises(VariableDoesNotExistError) as context:
            interp.eval('set x')

        self.assertTrue('set: Variable "x" does not exist.' in str(context.exception))

    def test_two_sets(self):
        interp = Interpreter()

        interp.eval('set x "This is the first string"')
        interp.eval('set x "This is the second string"')

        self.assertEqual(interp.get('x'), 'This is the second string')
