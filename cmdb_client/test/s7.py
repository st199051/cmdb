# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s7.py
# @time: 2020 03 25
# @email: lxh661314@163.com


import traceback

try:
    int("abc")
except Exception as e:
    print(traceback.format_exc())

print("11111111")


