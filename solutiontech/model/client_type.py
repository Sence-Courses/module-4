import random
from dataclasses import dataclass, field, InitVar
from datetime import datetime
from model import Client, Enterprise
from util.utils import get_attr_and_value, generate_random_id
from util.logger.logger import debug_logger

@dataclass(slots=True)
class RegularCustomer(Client):
  id: InitVar[str] = None
  points: InitVar[int] = None
  register_date: InitVar[datetime] = datetime.today()
  __id: str = field(init=False)
  __points: int = field(init=False)
  __register_datetime: datetime = field(init=False)

  def __post_init__(self, enterprise, id, points, register_date: datetime):
    if not isinstance(enterprise, Enterprise):
      raise TypeError("La empresa debe ser de tipo Enterprise.")
    if not isinstance(points, (int, float)):
      raise TypeError("Los puntos deben ser numericos.")
    if points < 0:
      raise ValueError("Los puntos no pueden ser negativos.")
    
    super(RegularCustomer, self).__post_init__(enterprise)
    self.__id = id if type(id)==str else self.generate_id(enterprise.id)
    self.__points = points
    self.__register_datetime = register_date
    debug_logger.debug(self.__str__())

  def generate_id(self, enterprise_id) -> str:
    return f'{enterprise_id}-REG-{generate_random_id(digits=3)}'

  def calculate_discount(self) -> float:
    return self.__points * 0.02

  @property
  def id(self) -> str:
    return self.__id

  @property
  def register_datetime(self) -> datetime:
    return self.__register_datetime

  def __str__(self):
    return f'{type(self).__name__}_{id(self)} : {get_attr_and_value(self)}'

@dataclass(slots=True)
class PremiumCustomer(Client):
  id: InitVar[str] = None
  register_date: InitVar[datetime] = datetime.today()
  __id: str = field(init=False)
  __register_datetime: datetime = field(init=False)

  def __post_init__(self, enterprise, id, register_date: datetime):
    if not isinstance(enterprise, Enterprise):
      raise TypeError("La empresa debe ser de tipo Enterprise.")
    
    super(PremiumCustomer, self).__post_init__(enterprise)
    self.__id = id if type(id)==str else self.generate_id(enterprise.id)
    self.__register_datetime = register_date
    debug_logger.debug(self.__str__())

  def generate_id(self, enterprise_id) -> str:
    return f'{enterprise_id}-REG-{generate_random_id(digits=3)}'

  def calculate_discount(self) -> float:
    return 10.0

  @property
  def id(self) -> str:
    return self.__id

  @property
  def register_datetime(self) -> datetime:
    return self.__register_datetime

  def __str__(self):
    return f'{type(self).__name__}_{id(self)} : {get_attr_and_value(self)}'

@dataclass(slots=True)
class CorporateCustomer(Client):
  id: InitVar[str] = None
  register_date: InitVar[datetime] = datetime.today()
  __id: str = field(init=False)
  __register_datetime: datetime = field(init=False)

  def __post_init__(self, enterprise, id, register_date: datetime):
    if not isinstance(enterprise, Enterprise):
      raise TypeError("La empresa debe ser de tipo Enterprise.")
    
    super(PremiumCustomer, self).__post_init__(enterprise)
    self.__id = id if type(id)==str else self.generate_id(enterprise.id)
    self.__register_datetime = register_date
    debug_logger.debug(self.__str__())

  def generate_id(self, enterprise_id) -> str:
    return f'{enterprise_id}-REG-{generate_random_id(digits=3)}'

  def calculate_discount(self) -> float:
    return 15.0

  @property
  def id(self) -> str:
    return self.__id

  @property
  def register_datetime(self) -> datetime:
    return self.__register_datetime

  def __str__(self):
    return f'{type(self).__name__}_{id(self)} : {get_attr_and_value(self)}'
