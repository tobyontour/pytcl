import unittest

from pytcl.interp import Interpreter
from pytcl.command import IncorrectNumberOfArgumentsError, CommandError
from pytcl.stdlib import ErrorCommand


class TestErrorCommand(unittest.TestCase):
    def test_metadata(self):
        cmd = ErrorCommand({})
        self.assertEqual(cmd.help(), "error: Returns an error.")
        self.assertEqual(str(cmd), "<Command, error>")

    def test_normal(self):
        interp = Interpreter()

        with self.assertRaises(CommandError) as context:
            interp.eval('error "Hello world."')

        self.assertTrue('Hello world.' in str(context.exception))

    def test_invalid_arguments(self):
        interp = Interpreter()

        with self.assertRaises(IncorrectNumberOfArgumentsError) as context:
            interp.eval('error "Hello world." 34')

        self.assertTrue('error: Expected 1 arguments but received 2.' in str(context.exception))
