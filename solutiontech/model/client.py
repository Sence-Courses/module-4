from dataclasses import dataclass, field, InitVar
from abc import ABC, abstractmethod
from util.utils import get_attr_and_value
from model import Enterprise
from util.logger.logger import debug_logger

@dataclass(slots=True)
class Client(ABC):
  enterprise: InitVar[Enterprise] = None
  __enterprise: Enterprise = field(init=False)

  def __post_init__(self, enterprise):
    self.enterprise = enterprise
    debug_logger.debug(self.__str__())

  @abstractmethod
  def generate_id(self) -> str:
    pass

  @abstractmethod
  def calculate_discount(self) -> float:
    pass

  @property
  def enterprise(self) -> Enterprise:
    return self.__enterprise

  @enterprise.setter
  def enterprise(self, value: Enterprise) -> None:
    self.__enterprise = value

  def __str__(self):
    return f'{type(self).__name__}_{id(self)} : {get_attr_and_value(self)}'