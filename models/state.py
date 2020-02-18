#!/usr/bin/python3
"""
state module
"""


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class model
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        initialization function
        """
        if (len(kwargs) != 0):
            super().__init__(**kwargs)
        else:
            super().__init__()
