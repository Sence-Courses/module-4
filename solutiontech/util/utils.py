import random

def get_attr_and_value(self):
  attributes = {}

  for cls in type(self).__mro__:
    for attr_name in getattr(cls, '__slots__', []):
      try:
        attributes[attr_name] = getattr(self, attr_name)
      except AttributeError:
        pass
  return attributes

def generate_random_id(digits):
  max_num = 10**digits - 1
  random_num = random.randint(1, max_num)  
  return str(random_num).zfill(digits)