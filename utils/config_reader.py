import os
import configparser


class ConfigReader:
    """
        This file reads value from config.ini and provide data encapsulation for the framework
    """

    @staticmethod
    def get_property(section, key):
        # create an instance of the ConfigParser class
        config = configparser.ConfigParser()
        # Read the contents of the 'config.ini' file
        config_path = os.path.join("..", "resources", "configs", "config.ini")
        config.read(config_path)
        return config.get(section, key)
