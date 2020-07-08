
from .tokens import Tokenizer, Token, Tokens
from .library import CommandFactory
from .state import State


class Interpreter():

    """Main interpreter"""
    def __init__(self):
        self.commands = CommandFactory()
        self.state = State()

    def set(self, variable_name, value):
        variables = self.state.get_globals()
        if type(value) is int:
            variables[variable_name] = Token(Token.INT, value)
        elif type(value) is str:
            variables[variable_name] = Token(Token.STRING, value)
        else:
            raise Exception("Cannot set a variable to type " + str(type(value)))

    def get(self, variable_name):
        variables = self.state.get_globals()
        try:
            return variables[variable_name].value
        except KeyError:
            return None

    def eval(self, script):
        tokens = self.tokenise(script)

        command = None

        while len(tokens) > 0:
            if tokens[0].type == Token.NAME:
                command = tokens.pop(0).value
                args = []
                for t in tokens:
                    if t.is_eol():
                        break
                    else:
                        args.append(tokens.pop(0))
                return self.call(command, args)
            else:
                raise Exception(f'invalid command name "{tokens[0].value}"')

    def call(self, command: str, args: Tokens):

        print(f"{command} (")
        for a in args:
            print(str(a))
        print(")")

        cmd = self.commands.get(command, self.state.get_current_scope())
        return cmd.call(args)

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

        for a in token_list:
            print(str(a))
        return token_list

