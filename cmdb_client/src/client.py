# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: client.py
# @time: 2020 03 25
# @email: lxh661314@163.com

import os
import json
import requests
from lib.config.get_settings import settings_obj
from src.plugins import PluginsManager
from concurrent.futures import ThreadPoolExecutor


class Base(object):
    """
    基类
    """
    def post_data(self, res):
        """
        向服务器端提交数据
        :return:
        """
        requests.post(url=settings_obj.API_URL, data=json.dumps(res))


class Agent(Base):
    """
    Agent方案
    """
    def collect(self):
        """
        采集数据，并发送
        :return:
        """
        res = PluginsManager().execute()
        host_name = res["basic"]["data"]["hostname"]

        host = open(os.path.join(settings_obj.BASE_DIR, 'files/cert'), 'r', encoding="utf-8").read()
        if host:
            # 这是非第一次采集信息时，将保存在文件中的唯一主机名写入到采集的服务器数据中
            res["basic"]["data"]["hostname"] = host
        else:
            # 这是第一次采集信息的时候，将采集到的唯一主机名写入到cert文件中
            with open(os.path.join(settings_obj.BASE_DIR, 'files/cert'), 'w', encoding="utf-8") as f:
                f.write(host_name)

        # 向API端提交数据
        self.post_data(res)


class SshSalt(Base):
    """
    集成ssh和salt两个方案
    """
    def get_host_name(self):
        host_list = requests.get(url=settings_obj.API_URL)
        return host_list

    def task(self, host_name):
        res = PluginsManager(host_name).execute()
        self.post_data(res)

    def collect(self):
        """
        采集数据，并发送
        :return:
        """
        host_list = self.get_host_name()
        pool = ThreadPoolExecutor(3)

        for host_name in host_list:
            pool.submit(self.task, host_name)
