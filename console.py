#!/usr/bin/python3
"""
Console cmd airbnb console
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Call a emptyline()"""
        pass

    def do_EOF(self, arg):
        """handle EOF"""
        return True

    def help_EOF(self):
        """Help to EOF"""
        print("EOF command to exit the program\n")

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def help_quit(self):
        """Help to quit"""
        print("Quit command to exit the program\n")

    def do_create(self, arg):
        """Create a new Instance"""
        argument = parse(arg)
        classes = [cl[0] for cl in globals().items()]

        if (len(arg) == 0):
            print("** class name missing **")
        elif (not argument[0] in classes):
            print("** class doesn't exist **")
        else:
            newModel = eval(argument[0]+'()')
            newModel.save()
            print(newModel.id)

    def help_create(self):
        """Help Create"""
        print("Usage: create <class_name>\n")

    def do_show(self, arg):
        """Show the string representation of an instance"""
        argument = parse(arg)
        classes = [cl[0] for cl in globals().items()]

        if (len(arg) == 0):
            print("** class name missing **")
        elif (not argument[0] in classes):
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print("** instance id missing **")
        else:
            res = None
            lis = models.storage.all()
            for key in lis.keys():
                if (lis[key].id == argument[1]):
                    res = lis[key]
            if (res is not None):
                print(res)
            else:
                print("** no instance found **")

    def help_show(self):
        """Help Show"""
        print("Usage: show <class_name> <id>\n")

    def do_destroy(self, arg):
        """Destroy the instance"""
        argument = parse(arg)
        classes = [cl[0] for cl in globals().items()]

        if (len(arg) == 0):
            print("** class name missing **")
        elif (not argument[0] in classes):
            print("** class doesn't exist **")
        elif len(argument) < 2:
            print("** instance id missing **")
        else:
            res = None
            lis = models.storage.all()
            for key in lis.keys():
                if (lis[key].id == argument[1]):
                    res = lis[key]
            if (res is not None):
                object_name = type(res).__name__+"."+res.id
                del lis[object_name]
                models.storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """Help destroy"""
        print("Usage: destroy <class_name> <id>\n")

    def do_all(self, arg):
        """Show all the instances"""
        argument = parse(arg)
        classes = [cl[0] for cl in globals().items()]

        if (len(arg) == 0):
            lis = []
            allInstances = models.storage.all()
            for el in allInstances.keys():
                p = allInstances[el].to_dict()
                lis.append(str(allInstances[el]))
            print(lis)
        elif (not argument[0] in classes):
            print("** class doesn't exist **")
        else:
            lis = []
            allInstances = models.storage.all()
            for el in allInstances.keys():
                p = allInstances[el].to_dict()
                if (p["__class__"] == argument[0]):
                    lis.append(str(allInstances[el]))
            print(lis)

    def help_all(self):
        """Help all"""
        print("Usage: all or all <class name>\n")

    def do_update(self, arg):
        """Update an instance"""
        argument = parse(arg)
        classes = [cl[0] for cl in globals().items()]

        if (len(arg) == 0):
            print("** class name missing **")
        elif (not argument[0] in classes):
            print("** class doesn't exist **")
        elif (len(argument) < 2):
            print("** instance id missing **")
        elif (len(argument) < 3):
            print("** attribute name missing **")
        elif (len(argument) < 4):
            print("** value missing **")
        else:
            myInstance = None
            allInstances = models.storage.all()
            for key in allInstances.keys():
                if (allInstances[key].id == argument[1]):
                    myInstance = allInstances[key]

            if (myInstance is None):
                print("** no instance found **")
            else:
                try:
                    if "." in argument[3]:
                        value = float(argument[3])
                    else:
                        value = int(argument[3])
                except Exception:
                    value = argument[3]
                myInstance.__dict__[argument[2]] = value
                myInstance.save()

    def help_update(self):
        """Help for update"""
        print("Usage: update <class_name> <id> <attr_name> \"<attr_value>\"\n")


def parse(arg):
    """ Split the arguments by spaces """
    finalString = arg.split("\"")
    fPart = finalString[0].split(" ")
    if len(finalString) > 1:
        fPart = fPart[:-1]
        fPart.append("".join(finalString[1]))
    return fPart


if __name__ == '__main__':
    HBNBCommand().cmdloop()
