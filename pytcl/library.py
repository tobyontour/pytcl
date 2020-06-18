from .tokens import Tokenizer, Token

class CommandError(Exception):
    pass

class IncorrectNumberOfArgumentsError(CommandError):
    pass

class VariableDoesNotExistError(CommandError):
    pass

class Command():
    name = 'nop'

    def __init__(self, variables: dict):
        self.variables = variables

    def call(args: [Token]) -> bool:
        if len(args) != 0:
            raise IncorrectNumberOfArgumentsError("Expected 0 arguments.")
        return True

    def help(self):
        return "Null command."

    def __str__(self):
        return f'<Command, {self.name}>'

    def assertNumberOfArguments(self, expected: int, args = []):
        actual = len(args)
        if actual != expected:
            raise IncorrectNumberOfArgumentsError(f"{self.name}: Expected {expected} arguments but received {actual}.")

    def assertNumberOfArgumentsMultiple(self, expected: [], args = []):
        actual = len(args)
        if len(args) not in expected:
            temp = ' or '.join(str(i) for i in expected)
            raise IncorrectNumberOfArgumentsError(f"{self.name}: Expected {temp} arguments but received {actual}.")

class SetCommand(Command):
    name = 'set'

    def call(self, args: [Token]) -> bool:
        self.assertNumberOfArgumentsMultiple([1, 2], args)
        if len(args) == 1:
            if args[0].value in self.variables:
                return self.variables[args[0].value]
            else:
                raise VariableDoesNotExistError(f'set: Variable "{args[0].value}" does not exist.')
        if args[0].type != Token.NAME:
            raise CommandError(f'Invalid variable name "{args[0].value}"')
        self.variables[args[0].value] = args[1]
        return args[1]

    def help(self):
        return "set - Read and write variables"

