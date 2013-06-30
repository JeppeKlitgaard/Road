#coding: UTF8
"""
System File Locations
Retrieves common system path names on Windows
Depends only on ctypes, and retrieves path locations in Unicode
"""

# TAKEN FROM winpaths module, then PEP8'd and some other stuff.
# Credit goes to Ryan Ginstrom

from sys import platform
if platform != "win32":
    error = "Environment wasn't Windows, was: '{env}'"
    raise EnvironmentError(error.format(env=platform))

import ctypes
from ctypes import windll, wintypes


CONSTANTS = {
    "CSIDL_DESKTOP": 0,
    "CSIDL_PROGRAMS": 2,
    "CSIDL_PERSONAL": 5,
    "CSIDL_FAVORITES": 6,
    "CSIDL_STARTUP": 7,
    "CSIDL_RECENT": 8,
    "CSIDL_SENDTO": 9,
    "CSIDL_BITBUCKET": 10,
    "CSIDL_STARTMENU": 11,
    "CSIDL_MYDOCUMENTS": 12,
    "CSIDL_MYMUSIC": 13,
    "CSIDL_MYVIDEO": 14,
    "CSIDL_DESKTOPDIRECTORY": 16,
    "CSIDL_DRIVES": 17,
    "CSIDL_NETWORK": 18,
    "CSIDL_NETHOOD": 19,
    "CSIDL_FONTS": 20,
    "CSIDL_TEMPLATES": 21,
    "CSIDL_COMMON_STARTMENU": 22,
    "CSIDL_COMMON_PROGRAMS": 23,
    "CSIDL_COMMON_STARTUP": 24,
    "CSIDL_COMMON_DESKTOPDIRECTORY": 25,
    "CSIDL_APPDATA": 26,
    "CSIDL_PRINTHOOD": 27,
    "CSIDL_LOCAL_APPDATA": 28,
    "CSIDL_ALTSTARTUP": 29,
    "CSIDL_COMMON_ALTSTARTUP": 30,
    "CSIDL_COMMON_FAVORITES": 31,
    "CSIDL_INTERNET_CACHE": 32,
    "CSIDL_COOKIES": 33,
    "CSIDL_HISTORY": 34,
    "CSIDL_COMMON_APPDATA": 35,
    "CSIDL_WINDOWS": 36,
    "CSIDL_SYSTEM": 37,
    "CSIDL_PROGRAM_FILES": 38,
    "CSIDL_MYPICTURES": 39,
    "CSIDL_PROFILE": 40,
    "CSIDL_SYSTEMX86": 41,
    "CSIDL_PROGRAM_FILESX86": 42,
    "CSIDL_PROGRAM_FILES_COMMON": 43,
    "CSIDL_PROGRAM_FILES_COMMONX86": 44,
    "CSIDL_COMMON_TEMPLATES": 45,
    "CSIDL_COMMON_DOCUMENTS": 46,
    "CSIDL_COMMON_ADMINTOOLS": 47,
    "CSIDL_ADMINTOOLS": 48,
    "CSIDL_CONNECTIONS": 49,
    "CSIDL_COMMON_MUSIC": 53,
    "CSIDL_COMMON_PICTURES": 54,
    "CSIDL_COMMON_VIDEO": 55,
    "CSIDL_RESOURCES": 56,
    "CSIDL_RESOURCES_LOCALIZED": 57,
    "CSIDL_COMMON_OEM_LINKS": 58,
    "CSIDL_CDBURN_AREA": 59,
    "CSIDL_COMPUTERSNEARME": 61
}


def _err_unless_zero(result):
    if result == 0:
        return result
    else:
        error = "Failed to retrieve windows path: '{result}'"
        raise OSError(error.format(result=result))

_SHGetFolderPath = windll.shell32.SHGetFolderPathW
_SHGetFolderPath.argtypes = [wintypes.HWND,
                             ctypes.c_int,
                             wintypes.HANDLE,
                             wintypes.DWORD, wintypes.LPCWSTR]
_SHGetFolderPath.restype = _err_unless_zero


def _get_path_buf(csidl):
    path_buf = wintypes.create_unicode_buffer(wintypes.MAX_PATH)
    result = _SHGetFolderPath(0, csidl, 0, 0, path_buf)
    return path_buf.value


# Very hacky, probably a very bad way to do things.

class Functions(object):
    @property
    def local_appdata(self):
        return _get_path_buf(CONSTANTS["CSIDL_LOCAL_APPDATA"])

    @property
    def appdata(self):
        return _get_path_buf(CONSTANTS["CSIDL_APPDATA"])

    @property
    def desktop(self):
        return _get_path_buf(CONSTANTS["CSIDL_DESKTOP"])

    @property
    def programs(self):
        """current user -> Start menu -> Programs"""
        return _get_path_buf(CONSTANTS["CSIDL_PROGRAMS"])

    @property
    def admin_tools(self):
        """current user -> Start menu -> Programs -> Admin tools"""
        return _get_path_buf(CONSTANTS["CSIDL_ADMINTOOLS"])

    @property
    def common_admin_tools(self):
        """all users -> Start menu -> Programs -> Admin tools"""
        return _get_path_buf(CONSTANTS["CSIDL_COMMON_ADMINTOOLS"])

    @property
    def common_appdata(self):
        return _get_path_buf(CONSTANTS["CSIDL_COMMON_APPDATA"])

    @property
    def common_documents(self):
        return _get_path_buf(CONSTANTS["CSIDL_COMMON_DOCUMENTS"])

    @property
    def cookies(self):
        return _get_path_buf(CONSTANTS["CSIDL_COOKIES"])

    @property
    def history(self):
        return _get_path_buf(CONSTANTS["CSIDL_HISTORY"])

    @property
    def internet_cache(self):
        return _get_path_buf(CONSTANTS["CSIDL_INTERNET_CACHE"])

    @property
    def my_pictures(self):
        """Get the user's My Pictures folder"""
        return _get_path_buf(CONSTANTS["CSIDL_MYPICTURES"])

    @property
    def personal(self):
        """AKA 'My Documents'"""
        return _get_path_buf(CONSTANTS["CSIDL_PERSONAL"])

    @property
    def my_documents(self):
        return self.personal

    @property
    def program_files(self):
        return _get_path_buf(CONSTANTS["CSIDL_PROGRAM_FILES"])

    @property
    def program_files_common(self):
        return _get_path_buf(CONSTANTS["CSIDL_PROGRAM_FILES_COMMON"])

    @property
    def system(self):
        """Use with care and discretion"""
        return _get_path_buf(CONSTANTS["CSIDL_SYSTEM"])

    @property
    def windows(self):
        """Use with care and discretion"""
        return _get_path_buf(CONSTANTS["CSIDL_WINDOWS"])

    @property
    def favorites(self):
        return _get_path_buf(CONSTANTS["CSIDL_FAVORITES"])

    @property
    def startup(self):
        """current user -> start menu -> programs -> startup"""
        return _get_path_buf(CONSTANTS["CSIDL_STARTUP"])

    @property
    def recent(self):
        return _get_path_buf(CONSTANTS["CSIDL_RECENT"])

windows = Functions()
