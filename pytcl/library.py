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
        elif command_name in ["after" "append" "apply" "array" "auto_execok" "auto_import" "auto_load" "auto_load_index"
            "auto_qualify" "binary" "break" "case" "catch" "cd" "chan" "clock" "close" "concat" "continue" "coroutine"
            "dict" "encoding" "eof" "error" "eval" "exec" "exit" "expr" "fblocked" "fconfigure" "fcopy" "file" "fileevent"
            "flush" "for" "foreach" "format" "gets" "glob" "global" "history" "if" "incr" "info" "interp" "join" "lappend"
            "lassign" "lindex" "linsert" "list" "llength" "lmap" "load" "lrange" "lrepeat" "lreplace" "lreverse" "lsearch"
            "lset" "lsort" "namespace" "open" "package" "pid" "proc" "puts" "pwd" "read" "regexp" "regsub" "rename"
            "return" "scan" "seek" "set" "socket" "source" "split" "string" "subst" "switch" "tailcall" "tclLog" "tell"
            "throw" "time" "trace" "try" "unknown" "unload" "unset" "update" "uplevel" "upvar" "variable" "vwait" "while"
            "yield" "yieldto" "zlib"]:
            raise CommandNotFoundError(f'Command "{command_name}" not implemented yet.')
        else:
            raise CommandNotFoundError(f'Command "{command_name}" not found.')

