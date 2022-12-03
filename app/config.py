from os import environ, path
from dotenv import load_dotenv

load_dotenv()

DEBUG = environ.get("DEBUG", True)
ENVIRONMENT = environ.get("ENVIRONMENT", "")
DATABASE_URL = environ.get("DATABASE_URL", "sqlite:///./sql_app.db")
SECRET_KEY = environ.get("SECRET_KEY")
BASE_DIR = path.abspath(path.dirname(__file__))
