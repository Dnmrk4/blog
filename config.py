import os

class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dnmrk:isystems123@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dnmrk:isystems123@localhost/blog'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:milkshake@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}