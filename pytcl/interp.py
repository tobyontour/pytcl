
from typing import List
from .tokens import Tokenizer, Token

Tokens = List[Token]

class IncorrectNumberOfArgumentsError(Exception):
    pass

class Interpreter():
    """Main interpreter"""

    def __init__(self):
        self.variables = {}

    def set(self, variable_name, value):
        if type(value) is int:
            self.variables[variable_name] = Token(Token.INT, value)
        elif type(value) is str:
            self.variables[variable_name] = Token(Token.STRING, value)
        else:
            raise Exception("Cannot set a variable to type " + str(type(value)))

    def get(self, variable_name):
        try:
            return self.variables[variable_name].value
        except KeyError:
            return None

    def eval(self, script):
        tokens = self.tokenise(script)
        if len(tokens) > 0:
            if tokens[0].type == Token.NAME:
                self.call(tokens.pop(0).value, tokens)

    def call(self, command, args: Tokens):
        if command == 'set':
            if len(args) == 2:
                if args[0].type != Token.NAME:
                    raise Exception(f'Invalid variable name "{args[0].value}"')
                self.variables[args[0].value] = args[1]
            else:
                raise IncorrectNumberOfArgumentsError(f"set requires 2 arguments, {len(args)} given.")

    def tokenise(self, script) -> Tokens:
        tokenizer = Tokenizer(script)

        token_list = []
        expecting_space = False

        while not tokenizer.eof():
            token = tokenizer.get_next_token()
            if expecting_space and token.type != Token.WHITESPACE:
                raise Exception(f"Expecting space but got '{token.value}'")
            elif expecting_space and token.type == Token.WHITESPACE:
                expecting_space = False
            elif token.type != Token.WHITESPACE:
                token_list.append(token)
                expecting_space = True

        return token_list

