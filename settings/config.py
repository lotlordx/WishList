from decouple import config


class Config:
    """Parent Configuration class"""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = config('SECRET', default='')
    DATABASE_CONNECTION_STRING = config('DATABASE_CONNECTION_STRING', default='')
    TESTING = True


class ProductionConfig(Config):
    """Production Configuration Class"""
    TESTING = False


class StagingConfig(Config):
    """StagingConfiguration Class"""
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    """Development Configuration Class"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Production Configuration Class"""
    DATABASE_CONNECTION_STRING = "mysql://root:password@localhost/test_db"
    DEBUG = True


app_config = {
    "production": ProductionConfig,
    "staging": StagingConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig
}