import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'ZmFtaWxpYTpzYW50YW5h'
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    DEBUG = False
    FLASK_RUN_HOST = '0.0.0.0'
    FLASK_RUN_PORT = 6999
    LOG_LEVEL = 'WARN'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    FLASK_RUN_HOST = '0.0.0.0'
    FLASK_RUN_PORT = 7999


class TestingConfig(Config):
    TESTING = True
