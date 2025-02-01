import logging,time
from logging.handlers import RotatingFileHandler
from flask import Flask
from .config import config


def setup_log(config_name):
    """

    :param config_name: 传入日志等级
    :return:
    """
    # 设置日志的的登记
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    file_log_handler = RotatingFileHandler("logs/log"+time.strftime("%Y%m%d%H%M%S")+".log",backupCount=100)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    formatter = logging.Formatter("[%(levelname)s] - %(filename)s - %(lineno)d - %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name, app):
    """

    :param config_name: info bug error
    :return:
    """
    # 创建app实例前先配置好日志文件
    setup_log(config_name)
    # 创建app实例对象
    # 实例对象从配置文件中加载配置
    app.config.from_object(config[config_name])   # 这里直接拿到的是类的名字，也就是引用
    return app