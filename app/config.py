class Config():
    DEBUG = False
    DATABASE_NAME = 'postgres'
    DATABASE_USER = 'postgres'
    DATABASE_PASSWORD = 'postgres'
    DATABASE_HOST = 'db'
    DATABASE_PORT = 5432
    PORT = '8080'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
