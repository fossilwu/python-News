#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=latin1:
# from tkinter import *
# from tkinter.filedialog import askdirectory,askopenfilename
from start_2 import maines
#
# filename = "1"
# def selectPath():
#     path_ = askopenfilename()
#     # print path_
#     # global filename
#     # filename = path_
#     path.set(path_)
#
# root = Tk()
# path = StringVar()
# # print filename
# Label(root,text = "目标路径:").grid(row = 0, column = 0)
# Entry(root, textvariable = path).grid(row = 0, column = 1)
# print
# Button(root, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
#
# root.mainloop()
from tkinter import filedialog

filename = filedialog.askopenfilename(initialdir = '',title = "请选择xls文件",filetypes = (("xls文件","*.xls"),("所有文件","*.*")))

print(filename)
maines(filename)
# print 'success'