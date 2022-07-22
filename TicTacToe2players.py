# imports - os, sys, tkinter, partial, random, font
import os
import sys
from tkinter import *
from tkinter import font
from functools import partial

#resource function
def path(rp):
    try:
        bp = sys._MEIPASS
    except:
        bp = os.path.abspath('.')
    return os.path.join(bp,rp)

# configuation
root = Tk()
root.title('TicTacToe')
root.resizable(0,0)
root.configure(height=500, width=500, padx=50, pady=50)
root.iconbitmap(path('icon.ico'))

# constants
BLUE = '#6785b5'
RED = '#673444'
DARKRED = '#540d0f'
GREEN = '#399e18'
FONT = font.Font(root, size=40)
YELLOW = '#c2a62d'

# configurations
CONFIGURATION = {
    'height' : 1,
    'width' : 3,
    'borderwidth' : 20,
    'background' : BLUE,
    'activebackground' : BLUE,
    'font' : FONT,
    'fg' : DARKRED
}

# game board
class Board:
    def __init__(self):
        self.board = [None] * 9
        self.player = True
        self.current = {True:'X' , False:'O'}
        self.gameover = False
        self.moves = 0
        
        for i in range(9):
            self.board[i] = Button(root, CONFIGURATION, command=partial(self.move , i))
            self.board[i].grid(row=i//3, column=i%3)

    def move(self, i):
        if self.gameover:
            return None

        if self.board[i]['text'] != '':
            return None
    
        self.moves += 1
        self.board[i]['text'] = self.current[self.player]
        self.board[i]['activebackground'] = RED

        

        if self.condition() is not None:
            self.gameover = True
            
        elif self.moves == 9:
            self.gameover = True
            for box in self.board:
                box['background'] = YELLOW

        self.player = not self.player
        

    def condition(self):        
        for i in range(3):
            if self.board[i*3]['text'] and self.board[i*3]['text'] == self.board[i*3+1]['text'] == self.board[i*3+2]['text']:
                self.board[i*3]['background'] = self.board[i*3+1]['background'] = self.board[i*3+2]['background'] = GREEN
                return self.player

            if self.board[i]['text'] and self.board[i]['text'] == self.board[i+1*3]['text'] == self.board[i+2*3]['text']:
                self.board[i]['background'] = self.board[i+1*3]['background'] = self.board[i+2*3]['background'] = GREEN
                return self.player
        
        if self.board[0]['text'] and self.board[0]['text'] == self.board[4]['text'] == self.board[8]['text']:
            self.board[0]['background'] = self.board[4]['background'] = self.board[8]['background'] = GREEN
            return self.player

        if self.board[2]['text'] and self.board[2]['text'] == self.board[4]['text'] == self.board[6]['text']:
            self.board[2]['background'] = self.board[4]['background'] = self.board[6]['background'] = GREEN
            return self.player

        return None
      
# game loop
board = Board()
root.mainloop()