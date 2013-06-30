# Very hacky, probably a very bad to do things.
from sys import platform

if platform == "win32":
    from windows import Functions
    windows = Functions()
    del Functions

del platform
