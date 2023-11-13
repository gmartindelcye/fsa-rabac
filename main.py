from logging.config import fileConfig

from sqlmodel import SQLModel, create_engine
from sqlmodel.pool import StaticPool
from decouple import config

from alembic import context

DATABASE_URL = config('DATABASE_URL')   