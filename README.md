# Airbnb clone project
# AirBnB clone

## Definition

It's a simple system to preserve, read and modify models that represents entities for the airbnb services.

This behavior is achieved by the console program, this program is capable of reading a .json file , deserialize it and create instaces for python objects, also it's capable of modify existimg objects create new ones and store them again in tje .json file.

This module is just a little piece for the airbnb clone full implementation, will change it's scope in the future.

# The console

This tool have the following methods

## all
 usage:

> (hbtn) all
> "==JSON REPR FOR ALL OBJECTS IN STORAGE=="

## create:
 usage:

> (hbtn) create User
> 'f51cc840-88d1-4213-9b29-18a0d14743bb'
>

Where **User** can be any of the above classes, and it returns the id created for that single object

## show
 usage:

> (hbtn) show User f51cc840-88d1-4213-9b29-18a0d14743bb
> "==JSON EXAMPLE FOR USER=="

giving the class you want to get, and it's "correspondiente" id string

## destroy
  usage:

> (hbtn) destroy User f51cc840-88d1-4213-9b29-18a0d14743bb
>

destroys an instanece by the given id string



By: Daniel Rodriguez and Diego Garzon
