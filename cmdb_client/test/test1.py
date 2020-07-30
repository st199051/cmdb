# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: test1.py
# @time: 2020 03 23
# @email: lxh661314@163.com


import requests
import subprocess


ret = subprocess.getoutput("ipconfig/all")
print(ret[100:200])
ip = ret[100:200]


requests.post(url="http://10.0.0.2/api", data={"ip": ip})


host_list = ["10.0.0.2", "10.0.0.3"]

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.7', port=22, username='root', password='centos')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('hostname')
# 获取命令结果
result = stdout.read()
print(result)

# 关闭连接
ssh.close()


