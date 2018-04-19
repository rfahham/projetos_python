#!/usr/local/bin/python
# -*- coding: utf-8 -*-
 
# importa modulo
from Tkinter import *
 
# Cria formulario
formulario = Tk()
 
# Cria um variave de Texto.
 
texto = "Desenvolvimento Aberto\nHello World\nTkinter!!!!"
# Cria um novo label
rotulo = Label(formulario, text = texto)
 
# Retira espaço desocupado na janela
rotulo.pack()
 
# Roda o loop principal do tcl
mainloop()