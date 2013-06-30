from sys import platform
from os import path
if platform == "win32":
    from road import windows


class Functions(object):
    @property
    def global_(self):
        """Added underscore to accommodate for Python syntax."""
        if platform == "win32":
            return windows.appdata
        else:
            return path.abspath("/etc")

    @property
    def local_(self):
        """Added underscore to accommodate for Python syntax."""
        if platform == "win32":
            return windows.local_appdata
        else:
            return path.abspath(path.join(path.expanduser("~"), ".config/"))

    def get_global(self, app_name):
        return path.abspath(path.join(self.global_, str(app_name)))

    def get_local(self, app_name):
        return path.abspath(path.join(self.local_, str(app_name)))

config = Functions()
