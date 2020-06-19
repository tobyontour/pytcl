from .tokens import Token

class CommandError(Exception):
    pass

class IncorrectNumberOfArgumentsError(CommandError):
    pass

class VariableDoesNotExistError(CommandError):
    pass

class CommandNotFoundError(CommandError):
    pass

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

