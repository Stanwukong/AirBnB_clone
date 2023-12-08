#!/usr/bin/python3
"""Defines the entry point of this command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

    def emptyline(self):
        """Executes nothing on empty line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
