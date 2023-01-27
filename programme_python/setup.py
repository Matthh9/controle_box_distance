# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:59:18 2020

@author: matth
"""


from cx_Freeze import setup, Executable
import pygame
import PyQt5
import threading


base = None #"Win32GUI" #None

#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("programme.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["pygame"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "controle moyen de test",
    options = options,
    version = "1.0",
    description = 'programme permettant le pilotage des moyens de test à distance par le biais d\'une interraction avec un arduino.',
    executables = executables
)