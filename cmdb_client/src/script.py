# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: script.py
# @time: 2020 03 25
# @email: lxh661314@163.com

from lib.config.get_settings import settings_obj
from src.client import Agent, SshSalt


def main():
    mode = settings_obj.MODE
    if mode == "agent":
        Agent().collect()
    else:
        SshSalt().collect()
