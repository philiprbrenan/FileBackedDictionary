from FileBackedDictionary import FileBackedDictionary

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
