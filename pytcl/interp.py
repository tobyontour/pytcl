
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
