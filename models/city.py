#!/usr/bin/python3
"""
city module
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    City class model
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initialization function
        """
        if (len(kwargs) != 0):
            super().__init__(**kwargs)
        else:
            super().__init__()
