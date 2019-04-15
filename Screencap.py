# -*- coding: utf-8 -*-

import time
import os


def screencap():
    dir_path = os.getcwd()
    current_time = time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time()))
    file_name = current_time + ".png"
    os.system('adb shell /system/bin/screencap -p /sdcard/%s' % file_name)  # 截图
    global screencap_dir_path
    screencap_dir_path = dir_path + r'\Downloaded File\Screencap'
    result = os.path.exists(screencap_dir_path)  # 判断Screencap文件夹是否存在，返回布尔值
    if not result:  # 如果不存在，返回False，
        os.makedirs(screencap_dir_path)  # 创建Screencap文件夹
    screencap_dir_path1 = '\"' + screencap_dir_path + '\"'  # 加转义符，排除文件夹名中有空格的影响，支持文件夹名为中文
    os.system('adb pull /sdcard/%s %s' % (file_name, screencap_dir_path1))
    os.system('adb shell rm /sdcard/%s' % file_name)
