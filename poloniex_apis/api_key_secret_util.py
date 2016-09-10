import ConfigParser


def get_api_key():
    """
    Returns a Poloniex API key from the config file
    """
    config = ConfigParser.ConfigParser()
    config.read("api_keys.ini")
    key = config.get("ApiKeys", "key")
    return key


def get_api_secret():
    """
    Returns a Poloniex API secret from the config file
    """
    config = ConfigParser.ConfigParser()
    config.read("api_keys.ini")
    secret = config.get("ApiKeys", "secret")
    return secret
