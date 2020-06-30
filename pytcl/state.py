

class Variable():
    ref_count = 0
    type_name = ""
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def increment_reference_count(self):
        self.ref_count += 1

    def decrement_reference_count(self):
        if self.ref_count > 0:
            self.ref_count -= 1

    def is_referenced(self):
        return self.ref_count > 0

class State():
    stack = []

    def __init__(self):
        stack = [{}]

    def init_globals(self):
        stack[0]['argv0'] = ''
        stack[0]['argv'] = ''
        stack[0]['argc'] = ''
        stack[0]['tcl_platform'] = {
            'engine' = 'pyTcl'
        }
        stack[0]['tcl_interactive'] = 0
        stack[0]['tcl_version'] = 0


