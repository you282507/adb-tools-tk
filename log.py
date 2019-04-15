# -*- coding: utf-8 -*-

import tkinter as tk
import os
from Transmission import fileRead
dir_path = os.getcwd()


def log_call_back():
    # Log下载的窗口
    def get_log(*args):
        indexs = log_list_box.curselection()[0]
        out_name = log_list_box.get(indexs)
        return out_name

    def down_log():
        path = '/sdcard/Log/' + get_log()
        pos = path.rfind('/')
        # 将获取到的分割取后面的文件名，再去除头尾的‘/’
        file_name_lod = path[pos:].strip('/')
        # 使用空格分割字符，获取时间，在时间前面+通配符“*”
        file_rename = '*' + file_name_lod.split(' ')[-1]
        # 将文件名中的非法字符替换
        file_name_new = file_name_lod.replace(':', '.').replace(' ', '_')
        # 将log的路径与加通配符的文件名拼接
        rename_lod = '/sdcard/Log/' + file_rename
        # 将/sdcard/与新的文件夹拼接
        rename_new = '/sdcard/' + file_name_new
        # 将 重命名前与重命名后的地址拼接
        rename_pact = rename_lod + ' ' + rename_new
        global log_dir_path
        log_dir_path = dir_path + r'\Downloaded File\Log'    # log文件夹的路径
        result = os.path.exists(log_dir_path)  # 判断log文件夹是否存在，返回布尔值
        if not result:  # 如果不存在，返回False，
            os.makedirs(log_dir_path)  # 创建log文件夹
        log_dir_path1 = '\"' + log_dir_path + '\"'  # 加转义符，排除文件夹名中有空格的影响，支持文件夹名为中文
        os.system('adb shell cp %s' % rename_pact)  # 复制文件到sdcard路径下
        os.system('adb pull %s %s' % (rename_new, log_dir_path1))   # pull文件到当前路径下的log文件夹中
        os.system('adb shell rm %s' % rename_new)   # 删除sdcard路径下的临时文件
        pull_txt = get_log() + '下载成功，\n请在' + log_dir_path + '\n查找'
        out_log_value['text'] = pull_txt
        out_log_value['bg'] = 'green'

    def openwindow(dirPath):
        os.system("explorer %s" % dirPath)

    def OpenLogWindow():
        openwindow(log_dir_path)

    window_log = tk.Toplevel()
    window_log.geometry('250x450')
    window_log.title('LOG下载')

    list_log = fileRead('/sdcard/Log')[1]
    new_name = tk.StringVar(value=list_log)  # 将输入的注册名赋值给变量
    log_list_box = tk.Listbox(window_log, selectmode='BROWSE',
                              height=len(list_log), listvariable=new_name, width=30)
    log_list_box.pack()

    down_button = tk.Button(window_log, text='确认下载', command=down_log)
    down_button.pack()

    log_list_box.bind("<<ListboxSelect>>", get_log)

    out_log_value = tk.Label(window_log, bg="#ffffff", text='等待获取')
    out_log_value.pack()

    open_button = tk.Button(window_log, text='打开目录', command=OpenLogWindow)
    open_button.pack()
