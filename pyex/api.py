from enum import Enum
from typing import Optional, Union, Dict, NoReturn
from functools import partial

from .util import enum_to_str

class Exchange(Enum):
    OKEX = 'okex'

class PyexAPI(object):
    def __init__(self):
        super().__init__()

class PyexAPIBuilder(object):
    def __init__(self):
        super().__init__()
        self.params: Dict[str, str] = dict()

    def set_param(self, key, value) -> 'PyexAPIBuilder':
        self.params[key] = value
        return self

    def __getattr__(self, name: str):
        return partial(self.set_param, name)

    def build(self, exchange: Union[Exchange, str]) -> PyexAPI:
        exchange = enum_to_str(exchange)
        if exchange.lower() == 'okex':
            from .okex.v5.api import OkexPyexAPI
            print(self.params)
            return OkexPyexAPI(self.params)


