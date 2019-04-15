# -*- coding: utf-8 -*-
#coding=utf-8

import socket
import os
import subprocess
import re



def get_host_ip():
    """
    获取本机IP地址
    :return: 返回获取的IP
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_gateway():
    """
    将获得IP 进行截取，获取网关地址
    :return: 返回ip的前3个地址
    """
    ip = get_host_ip()
    pos = ip.rfind('.')
    gateway = ip[:pos] + '.'
    return gateway


def connect_state(ip):
    """
    连接设备，并读取连接的状态
    :return: 连接的状态:0-连接成功、1-重复连接、2-连接失败、3-连接错误
    """
    # 初始化
    os.system('adb kill-server')
    os.system('adb start-server')
    # 读取连接状态
    path = 'adb connect ' + ip
    print(path)
    outstatus = ''
    out = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE)
    outlist = out.stdout.read().splitlines()
    for item in outlist:
        outstatus = item.decode('utf-8')
        print(outstatus)
    parameter = outstatus
    try:
        # 是否连接成功
        m = re.match('connected', parameter)
        m.group(0)
        result = 0
    except AttributeError:
        try:
            # 是否重复连接
            m = re.match('already', parameter)
            m.group(0)
            result = 1
        except AttributeError:
            try:
                # 是否无法连接
                m = re.match('unable', parameter)
                m.group(0)
                result = 2
            except AttributeError:
                result = 3
    return result



if __name__ == '__main__':
    run = connect_state('10.10.10.170')
