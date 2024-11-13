from abc import ABC
from typing import TypeVar

from base.repository import BaseRepository

R = TypeVar("R", bound=BaseRepository)

class AbstractService(ABC):
    pass

class BaseService(AbstractService):

    def __init__(self, repository: R):
        self._repo = repository