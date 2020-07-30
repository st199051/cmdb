# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: basic.py
# @time: 2019 11 16
# @email: lxh661314@163.com


class Basic(object):

    def process(self, command_func, debug):
        """
        真正采集服务器信息的函数
        :return:
        """
        if debug:
            output = {
                'os_platform': "linux",
                'os_version': "CentOS release 6.6 (Final)\nKernel \r on an \m",
                'hostname': 'c2.com'
            }
        else:
            output = {
                'os_platform': command_func("uname").strip(),
                'os_version': command_func("cat /etc/issue").strip().split('\n')[0],
                'hostname': command_func("hostname").strip(),
            }
        return output

    def parse(self, res):
        """
        具体分析的代码
        :param res:
        :return:
        """
        key_map = {
            'Manufacturer': "manufacturer",
            'Product Name': "product_name",
            'Serial Number': "sn",
        }

        response = dict()
        res = res.split('\n')
        for info in res:
            if info:
                data = info.strip().split(":")
                if len(data) == 2:
                    if data[0] in key_map:
                        response[key_map[data[0]]] = data[1]

        return response

