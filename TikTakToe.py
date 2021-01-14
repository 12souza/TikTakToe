from tkinter import *

master = Tk()

canvas_w = 840
canvas_h = 480

turn = 0
gameOver = 0

master.resizable(False, False)
w = Canvas(master, width = canvas_w, height = canvas_h)



table = {'1' : None,
        '2': None,
        '3': None,
        '4': None,
        '5': None,
        '6': None,
        '7': None,
        '8': None,
        '9': None
        }

spotsAvailable = list(table)

def DrawBoard():
    y = int(canvas_h / 3)
    ww = int(canvas_w / 3)
    w.create_line(0,y,canvas_w, y, fill = '#000000', width = 5)
    w.create_line(0,y*2,canvas_w, y*2, fill = '#000000', width = 5)
    w.create_line(ww, 0, ww, canvas_h, fill = '#000000', width = 5)
    w.create_line(ww*2, 0, ww*2, canvas_h, fill = '#000000', width = 5)

def DrawX(x, y):
    w.create_line(x, y, x + 100, y + 100, fill = '#000000', width = 2)
    w.create_line(x + 100, y, x, y + 100, fill = '#000000', width = 2)

def DrawO(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, width = 3)

def key(event):
    print ("pressed", repr(event.char))

def CheckWinner():
    global gameOver
    global spotsAvailable
    a = table['1']
    b = table['2']
    c = table['3']
    d = table['4']
    e = table['5']
    f = table['6']
    g = table['7']
    h = table['8']
    i = table['9']

    if a == b and b == c and a == c:
        if a == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif a == 1:
            print("Player 2 is the winner!")
            gameOver = 1
        
    if d == e and e == f and d == f:
        if d == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif d == 1:
            print("Player 2 is the winner!")
            gameOver = 1

    if g == h and h == i and g == i:
        if g == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif g == 1:
            print("Player 2 is the winner!")
            gameOver = 1

    if a == d and d == g and a == g:
        if a == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif a == 1:
            print("Player 2 is the winner!")
            gameOver = 1

    if b == h and b == e and e == h:
        if b == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif b == 1:
            print("Player 2 is the winner!")
            gameOver = 1

    if c == f and f == i and c == i:
        if c == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif c == 1:
            print("Player 2 is the winner!")
            gameOver = 1
  
    if a == e and e == i and a == i:
        if a == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif a == 1:
            print("Player 2 is the winner!")
            gameOver = 1

    if c == g and e == g and c == g:
        if c == 0:
            print("Player 1 is the winner!")
            gameOver = 1
        elif c == 1:
            print("Player 2 is the winner!")
            gameOver = 1  
    if(gameOver == 0 and len(spotsAvailable) == 0):
        print("Tie!")
        gameOver = 1  

def BoxClick(event):
    global turn
    global gameOver
    global spotsAvailable

    x = event.x
    y = event.y
    if(gameOver == 0):
        if((x > 0 and x < 280) and (y > 0 and y < 160) and (table['1'] == None)):
            if(turn == 0):
                DrawX(72, 25)
                turn = 1
                print("Box 1 clicked and belongs to player 1")
                table['1'] = 0
                spotsAvailable.remove('1')
            else:
                DrawO(125, 75, 50, w)
                turn = 0
                print("Box 1 clicked and belongs to player 2")
                table['1'] = 1
                spotsAvailable.remove('1')
        if((x > 281 and x < 560) and (y > 0 and y < 160) and (table['2'] == None)):
            if(turn == 0):
                DrawX(352, 25)
                turn = 1
                print("Box 2 clicked and belongs to player 1")
                table['2'] = 0
                spotsAvailable.remove('2')
            else:
                DrawO(405, 75, 50, w)
                turn = 0
                print("Box 2 clicked and belongs to player 2")
                table['2'] = 1
                spotsAvailable.remove('2')
        if((x > 561 and x < 840) and (y > 0 and y < 160) and (table['3'] == None)):
            if(turn == 0):
                DrawX(632, 25)
                turn = 1
                print("Box 3 clicked and belongs to player 1")
                table['3'] = 0
                spotsAvailable.remove('3')
            else:
                DrawO(685, 75, 50, w)
                turn = 0
                print("Box 3 clicked and belongs to player 2")
                table['3'] = 1
                spotsAvailable.remove('3')
        if((x > 0 and x < 280) and (y > 161 and y < 320) and (table['3'] == None)):
            if(turn == 0):
                DrawX(72, 185)
                turn = 1
                print("Box 4 clicked and belongs to player 1")
                table['4'] = 0
                spotsAvailable.remove('4')
            else:
                DrawO(125, 235, 50, w)
                turn = 0
                print("Box 4 clicked and belongs to player 2")
                table['4'] = 1
                spotsAvailable.remove('4')
        if((x > 281 and x < 560) and (y > 161 and y < 320) and (table['5'] == None)):
            if(turn == 0):
                DrawX(352, 185)
                turn = 1
                print("Box 5 clicked and belongs to player 1")
                table['5'] = 0
                spotsAvailable.remove('5')
            else:
                DrawO(405, 235, 50, w)
                turn = 0
                print("Box 5 clicked and belongs to player 2")
                table['5'] = 1
                spotsAvailable.remove('5')
        if((x > 561 and x < 840) and (y > 161 and y < 320) and (table['6'] == None)):
            if(turn == 0):
                DrawX(632, 185)
                turn = 1
                print("Box 6 clicked and belongs to player 1")
                table['6'] = 0
                spotsAvailable.remove('6')
            else:
                DrawO(685, 235, 50, w)
                turn = 0
                print("Box 6 clicked and belongs to player 2")
                table['6'] = 1
                spotsAvailable.remove('6')
        if((x > 0 and x < 280) and (y > 321 and y < 480) and (table['7'] == None)):
            if(turn == 0):
                DrawX(72, 345)
                turn = 1
                print("Box 7 clicked and belongs to player 1")
                table['7'] = 0
                spotsAvailable.remove('7')
            else:
                DrawO(125, 395, 50, w)
                turn = 0
                print("Box 7 clicked and belongs to player 2")
                table['7'] = 1
                spotsAvailable.remove('7')
        if((x > 281 and x < 560) and (y > 321 and y < 480) and (table['8'] == None)):
            if(turn == 0):
                DrawX(352, 345)
                turn = 1
                print("Box 8 clicked and belongs to player 1")
                table['8'] = 0
                spotsAvailable.remove('8')
            else:
                DrawO(405, 395, 50, w)
                turn = 0
                print("Box 8 clicked and belongs to player 2")
                table['8'] = 1
                spotsAvailable.remove('8')
        if((x > 561 and x < 840) and (y > 321 and y < 480) and (table['9'] == None)):
            if(turn == 0):
                DrawX(632, 345)
                turn = 1
                print("Box 9 clicked and belongs to player 1")
                table['9'] = 0
                spotsAvailable.remove('9')
            else:
                DrawO(685, 395, 50, w)
                turn = 0
                print("Box 9 clicked and belongs to player 2")
                table['9'] = 1
                spotsAvailable.remove('9')
        print(table)
        lengthSelect = len(list(table))
        print(lengthSelect)
        if(lengthSelect >= 5):
            CheckWinner()
        

w.bind("<Key>", key)
w.bind("<Button-1>", BoxClick)
#DrawO(125, 75, 50, w)
#DrawX(75,25)
w.pack()
DrawBoard()


mainloop()