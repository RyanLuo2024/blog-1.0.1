import logging,time
from logging.handlers import RotatingFileHandler
from flask import Flask
from .config import config
import colorlog,re

class NoColorFormatter(logging.Formatter):
    def format(self, record):
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        record.msg = ansi_escape.sub('', record.msg)
        return super().format(record)

def setup_log(config_name):
    # """

    # :param config_name: 传入日志等级
    # :return:
    # """
    # # 设置日志的的登记
    # logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    # file_log_handler = RotatingFileHandler("logs/log"+time.strftime("%Y%m%d%H%M%S")+".log",backupCount=100)
    # # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    # formatter = colorlog.ColoredFormatter("[%(levelname)s] - %(filename)s - %(lineno)d - %(message)s",
    #                              log_colors={
    #                                 'DEBUG': 'cyan',
    #                                 'INFO': 'green',
    #                                 'WARNING': 'yellow',
    #                                 'ERROR': 'red',
    #                                 'CRITICAL': 'red,bg_white',
    #                             }
    # )
    # # 为日志记录器设置记录格式
    # file_log_handler.setFormatter(formatter)
    # # 移除默认的handler
    # for handler in logger.handlers:
    #     logger.removeHandler(handler)
    # # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    # logging.getLogger().addHandler(file_log_handler)
    # 创建logger对象
    logger = logging.getLogger()
    logger.setLevel(level=config[config_name].LOG_LEVEL)
    # 创建控制台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level=config[config_name].LOG_LEVEL)
    # 创建文件日志处理器
    file_log_handler = RotatingFileHandler("logs/log"+time.strftime("%Y%m%d%H%M%S")+".log",backupCount=100, encoding='utf-8')
    file_log_handler.setLevel(level=config[config_name].LOG_LEVEL)
    # 定义颜色输出格式
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s[%(asctime)s.%(msecs)03d] %(filename)s -> %(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        datefmt='%Y-%m-%d  %H:%M:%S',
    )
    # 将颜色输出格式添加到控制台日志处理器
    console_handler.setFormatter(color_formatter)
    file_log_handler.setFormatter(color_formatter)
    # 移除默认的handler
    for handler in logger.handlers:
        logger.removeHandler(handler)
    # 将控制台日志处理器添加到logger对象
    logger.addHandler(console_handler)
    logger.addHandler(file_log_handler)
    return logger


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