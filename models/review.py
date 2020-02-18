#!/usr/bin/python3
"""
review module
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class model
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        initialization function
        """
        if (len(kwargs) != 0):
            super().__init__(**kwargs)
        else:
            super().__init__()
