# coding=utf-8
# -*- coding: utf-8 –*-

import os
import subprocess


def fileRead(file_path=''):
    """
    读取文件，返回文件路径
    :param file_path: 默认读取的文件路径
    :return:result：文件路径；out_fiel_type：文件类型（1：文件夹、2：文件）
    """
    filelist = []       # 存文件名的列表
    folderlist = []     # 存文件夹名的列表

    path = 'adb shell ls -F ' + file_path  # 路径地址
    # print(path)
    out = subprocess.Popen(path, shell=True, stdout=subprocess.PIPE)  # 读取
    outlist = out.stdout.read().splitlines()                          # 转码
    # print(outlist)
    for item in outlist:                                              # 遍历
        if item.decode('utf-8').split(' ')[0] == 'd':                 # 判断文件类型，是否为文件夹
            folderlist.append(item.decode('utf-8').split(' ')[1])     # 加到文件夹的字典列表中
        elif item.decode('utf-8').split(' ')[0] == '-':               # 判断文件类型，是否为文件
            filelist.append(item.decode('utf-8').split(' ', 1)[1])       # 加到文件的字典列表中
    return folderlist, filelist

