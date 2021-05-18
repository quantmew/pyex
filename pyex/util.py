
from enum import Enum

def enum_to_str(e):
    if isinstance(e, Enum):
        return e.value
    else:
        return e