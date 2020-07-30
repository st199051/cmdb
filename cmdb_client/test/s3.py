# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s3.py
# @time: 2020 03 24
# @email: lxh661314@163.com

from lib.config.get_settings import settings_obj

for k, v in settings_obj.PLUGINS_DICT.items():
    module_name, class_name = v.rsplit(".", 1)



