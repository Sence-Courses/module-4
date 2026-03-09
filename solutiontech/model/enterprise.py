import random
from dataclasses import dataclass, field, InitVar
from datetime import datetime
from util.utils import get_attr_and_value
from util.logger.logger import debug_logger

def generate_id(name):
  print(name)
  digits = 3
  max_num = 10**digits - 1
  random_num = random.randint(1, max_num)
  return name[:3].strip().upper() + str(random_num).zfill(digits)
  #print(id)
  #return id

@dataclass(slots=True)
class Enterprise:
  id: InitVar[str] = None
  name: InitVar[str] = None
  address: InitVar[str] = None
  email: InitVar[str] = None
  phone: InitVar[str] = None
  register_date: InitVar[datetime] = datetime.today()
  is_active: InitVar[bool] = False
  __id: str = field(init=False)
  __name: str = field(init=False)
  __address: str = field(init=False)
  __email: str = field(init=False)
  __phone: str = field(init=False)
  __register_datetime: datetime = field(init=False)
  __active: bool = field(init=False)

  def __post_init__(self, 
      id, name, address, email, phone, register_date: datetime, is_active):
    self.__id = id if type(id)==str else generate_id(name)
    self.name = name
    self.address = address
    self.email = email
    self.phone = phone
    self.__register_datetime = register_date
    self.__active = is_active
    debug_logger.debug(self.__str__())

  @property
  def id(self) -> str:
    return self.__id

  @property
  def register_datetime(self) -> datetime:
    return self.__register_datetime

  @property
  def active(self) -> bool:
    return self.__active

  @active.setter
  def active(self, value: bool) -> None:
    if not value:
      raise ValueError("active cannot be an empty value.")
    else:
      self.__active = value

  @property
  def name(self) -> str:
    return self.__name

  @name.setter
  def name(self, value: str) -> None:
    if not value:
      raise ValueError("name cannot be an empty value.")
    else:
      self.__name = value

  @property
  def address(self) -> str:
    return self.__address

  @address.setter
  def address(self, value: str) -> None:
    if not value:
      raise ValueError("address cannot be an empty value.")
    else:
      self.__address = value

  @property
  def email(self) -> str:
    return self.__email

  @email.setter
  def email(self, value: str) -> None:
    if not value:
      raise ValueError("email cannot be an empty value.")
    else:
      self.__email = value

  @property
  def phone(self) -> str:
    return self.__phone

  @phone.setter
  def phone(self, value: str) -> None:
    if not value:
      raise ValueError("phone cannot be an empty value.")
    else:
      self.__phone = value

  def __str__(self):
    return f'{type(self).__name__}_{id(self)} : {get_attr_and_value(self)}'
