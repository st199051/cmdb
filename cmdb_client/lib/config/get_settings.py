# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: get_settings.py
# @time: 2020 03 24
# @email: lxh661314@163.com

from conf import settings
from lib.config import global_settings


class Settings(object):
    def __init__(self):
        # 集成全局配置文件中的相关配置
        for key in dir(global_settings):
            if key.isupper():
                setattr(self, key, getattr(global_settings, key))

        # 集成自定义配置文件中的相关配置
        for key in dir(settings):
            if key.isupper():
                setattr(self, key, getattr(settings, key))


settings_obj = Settings()

