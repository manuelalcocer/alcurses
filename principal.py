#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from curses import ascii
import curses
import libcurses.alcurses as clib
from os import environ

def createMenu(window):
    menuwin = clib.MainMenu(window)
    menuwin.Refresh()
    return menuwin

def createSelections(menu):
    menu.AddSel('Fichero')
    menu.AddSel('Opciones')
    menu.AddSel('Salir')
    return

def WaitAction(w):
    keypressed = ''
    try:
        while keypressed != ascii.ESC:
            keypressed = w.win.getch()
            if curses.KEY_RESIZE:
                w.Redraw()
    except KeyboardInterrupt:
        pass
    return

def Main():
    with clib.Init() as Mainwindow:      
        Menu = createMenu(Mainwindow)
        createSelections(Menu)
        Menu.Refresh()
        WaitAction(Menu)

if __name__ == '__main__':
    environ['ESCDELAY']='0'
    Main()
