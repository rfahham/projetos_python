#!/usr/bin/env python
# -*- coding: utf-8 -*-

seguidores = 50
comentarios = 50
visualizacoes = 750

condicoes = [
	seguidores > 100,
	comentarios > 20,
	visualizacoes > 500
]

if all(condicoes):
	print("O perfil é bom !!!")
