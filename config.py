import os

class Config:
    
    QUOTE_URL='http://quotes.stormconsultancy.co.uk/random.json (Links to an external site.)'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ronald:1645@localhost/ronniesblog'       

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}