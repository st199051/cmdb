# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s5.py
# @time: 2020 03 24
# @email: lxh661314@163.com


import importlib

res = importlib.import_module("s4")

cls = getattr(res, "Person")
cls().get_info()

