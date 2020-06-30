from .tokens import Token
from .command import Command, CommandError, VariableDoesNotExistError

class ErrorCommand(Command):
    name = 'error'

    def call(self, args: [Token]) -> bool:
        self.assertNumberOfArgumentsMultiple([1, 2, 3], args)
        raise CommandError(args[0].value)

    def help(self):
        return "error: Returns an error."

    def syntax(self):
        return f'{self.name} message ?info? ?code?'

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

    def syntax(self):
        return f'{self.name} varName ?value?'

commands = {
    'set': SetCommand,
    'error': ErrorCommand
}
