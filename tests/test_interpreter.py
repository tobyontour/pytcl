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

    def test_simple_set_string_script(self):
        interp = Interpreter()

        interp.eval('set x "5"')

        self.assertEqual(interp.get('x'), '5')

    def test_simple_set_string_script_2(self):
        interp = Interpreter()

        interp.set('x', "The quick brown fox")

        self.assertEqual(interp.get('x'), 'The quick brown fox')

    def test_cannot_set_variable_to_class(self):
        interp = Interpreter()

        with self.assertRaises(Exception) as context:
            interp.set('x', interp)

        self.assertTrue("Cannot set a variable to type <class 'pytcl.interp.Interpreter'>" in str(context.exception))

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

    def test_malformed_script_1(self):
        interp = Interpreter()

        with self.assertRaises(Exception) as context:
            interp.eval('set x ]')
        self.assertTrue("Unexpected character ']'" in str(context.exception))

    def test_malformed_script_2(self):
        interp = Interpreter()

        with self.assertRaises(Exception) as context:
            interp.eval('set x "cat"se')

        self.assertTrue("Expecting space but got 'se'" in str(context.exception))
