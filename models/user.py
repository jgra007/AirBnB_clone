#!/usr/bin/python3
"""user.py module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class implementation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
