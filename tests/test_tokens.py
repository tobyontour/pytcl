import unittest

from pytcl.tokens import Tokenizer, Token


class TestTokenizer(unittest.TestCase):

    def test_consuming_string_simple(self):
        tokenizer = Tokenizer('"x"')

        tokenizer.consume()

        token = tokenizer.consume_string()

        self.assertEqual(token.type, Token.STRING)
        self.assertEqual(token.value, 'x')
        self.assertIsNone(tokenizer.c)

    def test_consuming_string_escaped(self):
        tokenizer = Tokenizer('"The quick brown fox said \\\"Hi\\\" to me."')

        tokenizer.consume()

        token = tokenizer.consume_string()

        self.assertEqual(token.type, Token.STRING)
        self.assertEqual(token.value, 'The quick brown fox said "Hi" to me.')
        self.assertIsNone(tokenizer.c)

    def test_consuming_broken_string_escaped(self):
        tokenizer = Tokenizer('"The quick brown fox said \\\"Hi\\\" to me.')

        tokenizer.consume()

        with self.assertRaises(Exception) as context:
            token = tokenizer.consume_string()

        self.assertTrue("Expected '\"' not end of line" in str(context.exception))

    def test_consuming_number_int(self):
        tokenizer = Tokenizer('123')

        token = tokenizer.consume_number()

        self.assertEqual(token.type, Token.INT)
        self.assertEqual(token.value, 123)
        self.assertIsNone(tokenizer.c)

    # def test_simple_character(self):
    #     tokenizer = Tokenizer('x')

    #     token = tokenizer.get_next_token()

    #     self.assertEqual(token.type, Tokenizer.NAME)
    #     self.assertEqual(token.value, 'x')

    # def test_simple_string(self):

    #     interp = Interpreter()

    #     self.assertEqual(interp.tokenise('"This is a string"'), ['This is a string'])

    # def test_simple_string_set(self):

    #     interp = Interpreter()

    #     self.assertEqual(interp.tokenise('set x "This is a string"'), ['set', 'x', 'This is a string'])

    # def test_simple_number_set(self):

    #     interp = Interpreter()

    #     self.assertEqual(interp.tokenise('set x 5'), ['set', 'x', '5'])