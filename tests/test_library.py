import unittest

from pytcl.library import CommandFactory, SetCommand, ErrorCommand

class TestCommandFactory(unittest.TestCase):
    def test_add_command(self):

        factory = CommandFactory()
        factory.add('set', SetCommand)

    def test_invalid_command(self):

        factory = CommandFactory()
        with self.assertRaises(AssertionError) as context:
            factory.add('set', int)

    def test_add_multiple_commanda(self):

        factory = CommandFactory()
        factory.add_multiple({
            'set': SetCommand,
            'error': ErrorCommand
        })

        self.assertEqual({
            'set': SetCommand,
            'error': ErrorCommand
        }, factory.commands)

