# -*- coding: utf-8 -*-
import os
import tkinter as tk


def key_call_back():
    def home_call_back():
        key_button = 3
        os.system('adb shell input keyevent %s' % key_button)

    def back_call_back():
        key_button = 4
        os.system('adb shell input keyevent %s' % key_button)

    def up_call_back():
        key_button = 24
        os.system('adb shell input keyevent %s' % key_button)

    def down_call_back():
        key_button = 25
        os.system('adb shell input keyevent %s' % key_button)

    def send_call_back():
        list_txt = text_entry.get()
        if list_txt is None:
            pass
        else:
            os.system('adb shell input text "%s"' % list_txt)

    window_input = tk.Toplevel()
    window_input.geometry('250x450')
    window_input.title('按键及文本输入')

    home_button = tk.Button(window_input, text='Home（返回桌面）', command=home_call_back)
    home_button.pack()

    back_button = tk.Button(window_input, text='Back（返回上一级）', command=back_call_back)
    back_button.pack()

    up_button = tk.Button(window_input, text='音量加', command=up_call_back)
    up_button.pack()

    down_button = tk.Button(window_input, text='音量减', command=down_call_back)
    down_button.pack()

    label_0 = tk.Label(window_input, text="------------------------------------------------")
    label_0.pack()

    text_entry = tk.Entry(window_input)
    text_entry.insert('end', '请输入英文或数字！')
    text_entry.pack()

    send_button = tk.Button(window_input, text='发送文本', command=send_call_back)
    send_button.pack()

