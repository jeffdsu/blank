from enum import Enum
import json


class blankRepsponse():
    pass

class blankError ():

    class ERROR_TYPES(Enum):

        OBJ_NOT_FOUND = 0x1

    ERROR_TYPE_TO_STATUS_MAP = {
        ERROR_TYPES.OBJ_NOT_FOUND : [404, "[%s] (%s) not {found}"]
    }

    def __init__(self, type, **kwargs):
        self.type = type
        self.status = self.ERROR_TYPE_TO_STATUS_MAP[self.type] [0]


        if self.type == self.ERROR_TYPES.OBJ_NOT_FOUND:
            self.err_msg = self.ERROR_TYPE_TO_STATUS_MAP[self.type] [1]%(str(kwargs['cls'].__name__), kwargs['id'])

    def serialize(self):
        # Jeff - anyone have better way to do this?
        temp_dict = dict()
        temp_dict['type'] = str(self.type)
        temp_dict['status'] = self.status
        temp_dict['err_msg'] = self.err_msg
        return temp_dict



## unit tests
if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blank.settings")
    from inspiration.models import Medium
    from django.contrib.auth import get_user_model

    User = get_user_model()


    print(b.serialize())