from sys import platform

import unittest


class WindowsTest(unittest.TestCase):
    @unittest.skipUnless(platform == "win32", "requires Windows")
    def test_windows(self):
        from road import windows
        for function in dir(windows):
            if function.startswith("__"):
                continue

            s = "{function}: {output: >50}"
            output = getattr(windows, function)
            print(s.format(function=function, output=output))

if __name__ == "__main__":
    unittest.main()
    