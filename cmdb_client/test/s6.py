# -*- coding: utf-8 -*-
# __author: Tiger_Lee
# @file: s6.py
# @time: 2020 03 25
# @email: lxh661314@163.com


res_list = open('../files/board.out', 'r', encoding="utf-8").readlines()

key_map = {
    "Manufacturer": "manufacturer",
    'Product Name': 'product name',
    'Serial Number': "serial number"
}

response = dict()
for data in res_list:
    if data:
        res = data.strip().split(":")
        if len(res) == 2:
            if res[0] in key_map:
                response[key_map[res[0]]] = res[1]

print(response)


"""
{
'basic': {'os_platform': 'linux', 'os_version': 'CentOS release 6.6 (Final)\nKernel \r on an \\m', 'hostname': 'c2.com'}, 
'cpu': {'cpu_count': 24, 'cpu_physical_count': 2, 'cpu_model': ' Intel(R) Xeon(R) CPU E5-2620 v2 @ 2.10GHz'}, 
'disk': {'0': {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'}, '1': {'slot': '1', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5AH'}, '2': {'slot': '2', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1SZNSAFA01085L     Samsung SSD 850 PRO 512GB               EXM01B6Q'}, '3': {'slot': '3', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1AXNSAF912433K     Samsung SSD 840 PRO Series              DXM06B0Q'}, '4': {'slot': '4', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1AXNSAF303909M     Samsung SSD 840 PRO Series              DXM05B0Q'}, '5': {'slot': '5', 'pd_type': 'SATA', 'capacity': '476.939', 'model': 'S1AXNSAFB00549A     Samsung SSD 840 PRO Series              DXM06B0Q'}}, 
'memory': {'DIMM #0': {'capacity': 1024, 'slot': 'DIMM #0', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #1': {'capacity': ' No Module Installed', 'slot': 'DIMM #1', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #2': {'capacity': ' No Module Installed', 'slot': 'DIMM #2', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #3': {'capacity': ' No Module Installed', 'slot': 'DIMM #3', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #4': {'capacity': ' No Module Installed', 'slot': 'DIMM #4', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #5': {'capacity': ' No Module Installed', 'slot': 'DIMM #5', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #6': {'capacity': ' No Module Installed', 'slot': 'DIMM #6', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}, 'DIMM #7': {'capacity': ' No Module Installed', 'slot': 'DIMM #7', 'model': 'DRAM', 'speed': '667 MHz', 'manufacturer': 'Not Specified', 'sn': 'Not Specified'}}, 
'nic': {'eth0': {'up': True, 'hwaddr': '00:1c:42:a5:57:7a', 'ipaddrs': '10.211.55.4', 'netmask': '255.255.255.0'}}
}
"""
