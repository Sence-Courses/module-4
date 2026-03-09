from enum import Enum
import re

VF = Enum('ValidateField', [
  ('email', r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
  ('phone', r'\d{8}'),
])

EM = Enum('ErrorMessage', [
  ('email', 'Ingrese un email valido'),
  ('phone', 'Ingrese un telefono valido'),
])

def validate(value, type):
  match (type):
    case VF.email.name:
      if re.fullmatch(VF.email.value, value) is None:
        return False
      return True
    case VF.phone.name:
      if re.fullmatch(VF.phone.value, value) is None:
        return False
      return True
    case _:
      pass
