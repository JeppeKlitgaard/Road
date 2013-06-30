# Very hacky, probably a very bad to do things.
from sys import platform

if platform == "win32":
    from windows import windows

del platform

from config import config
