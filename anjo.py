#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("Seja bem vindo! Conheça o nomedo seu Anjo da Guarda.")

g = input("Insira o dia do seu nascimento:")

guess = int(g)

dicionario = {'1': 'Anjo Rochel',
			  '2': 'Anjo Yabamiah',
			  '3': 'Anjo Haiaiel',
			  '4': 'Anjo Mumiah',
			  '5': 'Anjo da Humildade',
			  '6': 'Anjo Vehuiah', 
			  '7': 'Anjo Jeliel',
			  '8': 'Anjo Sitael',
			  '9': 'Anjo Elemiah',
			  '10': 'Anjo Mahasiah',
			  '11': 'Anjo Lelahel',
			  '12': 'Anjo Achaiah',
			  '13': 'Anjo Cahethel',
			  '14': 'Anjo Haziel',
			  '15': 'Anjo Aladiah',
			  '16': 'Anjo Laoviah',
			  '17': 'Anjo Hahahiah',
			  '18': 'Anjo Yesalel',
			  '19': 'Anjo Mebahel',
			  '20': 'Anjo Hariel',
			  '21': 'Anjo da Hekamiah',
			  '22': 'Anjo Lauviah',
			  '23': 'Anjo Caliel',
			  '24': 'Anjo Leuviah',
			  '25': 'Anjo Pahaliah',
			  '26': 'Anjo Nelchael',
			  '27': 'Anjo Ieiaiel',
			  '28': 'Anjo Melahel',
			  '29': 'Anjo Haheuiah',
			  '30': 'Anjo Nith-Haiah',
			  '31': 'Anjo Haaiah',}

print(dicionario.get(g))

