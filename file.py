# -*- coding: utf-8 -*-

import tkinter as tk
import os
from Transmission import fileRead
dir_path = os.getcwd()


def get_file_call_back(filepath):
    # 获取文件的窗口
    global file_path
    file_path_tem = filepath
    if file_path_tem[-1] != '/':
        file_path = file_path_tem + '/'
    else:
        file_path = file_path_tem

    file_list = fileRead(file_path)[1]

    window_file = tk.Toplevel()
    window_file.geometry('250x400')
    window_file.title('文件获取')

    def get_file(*args):
        indexs = file_list_box.curselection()[0]
        out_name = file_list_box.get(indexs)
        return out_name

    def file_down():
        path = file_path + get_file()
        global file_dir_path
        file_dir_path = dir_path + r'\Downloaded File\File'
        result = os.path.exists(file_dir_path)  # 判断文件夹是否存在，返回布尔值
        if not result:  # 如果不存在，返回False，
            os.makedirs(file_dir_path)  # 创建文件夹
        file_dir_path1 = '\"' + file_dir_path + '\"'  # 加转义符，排除文件夹名中有空格的影响，支持文件夹名为中文
        os.system('adb pull %s %s' % (path, file_dir_path1))  # pull文件到当前路径下的log文件夹中
        pull_txt = get_file() + '下载成功，\n请在' + file_dir_path + '\n查找'
        out_file_value['text'] = pull_txt
        out_file_value['bg'] = 'green'

    def openwindow(dir_path):
        os.system("explorer %s" % dir_path)

    def OpenFileWindow():
        openwindow(file_dir_path)

    new_name = tk.StringVar(value=file_list)  # 将输入的注册名赋值给变量
    file_list_box = tk.Listbox(window_file, selectmode='BROWSE',
                              height=len(file_list), listvariable=new_name, width=30)
    file_list_box.pack()

    down_Button = tk.Button(window_file, text='确认下载', command=file_down)
    down_Button.pack()

    file_list_box.bind("<<ListboxSelect>>", get_file)

    out_file_value = tk.Label(window_file, bg="#ffffff", text='等待获取')
    out_file_value.pack()

    open_Button = tk.Button(window_file, text='打开目录', command=OpenFileWindow)
    open_Button.pack()
