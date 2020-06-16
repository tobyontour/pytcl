

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
        tokens = self.tokenise(script)
        if len(tokens) > 0:
            self.call(tokens.pop(0), tokens)

    def call(self, command, args):
        if command == 'set':
            if len(args) == 2:
                if args[1][0].isdigit():
                    self.variables[args[0]] = int(args[1])
                elif args[1][0] == '"' and args[1][-1] == '"' and len(args[1]) > 2:
                    self.variables[args[0]] = args[1][1:-1]
                elif args[1][0] == "'" and args[1][-1] == "'" and len(args[1]) > 2:
                    self.variables[args[0]] = args[1][1:-1]

                else:
                    self.variables[args[0]] = args[1]
            else:
                raise IncorrectNumberOfArgumentsError(f"set requires 2 arguments, {len(args)} given.")

    def tokenise(self, script):
        WAITING = 0
        WAITING_FOR_SPACE = 1
        MID_TOKEN = 2
        DOUBLE_QUOTES = 3
        SINGLE_QUOTES = 4
        tokens = []
        token = ""
        state = WAITING
        for i, char in enumerate(script):
            # print(f"== {state} {char} -> ", end=' ')
            if char == ' ':
                if state == WAITING:
                    pass
                elif state == WAITING_FOR_SPACE:
                    state = WAITING
                elif state == MID_TOKEN:
                    tokens.append(token)
                    token = ""
                    state = WAITING
                else:
                    token = token + char
            elif state == WAITING_FOR_SPACE:
                raise Exception(f"Expected space at character {i}")
            elif char == '"' and state == WAITING:
                state = DOUBLE_QUOTES
            elif char == '"' and state == DOUBLE_QUOTES:
                tokens.append(token)
                token = ""
                state = WAITING_FOR_SPACE
            elif char == "'" and state == WAITING:
                state = SINGLE_QUOTES
            elif char == "'" and state == SINGLE_QUOTES:
                tokens.append(token)
                token = ""
                state = WAITING_FOR_SPACE
            else:
                token = token + char
                if state == WAITING:
                    state = MID_TOKEN
            # print(f"{state}   ({token})")
        if state == MID_TOKEN and len(token) > 0:
            tokens.append(token)

        return tokens

