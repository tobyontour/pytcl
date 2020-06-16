

class IncorrectNumberOfArgumentsError(Exception):
    pass

class Interpreter():
    """Main interpreter"""

    def __init__(self):
        self.variables = {}

    def set(self, variable_name, value):
        self.variables[variable_name] = value

    def get(self, variable_name):
        try:
            return self.variables[variable_name]
        except KeyError:
            return None

    def eval(self, script):
        tokens = script.split(' ')
        if len(tokens) > 0:
            self.call(tokens.pop(0), tokens)

    def call(self, command, args):
        if command == 'set':
            if len(args) == 2:
                if args[1][0].isdigit():
                    self.variables[args[0]] = int(args[1])
                else:
                    self.variables[args[0]] = args[1]
            else:
                raise IncorrectNumberOfArgumentsError(f"set requires 2 arguments, {len(args)} given.")

