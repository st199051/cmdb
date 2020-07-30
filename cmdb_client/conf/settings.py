# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: settings.py
# @time: 2020 03 24
# @email: lxh661314@163.com


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = "root"
PWD = "centos"

EMAIL_PORT = 20

MODE = "agent"

PLUGINS_DICT = {
    "basic": "src.plugins.basic.Basic",
    "cpu": "src.plugins.cpu.Cpu",
    "board": "src.plugins.board.Board",
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
    "nic": "src.plugins.nic.Nic",
}

SSH_USER = "root"
SSH_PWD = "centos"
SSH_PORT = 22

DEBUG = True

API_URL = "http://127.0.0.1:8000/asset/"
