# -*- coding: utf-8 -*-

from tkinter import ttk
import tkinter as tk
import tkinter.filedialog
from Library import *
from log import log_call_back
from file import get_file_call_back
from Crash import crash_call_back
from Screencap import screencap
from Control import key_call_back


local_ip = get_gateway()    # 获取本机IP的前三位
dir_path = os.getcwd()      # 获取当前路径

window = tk.Tk()            # 实例化object，建立窗口window
window.title('ADB Tools')   # 设置窗口标题
# window.geometry('400x300')


def connect_call_back():
    """
    连接按钮的调用函数
    """
    global ip                   # 全局变量
    ip = ip_entry.get()         # 获取ip_entry中的IP地址
    ip_value['text'] = ip       # 将ip_entry获取的值赋值给ip_value
    start = connect_state(ip)   # 连接设备
    if start == 0 or start == 1:            # 判断连接结果，0为连接成功，1位已连接
        a = os.system('adb shell exit')     # test
        print(a)                            # test
        str_start = '连接成功！'
        out_start(str_start, 0)
    else:                                   # 不为0或1，上报‘连接错误’
        str_start = '连接失败！'
        out_start(str_start, 1)


def out_start(input_val, opt):
    """
    连接按钮下方的value的调用函数
    :param input_val: 显示信息
    :param opt: 背景颜色
    """
    if opt == 0:
        out_start_value['bg'] = '#00ff00'    # opt为0,将背景色设置为绿色
        out_start_value['text'] = input_val  # 显示input_val的值
    elif opt == 1:
        out_start_value['bg'] = '#ff0000'    # opt为0,将背景色设置为红色
        out_start_value['text'] = input_val  # 显示input_val的值


def file_call_back():
    """
    文件下载的按钮的调用函数
    """
    file_path = file_entry.get()    # 获取file_entry的路径
    get_file_call_back(file_path)   # call获取文件的窗口


def screencap_call_back():
    """
    截图按钮的调用函数
    """
    screencap()     # 调Screencap.py 的screencap


def select_call_back():
    """
    打开系统的文件上传窗口来获取文件路径的调用函数
    """
    global filename         # 全局变量
    filename = tk.filedialog.askopenfilename()  # 调用文件选择窗口来获取文件路径，并赋值给变量filename
    if filename != '':                          # 如果选择的文件不为空
        upload_Label.config(text= filename)     # 将变量filename 的值赋给 upload_Label
    else:
        upload_Label.config(text="没有选择任何文件")    # 如果未选择文件，就返回 "没有选择任何文件"


def upload_call_back():
    """
    上传文件按钮的调用函数
    """
    file_path = '\"' + filename + '\"'          # 在文件路径前后加上"",来支持中文及文件名中含有空格给adb shell命令的影响
    pos = file_path.rfind('/')                  # 定位最后一个‘/’的出现位置
    file_name = file_path[pos:]                 # 获取文件名
    # 获取objective_entry中路径，并赋值给变量objective_path
    # 将获取的文件名，添加到目标路径后
    objective_path = objective_entry.get() + file_name
    # 将file_path路径下得文件，上传到objective_path 的路径下
    os.system('adb push %s %s' % (file_path, objective_path))

def shell_call_back():
    """
     打开Shell命令窗口按钮的调用函数
    """
    os.system("cmd/c start adb -s %s:5555 shell" % ip)  # 打开cmd窗口，并进入shell模式


def logcat_call_back():
    """
    打印日志按钮的调用函数
    :return:
    """
    command_line = '\"' + logcat_Combobox.get() + '\"'   # 在文件路径前后加上"",来支持中文及文件名中含有空格给adb shell命令的影响
    os.system("cmd/c start adb -s %s:5555 shell %s" % (ip, command_line))   # 打开cmd窗口，进入shell模式，并直接执行logcat_Combobox中输入的命令


label_0 = tk.Label(window, text=" 设备IP ")
label_0.grid(row=0, column=0)

ip_entry = tk.Entry(window)
ip_entry.insert('end', local_ip)
ip_entry .grid(row=0, column=1)

connect = tk.Button(window, text="连  接", command=connect_call_back)
connect.grid(row=0, column=2)

label_1 = tk.Label(window, text=" 连接设备IP：")
label_1.grid(row=1, column=0)

ip_value = tk.Label(window, text='未连接设备')
ip_value.grid(row=1, column=1)

out_start_value = tk.Label(window, bg="#ffffff", text='')
out_start_value.grid(row=1, column=2)

label_1 = tk.Label(window, text="--------------------文件获取--------------------")
label_1.grid(row=2, column=0, columnspan=3)

logdown = tk.Button(window, text="获取LOG", command=log_call_back)
logdown.grid(row=3, column=0)

logdown = tk.Button(window, text="获取Crash", command=crash_call_back)
logdown.grid(row=3, column=1)

screencap_button = tk.Button(window, text="截图", command=screencap_call_back)
screencap_button.grid(row=3, column=2)

file_down = tk.Button(window, text=" 获取文件", command=file_call_back)
file_down.grid(row=4, column=2)

file_entry = tk.Entry(window)
file_entry.insert('end', '/sdcard/')
file_entry .grid(row=4, column=1)

label_4 = tk.Label(window, text="文件路径：")
label_4.grid(row=4, column=0)

label_2 = tk.Label(window, text="--------------------文件上传--------------------")
label_2.grid(row=5, column=0, columnspan=3)

upload_Label = tk.Label(window, text='请选择你需要上传的文件')
upload_Label.grid(row=6, column=0, columnspan=2)

upload = tk.Button(window, text=" 选择文件", command=select_call_back)
upload.grid(row=6, column=2)

objective_entry = tk.Entry(window)
objective_entry.insert('end', '/sdcard/')
objective_entry .grid(row=7, column=1)

label_5 = tk.Label(window, text="上传路径：")
label_5.grid(row=7, column=0)

upload = tk.Button(window, text=" 上传文件", command=upload_call_back)
upload.grid(row=7, column=2)

label_3 = tk.Label(window, text="--------------------其他功能--------------------")
label_3.grid(row=8, column=0, columnspan=3)

shell_button = tk.Button(window, text=" 打开Shell命令窗口", command=shell_call_back)
shell_button.grid(row=9, column=1)

button_bt = tk.Button(window, text=" 发送按键", command=key_call_back)
button_bt.grid(row=9, column=0)

button_logcat = tk.Button(window, text=" 打印日志", command=logcat_call_back)
button_logcat.grid(row=10, column=2)

logcat_Combobox = ttk.Combobox(window)
logcat_Combobox.insert('end', 'logcat')
logcat_Combobox .grid(row=10, column=1)
logcat_Combobox['value'] = ('candump ', 'logcat | grep ', 'logcat')


label_6 = tk.Label(window, text="日志打印：")
label_6.grid(row=10, column=0)

label_version = tk.Label(window, text=" Ver: debug_v0.5").grid(row=12, column=0)


if __name__ == '__main__':
    # 主窗口循环显示
    window.mainloop()
