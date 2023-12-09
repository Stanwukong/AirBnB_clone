#!/usr/bin/python3
"""Defines the entry point of this command interpreter."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter
    """
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        words = arg.split()
        if len(words) == 2:
            for i, v in enumerate(words):
                if i == 0:
                    if v != "BaseModel":
                        print("** class doesn't exist **")
                        return
                elif i == 1:
                    with open("file.json", "r") as file:
                        data = json.load(file)
                        for item in data.values():
                            del item["__class__"]

                        for k, o in data.items():
                            if k == f"BaseModel.{words[1]}":
                                print(f"[BaseModel] ({words[1]})", o)
                                return
                    print("** no instance found **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 0:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Executes nothing on empty line
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
