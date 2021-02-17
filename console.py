#!/usr/bin/python3
"""This is the console for the Holberton HNBN project"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Class HBNB command line console prompt
       prompt - The start prompt for the HBNB console
       group - contains all the classes used in the project
    """
    prompt = "(hbnb)"

    __list_class = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review']

    def do_EOF(self, line):
        """Executes the EOF (Ctrl -D/ Ctrl-Z) commands on console"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered
        Prints the prompt again
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__list_class:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args[0] + '()')
            storage.save()
            print(new_inst.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__list_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                print(objects[key_find])
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        objects = storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__list_class:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel
        """
        args = line.split()
        objects = storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)

        elif args[0] not in self.__list_class:
            print("** class doesn't exist **")

        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, arg):
        """updates an instance by class name and id adding or updating
        the attribute
        Args:
            arg (str): class name, instance id and attributes
        """
        args = arg.split()

        my_inst = getobj(arg)

        if my_inst:
            if len(args) < 3:
                errors("!att_name")
                return
            if len(args) < 4:
                errors("!value")
                return

            if args[2] in ("created_at", "updated_at", "id"):
                return

            if '"' in args[3]:
                i = 3
                concat = args[3].replace('"', "")
                i += 1
                while i < len(args):
                    if '"' in args[i]:
                        concat += " " + args[i].replace('"', "")
                        break
                    concat += " " + args[i]
                    i += 1
                if '"' in concat:
                    args[3] = concat.replace('"', "")
                else:
                    args[3] = concat

            try:
                convert = int(args[3])
            except ValueError:
                try:
                    convert = float(args[3])
                except ValueError:
                    convert = args[3]

            my_inst.__dict__[args[2]] = convert
            my_inst.save()

    def default(self, line):
        """ Dafault function """
        split_line = line.split('.')
        if len(split_line) > 1:
            if split_line[1] == "all()":
                self.do_all(split_line[0])
        else:
            cmd.Cmd.default(self, line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
