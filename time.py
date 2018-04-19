#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import timeit

soma = 1 + 2

inicio = timeit.default_timer()
print soma
fim = timeit.default_timer()
print ('duração: %f' % (fim - inicio))