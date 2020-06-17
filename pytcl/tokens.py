
class Token():
    EOF = 0
    WHITESPACE = 1
    NAME = 2
    INT = 3
    STRING = 4

    token_names = [
        'EOF',
        'Whitespace',
        'Name',
        'Integer',
        'String',
    ]

    type = None
    value = ""

    def __init__(self, type: int, value = ""):
        self.type = type
        self.value = value

    def __str__(self):
        tname = Token.token_names[self.type]
        return f"<'{self.value}', {tname}>"

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

    def match(self, x: str):
        if (self.c == x):
            self.consume()
        else:
            raise Exception(f"Expected '{x}' but got '{self.c}'")

    def whitespace(self) -> Token:
        while self.c in [" "]:
            self.consume()
        return Token(Token.WHITESPACE)

    def consume_string(self, delimiter = '"') -> Token:
        escaped = False
        closed = False
        value = ""
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
        if not closed:
            raise Exception(f"Expected '{delimiter}' not end of line")
        return Token(Token.STRING, value)

    def consume_number(self) -> Token:
        value = ""
        while self.c is not None and self.c.isdigit():
            value += self.c
            self.consume()
        return Token(Token.INT, int(value))

    def consume_name(self) -> Token:
        value = ""
        while self.c is not None and self.c.isalpha():
            value += self.c
            self.consume()
        return Token(Token.NAME, value)

    def get_next_token(self) -> Token:
        print(f">{self.c}<")
        while self.c is not None:
            # print(f"== {state} {char} -> ", end=' ')
            if self.c == ' ':
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
            # print(f"{state}   ({token})")

        return Token(Token.EOF, None)