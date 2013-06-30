from sys import platform

import unittest


# Very bad test, only checks for Exceptions.
@unittest.skipUnless(platform == "win32", "Platform was not Windows.")
class WindowsTest(unittest.TestCase):
    def test_windows(self):
        from road import windows

        for function in dir(windows):
            if function.startswith("__"):
                continue

            s = "{function}: {output: >50}"
            output = getattr(windows, function)
            print(s.format(function=function, output=output))
