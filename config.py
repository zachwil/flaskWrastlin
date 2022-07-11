import os

from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DB_URI = os.environ.get("DB_URI")
