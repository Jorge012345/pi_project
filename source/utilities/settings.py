import configparser
import os


class Settings:
    parser = None
    headers_json = {"content-type": "application/json"}
    services_url = None
    ConnectionStringLocal = None

    @classmethod
    def get_value(cls, section=None, option=None):
        _value = None
        try:
            _value = os.environ[option]
        except:
            try:
                _value = cls.parser.get(section, option)
            except:
                _value = None
        return _value

    @classmethod
    def init(cls):

        _real_path = os.path.realpath(__file__)  # /home/user/test/my_script.py
        _dir_path = os.path.dirname(_real_path)

        _config_file = _dir_path + "/config.ini"
        cls.parser = configparser.ConfigParser()
        cls.parser.read(_config_file)

        cls.services_url = cls.get_value("Environment", "services_url")

        cls.ConnectionStringLocal = "sqlite:///" + _dir_path + "/app.db"
        # cls.ConnectionStringLocal = "sqlite:///app.db"
