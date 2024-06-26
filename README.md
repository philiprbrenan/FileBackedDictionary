<div>
    <p><a href="https://github.com/philiprbrenan/FileBackedDictionary"><img src="https://github.com/philiprbrenan/FileBackedDictionary/workflows/Test/badge.svg"></a>
</div>

# FileBackedDictionary

A python dictionary object that can save/reload itself to/from a
backing file to facilitate inter-process communication.

Add fields as you wish to an object simply by assigning to them.  Save the
object to the backing file, then change some values before restoring the object
to its original state.

The class is held in file: ```FileBackedDictionary.py```.  The code in this
this file can tested using file ```test.py```.  You can see the code in action
under the
[actions tab](https://github.com/philiprbrenan/FileBackedDictionary/actions)

Copyright Philip R. Brenan ```2024-04-06``` as part of the [Database on a Silicon Chip Project](http://prb.appaapps.com/zesal/pitchdeck/pitchDeck.html)

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
