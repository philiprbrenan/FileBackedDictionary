import pickle, os

class FileBackedDictionary:                                                     # A file backed dictionary
  def __init__(self, filename):                                                 # File used to back the dictionary
    self.__filename__ = filename                                                # Save backing file name

  def save(self):                                                               # Save the user fields assigned to the object
    d = {}
    for key, value in self.__dict__.items():                                    # Attributes of the object
      if not callable(getattr(self, key)) and not key.startswith("__"):         # Horrible!
        d[key] = value

    try:
      with open(self.__filename__, 'wb') as f:                                  # Save to backing file
        pickle.dump(d, f)
    except Exception as e:
      print(f"Unable to write file {self.filename} because {e}")

  def load(self):                                                               # Reload object from the backing file
    try:
      with open(self.__filename__, 'rb') as f:
        fields = pickle.load(f)
        for f in fields.keys():
          self.__dict__[f] = fields[f]
    except Exception as e:
      print(f"Unable to read file {self.__filename__} because {e}")

if __name__ == "__main__":                                                      # Tests
  d   = FileBackedDictionary("zzz.txt")                                         # Create a file backed dictionary
  d.a = "aaa"                                                                   # Create some user fields
  d.b = "bbb"
  d.c = "ccc"
  assert d.b == "bbb"                                                           # Confirm field value
  d.save()                                                                      # Write object to backing file
  d.b = "BBB"                                                                   # Update a field
  assert d.b == "BBB"                                                           # Confirm field value
  d.load()                                                                      # Reload original value
  assert d.b == "bbb"                                                           # Confirm original field value
