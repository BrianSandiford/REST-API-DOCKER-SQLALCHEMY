import os

user = 'admin'
password = 'admin123'
host = 'postgres'
database = 'postgresdb'
port = 5432

#DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
#DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{admin}:{admin123}@{postgres}:{postgres}/{postgresdb}'
DATABASE_CONNECTION_URI = 'sqlite:///'
  empty database to jumpstar migration on existing project
class BaseConfig:
    TESTING = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
