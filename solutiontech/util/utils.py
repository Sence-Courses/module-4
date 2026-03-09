def get_attr_and_value(self):
  attributes = {}

  for cls in type(self).__mro__:
    for attr_name in getattr(cls, '__slots__', []):
      try:
        attributes[attr_name] = getattr(self, attr_name)
      except AttributeError:
        pass
  return attributes