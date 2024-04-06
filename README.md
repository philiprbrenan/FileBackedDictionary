<div>
    <p><a href="https://github.com/philiprbrenan/FileBackedDictionary"><img src="https://github.com/philiprbrenan/FileBackedDictionary/workflows/Test/badge.svg"></a>
</div>

# FileBackedDictionary

A python dictionary object that can save and reload itself to and from a
backing file to facilitate inter-process communication.

```
from FileBackedDictionary import FileBackedDictionary

d   = FileBackedDictionary("zzz.txt")    # Create a file backed dictionary
d.a = "aaa"                              # Create some user fields
d.b = "bbb"
d.c = "ccc"
assert d.b == "bbb"                      # Confirm field value
d.save()                                 # Write object to backing file
d.b = "BBB"                              # Update a field
assert d.b == "BBB"                      # Confirm field value
d.load()                                 # Reload original value
assert d.b == "bbb"
```
