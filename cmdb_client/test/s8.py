# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s8.py
# @time: 2020 03 25
# @email: lxh661314@163.com


import time
from concurrent.futures import ThreadPoolExecutor


def main(i):
    time.sleep(2)
    print(i)


pool = ThreadPoolExecutor(100)

for i in range(100):
    pool.submit(main, i)
