import unittest

from pytcl.interp import Interpreter, IncorrectNumberOfArgumentsError


class TestTokeniser(unittest.TestCase):

    def test_simple_character(self):
        interp = Interpreter()

        self.assertEqual(interp.tokenise('x'), ['x'])

    def test_simple_string(self):

        interp = Interpreter()

        self.assertEqual(interp.tokenise('"This is a string"'), ['This is a string'])

    def test_simple_string_set(self):

        interp = Interpreter()

        self.assertEqual(interp.tokenise('set x "This is a string"'), ['set', 'x', 'This is a string'])

    def test_simple_number_set(self):

        interp = Interpreter()

        self.assertEqual(interp.tokenise('set x 5'), ['set', 'x', '5'])