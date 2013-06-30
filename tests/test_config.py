import unittest

from road import config


# Very bad test, only checks for Exceptions.
class ConfigTest(unittest.TestCase):
    def test_config_global_(self):
        print("config.global_: " + config.global_)

    def test_config_local_(self):
        print("config.local_: " + config.local_)

    def test_config_get_global(self):
        print('config.get_global("TEST"): ' + config.get_global("TEST"))

    def test_config_get_local(self):
        print('config.get_local("TEST"): ' + config.get_local("TEST"))
