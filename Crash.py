# -*- coding: utf-8 -*-

import tkinter as tk
import os
from Transmission import fileRead
dir_path = os.getcwd()


def crash_call_back():
    # Crash下载的窗口
    def get_crash(*args):
        indexs = crash_list_box.curselection()[0]
        out_name = crash_list_box.get(indexs)
        return out_name

    def down_crash():
        path = '/sdcard/Crash/' + get_crash()
        global crash_dir_path
        crash_dir_path = dir_path + r'\Downloaded File\Crash'
        result = os.path.exists(crash_dir_path)  # 判断文件夹是否存在，返回布尔值
        if not result:  # 如果不存在，返回False，
            os.makedirs(crash_dir_path)  # 创建文件夹
        crash_dir_path1 = '\"' + crash_dir_path + '\"'  # 加转义符，排除文件夹名中有空格的影响，支持文件夹名为中文
        os.system('adb pull %s %s' % (path, crash_dir_path1))   # pull文件到当前路径下的文件夹中
        pull_txt = get_crash() + '下载成功，\n请在' + crash_dir_path + '\n查找'
        out_crash_value['text'] = pull_txt
        out_crash_value['bg'] = 'green'

    def openwindow(dir_path):
        os.system("explorer %s" % dir_path)

    def OpencrashWindow():
        openwindow(crash_dir_path)

    window_crash = tk.Toplevel()
    window_crash.geometry('250x450')
    window_crash.title('Crash下载')

    list_crash = fileRead('/sdcard/Crash')[1]
    new_name = tk.StringVar(value=list_crash)  # 将输入的注册名赋值给变量
    crash_list_box = tk.Listbox(window_crash, selectmode='BROWSE',
                              height=len(list_crash), listvariable=new_name, width=30)
    crash_list_box.pack()

    down_Button = tk.Button(window_crash, text='确认下载', command=down_crash)
    down_Button.pack()

    crash_list_box.bind("<<ListboxSelect>>", get_crash)

    out_crash_value = tk.Label(window_crash, bg="#ffffff", text='等待获取')
    out_crash_value.pack()

    open_Button = tk.Button(window_crash, text='打开目录', command=OpencrashWindow)
    open_Button.pack()
