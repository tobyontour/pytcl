from .tokens import Tokenizer, Token
from .command import CommandNotFoundError, Command
from .stdlib import commands as stdlib_commands

class CommandFactory():

    commands = {}

    def __init__(self):
        self.add_multiple(stdlib_commands)

    def add(self, command_name: str, command_class):
        assert issubclass(command_class, Command), ""
        self.commands[command_name] = command_class

    def add_multiple(self, commands: dict):
        self.commands.update(commands)

    def get(self, command_name: str, variables: dict):
        if command_name in self.commands:
            return self.commands[command_name](variables)
        else:
            raise CommandNotFoundError(f'Command "{command_name}" not found.')

