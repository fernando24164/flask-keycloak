from pathlib import Path
from uuid import uuid4

basedir = Path.cwd().parents[1]


class Config:
    SECRET_KEY = uuid4()
    DEBUG = False


class DevelopmentConfig:
    DEBUG = True


config_by_name = dict(dev=DevelopmentConfig)

key = Config.SECRET_KEY
