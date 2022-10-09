from dataclasses import dataclass
from os import path, environ
from dotenv import load_dotenv

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
load_dotenv(dotenv_path=path.join(base_dir, ".env"))


@dataclass
class Config:
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    DB_HOST: str = environ['DB_HOST']
    DB_PORT: int = environ['DB_PORT']
    DB_USER: str = environ['DB_USER']
    DB_PW: str = environ['DB_PASSWORD']
    DB_NAME: str = environ['DB_NAME']
    PROJ_RELOAD: bool = True


@dataclass
class RedisConfig:
    REDIS_HOST: str = environ["REDIS_HOST"]
    REDIS_PORT: int = environ["REDIS_PORT"]
    REDIS_DATABASE: int = environ["REDIS_DATABASE"]


def conf():
    config = dict(local=LocalConfig())
    return config.get("local")


def redis_conf():
    config = dict(local=RedisConfig())
    return config.get("local")
