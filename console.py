#!/usr/bin/python3
"""Import and define class"""

import cmd

promt = "(hbnb)"

class HBNBCommand(cmd.Cmd):
    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True
        
    def do_EOF(self, args):
        """End of File to exit file."""
        return True
    
    def emptyline(self):
        """method so it should not execute anything"""
        pass
