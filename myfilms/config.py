import os
from configparser import ConfigParser
from functools import cache


class Config:
    @staticmethod
    @cache
    def version():
        try:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".version")) as f:
                return f.read()
        except FileNotFoundError:
            return None
