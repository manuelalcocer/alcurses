# -*- coding: utf-8 -*-

import curses as c

class Init(object):
    def __init__(self):
        self.win = c.initscr()
        c.noecho()
        c.cbreak()
        c.curs_set(0)
        self.win.keypad(1)
        if c.has_colors():
            c.start_color()
            c.use_default_colors()
            self.CreatePairs()
        self.win.border(0)
        return

    def Dims(self):
        return self.win.getmaxyx()

    def Refresh(self):
        self.win.refresh()
        return

    def Sweep(self):
        self.win.move(0,0)
        self.win.clrtobot()
        return
    
    def Changecolor(self,pair):
        self.win.bkgd(c.color_pair(pair))
        self.win.attrset(c.color_pair(pair))
        self.win.refresh()
        return

    def __enter__(self):
        self.Changecolor(6) 
        return self

    def __exit__(self, type, value, traceback):
        c.nocbreak()
        self.win.keypad(0)
        c.echo()
        c.endwin()
    
    def CreatePairs(self):
        c.init_pair(1,c.COLOR_WHITE,-1)
        c.init_pair(2,c.COLOR_YELLOW,-1)
        c.init_pair(3,c.COLOR_CYAN,-1)
        c.init_pair(4,c.COLOR_WHITE,c.COLOR_BLUE)
        c.init_pair(5,c.COLOR_YELLOW,c.COLOR_BLUE)
        c.init_pair(6,c.COLOR_CYAN,c.COLOR_BLUE)

class Subwindow(Init):
    def __init__(self,parent,y=0,x=0):
        self.parent = parent
        self.win = self.parent.win.subwin(y,x)
        return

class MainMenu(Subwindow):
    def __init__(self,parent):
        Subwindow.__init__(self,parent,y=1,x=1)
        self.Changecolor(5)
        self.createvars()
        self.Draw()
        return
    
    def Draw(self):
        self.H = 2
        self.W = self.parent.Dims()[1] - 2
        self.win.resize(self.H,self.W)
        return

    def createvars(self):
        self.menuelements = []
        self.currentpos = 0
        return

    def AddSel(self, namesel):
        self.menuelements.append({ 'name' : namesel, 'pos' : 0 })
        menulength = len(self.menuelements)
        pos = 0
        spacing = 3
        for index in xrange(len(self.menuelements)):
            if index == 0:
                pos += 1
            else:
                pos += spacing
            self.menuelements[index]['pos'] = pos
            pos += len(self.menuelements[index]['name'])
        self.WriteMenu()
        return

    def WriteMenu(self):
        y = 0
        for element in self.menuelements:
            x = element['pos']
            self.win.addstr(y,x,element['name'])
        self.win.hline(1,0,c.ACS_HLINE,self.W)
        return
    
    def Redraw(self):
        self.Sweep()
        self.parent.Sweep()
        self.parent.win.border(0)
        self.parent.Refresh()
        y,x = self.parent.Dims()
        c.resize_term(y,x)
        self.Draw()
        if len(self.menuelements): self.WriteMenu()
        return
