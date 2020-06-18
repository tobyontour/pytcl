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

    # def test_string_set(self):
    #     interp = Interpreter()

    #     interp.eval('set x "This is a string"')

    #     self.assertEqual(interp.get('x'), 'This is a string')

if __name__ == '__main__':
    unittest.main()