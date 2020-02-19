#!/usr/bin/python3
"""
user module
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    User class model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
