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

    def __init__(self, *args, **kwargs):
        """
        initialization function
        """
        if (len(kwargs) != 0):
            super().__init__(**kwargs)
        else:
            super().__init__()
