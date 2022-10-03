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
    DB_URL: str = 'mysql://{}:{}@{}:{}/{}'.format(
        environ['DB_USER'],
        environ['DB_PASSWORD'],
        environ['DB_HOST'],
        environ['DB_PORT'],
        environ['DB_NAME']
    )
    PROJ_RELOAD: bool = True


def conf():
    config = dict(local=LocalConfig())
    return config.get("local")


