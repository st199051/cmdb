# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: __init__.py
# @time: 2020 03 24
# @email: lxh661314@163.com


import paramiko
import traceback
import importlib
import subprocess
from lib.config.get_settings import settings_obj


class PluginsManager(object):
    def __init__(self, host_name=None):
        self.mode = settings_obj.MODE
        self.host_name = host_name
        self.debug = settings_obj.DEBUG

        if self.mode == "ssh":
            self.user = settings_obj.SSH_USER
            self.pwd = settings_obj.SSH_PWD
            self.port = settings_obj.SSH_PORT

    def execute(self):
        """
        管理配置文件中的采集信息操作
        1. 获取配置文件中的PLUGINS_DICT，并循环获取里面的key(basic)和value(src.plugins.basic.Basic)
        2. 需要将value里面的类Basic导入,并实例化，再执行process函数
        :return:
        """
        response = dict()
        for k, v in settings_obj.PLUGINS_DICT.items():
            res = {"code": None, "data": None}
            try:
                module_name, class_name = v.rsplit(".", 1)
                # module_name = src.plugins.basic  class_name = Basic

                module_obj = importlib.import_module(module_name)
                cls = getattr(module_obj, class_name)
                result = cls().process(self.__cmd_run, self.debug)

                res["code"] = 200
                res["data"] = result
            except Exception as e:
                print(e)
                res["code"] = 500
                res["data"] = "{}主机采集{}出错，错误信息为:{}".format(
                    self.host_name if self.host_name else "agent", k, str(traceback.format_exc())
                )
            response[k] = res

        return response

    def __cmd_run(self, cmd):
        if self.mode == "agent":
            self.__cmd_agent(cmd)
        elif self.mode == "ssh":
            self.__cmd_ssh(cmd)
        elif self.mode == "salt":
            self.__cmd_salt(cmd)
        else:
            pass

    def __cmd_agent(self, cmd):
        ret = subprocess.getoutput(cmd)
        return ret[100:200]

    def __cmd_ssh(self, cmd):
        # 创建SSH对象
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        ssh.connect(hostname=self.host_name, port=self.port, username=self.user, password=self.pwd)

        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 获取命令结果
        result = stdout.read()
        # 关闭连接
        ssh.close()

        return result

    def __cmd_salt(self, cmd):
        ret = subprocess.getoutput("salt '{}' cmd.run {}".format(self.host_name, cmd))
        return ret[100:200]
