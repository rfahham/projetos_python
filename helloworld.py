#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import Tkinter

root = Tkinter.Tk()

def helloCallBack():
    print 'oi'

b = Tkinter.Button(root, text ="Hello", command = helloCallBack)

b.pack()
root.mainloop()