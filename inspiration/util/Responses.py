from enum import Enum
import json


def blankRepsponse():
    pass

def blankError ():

    class ERROR_TYPES(Enum):
        OBJ_NOT_FOUND = 0x1

    def __init__(self, status, type, msg, **kwargs):
        pass

    def serialize(self):
        return json.dump(self.__dict__)

