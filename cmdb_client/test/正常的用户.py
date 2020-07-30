# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: 正常的用户.py
# @time: 2020 03 26
# @email: lxh661314@163.com


import time
import hashlib
import requests
from lib.config.get_settings import settings_obj


client_token = "asdfjalrkqwpoitdlsgfkjsdlfgjalsdfj"
client_time = time.time()

tmp = "{}|{}".format(client_token, client_time)

# 使用haslib生成一个md5值
m = hashlib.md5()
m.update(bytes(tmp, encoding="utf-8"))
client_md5 = m.hexdigest()

# 将客户端的时间戳和md5码进行拼接一并发送给服务器端
client_md5_token = "{}|{}".format(client_md5, client_time)  # 319345721ef2d09a5507cf5c33dd5eb2|1585186386.290012
print(client_md5_token)

# 将md5值传递给服务器端
res = requests.get(url=settings_obj.API_URL, headers={"token": client_md5_token})
print(res.text)

