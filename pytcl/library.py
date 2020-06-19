from .tokens import Tokenizer, Token

class CommandError(Exception):
    pass

class IncorrectNumberOfArgumentsError(CommandError):
    pass

class VariableDoesNotExistError(CommandError):
    pass

class CommandNotFoundError(CommandError):
    pass

class CommandFactory():

    def get(self, command_name: str, variables: dict):
        if command_name == 'set':
            return SetCommand(variables)
        elif command_name == 'error':
            return ErrorCommand(variables)
        else:
            raise CommandNotFoundError(f'Command "{command_name}" not found.')

class Command():
    name = ''

    def __init__(self, variables: dict):
        self.variables = variables

    def call(self, args: [Token]) -> bool: # pragma: no cover
        pass

    def help(self): # pragma: no cover
        return "Base command."

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

class ErrorCommand(Command):
    name = 'error'

    def call(self, args: [Token]) -> bool:
        self.assertNumberOfArguments(1, args)
        raise CommandError(args[0].value)

    def help(self):
        return "error: Returns an error."

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
        return "set: Read and write variables."

