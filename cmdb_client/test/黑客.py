# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: 黑客.py
# @time: 2020 03 26
# @email: lxh661314@163.com


import requests
from lib.config.get_settings import settings_obj


res = requests.get(url=settings_obj.API_URL, headers={"token": "9ac6c5950ace16335189a453938ce211|1585187253.894847"})
print(res.text)
