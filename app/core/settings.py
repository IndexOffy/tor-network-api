from os import environ, path

from dotenv import load_dotenv


def set_up():
    """Sets up configuration for the app"""
    load_dotenv()

    config = {
        "DEBUG": bool(environ.get("DEBUG", 1)),
        "ENVIRONMENT": environ.get("ENVIRONMENT", ""),
        "DATABASE_URL": "mysql+pymysql://u141500443_onion_api:wUPzPl^2@srv1064.hstgr.io/u141500443_onion_api",
        "SECRET_KEY": environ.get("SECRET_KEY", "Tor"),
        "BASE_DIR": path.abspath(path.dirname(__file__)),
    }
    return config
