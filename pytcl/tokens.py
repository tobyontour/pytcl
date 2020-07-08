import re
from typing import List

class Token():
    UNKNOWN = 0
    EOF = 1
    WHITESPACE = 2
    NAME = 3
    INT = 4
    STRING = 5
    FLOAT = 6

    token_names = [
        'Unknown',
        'EOF',
        'Whitespace',
        'Name',
        'Integer',
        'String',
        'Float',
    ]

    type = 0
    value = ""

    def __init__(self, type: int, value = ""):
        self.type = type
        self.value = value

    def is_eol(self):
        return self.value in ['\n', ';']

    def __str__(self):
        token_name = Token.token_names[self.type]
        return f"<'{self.value}', {token_name}>"

Tokens = List[Token]

class Tokenizer():

    c = None

    def __init__(self, script: str):
        self.script = script
        self.ptr = 0
        if len(script) > 0:
            self.c = script[0]

    def eof(self):
        return self.c is None

    def consume(self):
        self.ptr += 1
        if self.ptr >= len(self.script):
            self.c = None
        else:
            self.c = self.script[self.ptr]

    # def match(self, x: str):
    #     if (self.c == x):
    #         self.consume()
    #     else:
    #         raise Exception(f"Expected '{x}' but got '{self.c}'")

    def is_whitespace(self, c):
        return c in [' ', '\t', '\r', '\n']

    def whitespace(self) -> Token:
        nl = False
        while self.is_whitespace(self.c):
            if self.c == '\n':
                nl = True
            self.consume()

        if nl:
            return Token(Token.WHITESPACE, '\n')
        else:
            return Token(Token.WHITESPACE, ' ')

    def consume_string(self, delimiter = '"', prefix = '') -> Token:
        escaped = False
        closed = False
        value = prefix
        if self.c == delimiter:
            self.consume()
        while self.c is not None:
            if self.c == '\\' and not escaped:
                escaped = True
            elif self.c == delimiter and not escaped:
                self.consume()
                closed = True
                break
            else:
                escaped = False
                value += self.c
            self.consume()
        if not closed and not self.is_whitespace(delimiter):
            raise Exception(f"Expected '{delimiter}' not end of line")
        return Token(Token.STRING, value)

    def consume_number(self) -> Token:
        value = ""
        allowed_characters = ['+', '-', '.']
        while self.c is not None:
            if self.c.isdigit() or self.c in allowed_characters:
                value += self.c
                self.consume()
            else:
                break
            allowed_characters.append('e')

        integer_p = re.compile(r'^[\+\-]?[0-9]+$')
        if integer_p.match(value):
            return Token(Token.INT, int(value))

        float_p = re.compile(r'^[\+\-]?[0-9]+(\.[0-9]+)(e[\+\-][0-9]+)?$')
        if float_p.match(value):
            return Token(Token.FLOAT, float(value))

        return self.consume_string(' ', value)

    def consume_name(self) -> Token:
        value = ""
        while self.c is not None and self.c.isalpha():
            value += self.c
            self.consume()
        return Token(Token.NAME, value)

    def get_next_token(self) -> Token:
        while self.c is not None:
            if self.is_whitespace(self.c):
                return self.whitespace()
            elif self.c == '"':
                return self.consume_string('"')
            elif self.c == "'":
                return self.consume_string('\'')
            elif self.c.isdigit():
                return self.consume_number()
            elif self.c.isalpha():
                return self.consume_name()
            else:
                raise Exception(f"Unexpected character '{self.c}'")

        return Token(Token.EOF)
