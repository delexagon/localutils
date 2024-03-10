# localutils

Modified from https://github.com/pypa/sampleproject lmao  
Anyway, just like load this into pip   and then create a .python_utils directory in your home directory.  
Then if you add a file to that directory like  
```
# test.py
def a():
    print(1)
```
you can say stuff like
```
from localutils.test import a
```
interactively or from any python script in your computer.  
Of course, a repository will not be transferrable with code using this and other users on the same computer will not be able to import the scripts you create.  
Obviously, this program loads arbitrary python code from the .python_utils directory so don't let people put random garbage in it.
