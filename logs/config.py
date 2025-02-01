import logging


class Config(object):
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopConfig(Config):
    """开发环境下的配置"""
    DEBUG = True


class ProductConfig(Config):
    """生成环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestConfig(Config):
    """测试环境下的配置"""
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopConfig,
    "production": ProductConfig,
    "testing": TestConfig,
}