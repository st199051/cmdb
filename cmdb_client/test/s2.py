# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s2.py
# @time: 2020 03 24
# @email: lxh661314@163.com


import s1

for key in dir(s1):
    if key.isupper():
        print(getattr(s1, key))

