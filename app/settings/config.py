from os import environ
from dotenv import load_dotenv

load_dotenv()

DEBUG = environ.get("DEBUG")
ENVIRONMENT = environ.get("ENVIRONMENT")
DATABASE_URL = environ.get("DATABASE_URL")
SECRET_KEY = environ.get("SECRET_KEY")
