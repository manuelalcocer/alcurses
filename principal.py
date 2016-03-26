#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import curses
import libcurses.alcurses as clib
from os import environ

def createMenu(window):
    menuwin = clib.MainMenu(window)
    menuwin.Refresh()
    return menuwin

def createSelections(menu):
    menuoptions = ['Fichero','Edicion','Opciones','Herramientas','Salir']
    for option in menuoptions:
        menu.AddSel(option)
    return

def WaitAction(w):
    action = ''
    try:
        while action != 'exit':
            keypressed = w.win.getch()
            if curses.KEY_RESIZE:
                w.Redraw()
            action = w.Action(keypressed)
    except KeyboardInterrupt:
        pass
    return

def Main():
    with clib.Init() as Mainwindow:      
        Menu = createMenu(Mainwindow)
        createSelections(Menu)
        WaitAction(Menu)

if __name__ == '__main__':
    environ['ESCDELAY']='0'
    Main()
