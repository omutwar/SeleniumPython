import os.path
from configparser import ConfigParser


class PropertyReader:
    """

    """
    file_path = "../resources/configurations/config.ini"

    def __init__(self):
        self.config = ConfigParser()

    def get_property(self, section, key):
        print(self.file_path)
        self.config.read(self.file_path)
        print(self.config.get(section, key))
        return self.config.get(section, key)


prop = PropertyReader()
prop1 = prop.get_property("test", "test1")
print(prop1)
