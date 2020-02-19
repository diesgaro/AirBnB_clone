# Airbnb clone project

## Definition

It's a simple system to preserve, read and modify models that represents entities for the airbnb services.

This behavior is achieved by the console program, this program is capable of reading a .json file , deserialize it and create instaces for python objects, also it's capable of modify existimg objects create new ones and store them again in tje .json file.

This module is just a little piece for the airbnb clone full implementation, will change it's scope in the future.

## The console

To run this tool you type

```
$ ./console.py
(hbtn)
```
This tool have the following methods

### help
 usage:
 
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

you can get specific information of one method

```
(hbnb) help create
Usage: create <class_name>
```


### all
 usage:
```
(hbtn) all
["[User] (98b9072f-ce8d-4856-b7a7-2004f91815d4) {'created_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505440), 'updated_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505466), 'id': '98b9072f-ce8d-4856-b7a7-2004f91815d4'}", "[BaseModel] (76e5ff68-6fd8-4e4b-9111-eb8dbb9eb2bb) {'created_at': datetime.datetime(2020, 2, 19, 22, 23, 55, 671400), 'updated_at': datetime.datetime(2020, 2, 19, 22, 23, 55, 671482), 'id': '76e5ff68-6fd8-4e4b-9111-eb8dbb9eb2bb'}"]
```
you can also specify the class objects you want to retrieve

```
(hbtn) all User
["[User] (98b9072f-ce8d-4856-b7a7-2004f91815d4) {'created_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505440), 'updated_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505466), 'id': '98b9072f-ce8d-4856-b7a7-2004f91815d4'}"]
```

### create:
 usage:
```
(hbtn) create User
98b9072f-ce8d-4856-b7a7-2004f91815d4
```

Where **User** can be any of the above classes, and it returns the id created for that single object

### show
 usage:
```
(hbtn) show User 98b9072f-ce8d-4856-b7a7-2004f91815d4
[User] (98b9072f-ce8d-4856-b7a7-2004f91815d4) {'created_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505440), 'updated_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505466), 'id': '98b9072f-ce8d-4856-b7a7-2004f91815d4'}
```
giving the class you want to get, and it's "correspondiente" id string

### destroy
  usage:
```
(hbtn) destroy User f51cc840-88d1-4213-9b29-18a0d14743bb
```

destroys an instanece by the given id string

### update
  usage:
```
(hbnb) update User 98b9072f-ce8d-4856-b7a7-2004f91815d4 name "Diego Garzon"
(hbnb) show User 98b9072f-ce8d-4856-b7a7-2004f91815d4
[User] (98b9072f-ce8d-4856-b7a7-2004f91815d4) {'updated_at': datetime.datetime(2020, 2, 19, 22, 29, 17, 431002), 'created_at': datetime.datetime(2020, 2, 19, 22, 22, 12, 505440), 'name': 'Diego Garzon', 'id': '98b9072f-ce8d-4856-b7a7-2004f91815d4'}

```
## Classes included
### User

* email: string 
* password: string 
* first_name: string 
* last_name: string 

## State

* name: string

## City

* state_id: string
* name: string
## Amenity

* name: string

## Place

* city_id: string
* user_id: string
* name: string
* description: string
* number_rooms: integer
* number_bathrooms: integer
* max_guest: integer
* price_by_night: integer
* latitude: float
* longitude: float
* amenity_ids: list of string

## Review

* place_id: string
* user_id: string
* text: string

## Authors
* **Diego Garzon** - [Email] (mailto:digarodev@gmail.com)
* **Daniel Rodriguez** - [Email] (mailto:danrodcastillo1994@gmail.com)
