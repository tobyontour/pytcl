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

    def test_eof(self):
        tokenizer = Tokenizer('123')

        token = tokenizer.consume_number()

        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.EOF)
        self.assertEqual(token.value, '')
        self.assertIsNone(tokenizer.c)

    def test_consuming_string_not_float(self):
        tokenizer = Tokenizer('"Hello world."')

        tokenizer.consume()

        token = tokenizer.consume_string()

        self.assertEqual(token.type, Token.STRING)
        self.assertEqual(token.value, 'Hello world.')
        self.assertIsNone(tokenizer.c)

    def test_line(self):
        tokenizer = Tokenizer('error "Hello world." 34 4.5')

        # error
        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.NAME)
        self.assertEqual(token.value, 'error')

        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.WHITESPACE)

        # 'Hello world.'
        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.STRING)
        self.assertEqual(token.value, 'Hello world.')

        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.WHITESPACE)

        # 34
        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.INT)
        self.assertEqual(token.value, 34)

        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.WHITESPACE)

        # 4.5
        token = tokenizer.get_next_token()
        self.assertEqual(token.type, Token.FLOAT)
        self.assertEqual(token.value, 4.5)