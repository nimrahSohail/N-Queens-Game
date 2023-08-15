#importing libraries

import pygame
from tkinter import*
from PIL import ImageTk,Image
import tkinter as tk


# create the board
def create_board(n):
    board = []

    for i in range(n):
        row = [0] * n
        board.append(row)

    return board


# if queen exists on board position, board value = 1 else value = 0
def solve_n_queens(board):

    if not problem_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


# check if queen can be placed in the position
def is_safe(board, row, col):
    n = len(board)
    clock = pygame.time.Clock()

    # check the row on left side
    for i in range(col):
        if board[row][i] == 1:
            for j in range(col):
                if board[row][j] == 2:
                    board[row][j] = 0
            return False
        board[row][i] = 2
        draw(board, n)
        clock.tick(2)

    # check for queens in upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False
        board[i][j] = 2
        draw(board, n)
        clock.tick(2)

    # check for queens in lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[x][y] == 2:
                    board[x][y] = 0
            return False
        board[i][j] = 2
        draw(board, n)
        clock.tick(2)

    return True


def problem_util(board, col):
    n = len(board)
    clock = pygame.time.Clock() # to delay display

    # if all queens are placed
    if col >= n:
        return True

    # for given column, try placing queens in each row
    for i in range(n):
        if is_safe(board, i, col):
            # place the queen on board[i][col] if it is safe to place it
            board[i][col] = 1

            draw(board, n)
            clock.tick(2)

            # recursively place the rest of the queens
            if problem_util(board, col + 1):
                return True

            # if placing the queen at board[i][col] does not provide a solution, remove it
            board[i][col] = 0

            draw(board, n)
            clock.tick(2)

    # if the queen cannot be placed in any row in this column
    return False


def draw(board, n):
    win = pygame.display.set_mode((800, 800))
    size = 800 // n
    queen_image = pygame.transform.scale(pygame.image.load('queen.jpg'), (size, size))

    # fill the window white
    win.fill((0, 0, 0))

    for i in range(n):
        for j in range(n):
            if board[j][i] == 0:
                pygame.draw.rect(win, (255, 255, 255), [i*size, j*size, size, size])
                pygame.display.update()

            elif board[j][i] == 1:
                pygame.draw.rect(win, (0, 0, 0), [i*size, j*size, size, size])
                win.blit(queen_image,(i*size,j*size))
                pygame.display.update()

            elif board[j][i] == 2:
                pygame.draw.rect(win, (255, 0, 0), [i*size, j*size, size, size])
                pygame.display.update()


# Print the solution and draw it on the board
def print_solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0
            print(board[i][j], end="  ")
        print()

    draw(board, n)



#gui
#import tkinter as tk
#from tkinter import *



# Label Class
class BulletLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        text = kwargs.pop('text', '')
        kwargs['text'] = self.bulletise(text)
        tk.Label.__init__(self, master, *args, **kwargs)

    def bulletise(self, text):
        if len(text) == 0:  # no text so no bullets
            return ''
        lines = text.split('\n')
        parts = []
        for line in lines:  # for each line
            parts.extend(['\u2022', line, '\n'])  # prepend bullet and re append newline removed by split
        return ''.join(parts)

    def configure(self, *args, **kwargs):
        text = kwargs.pop('text', '')
        if text != '':
            kwargs['text'] = self.bulletise(text)
        tk.Label.configure(*args, **kwargs)


#btn function
def btn(x, y, text, bcolor, fcolor, bd,screen,command):
    def on_enter(e):
        mybutton['background'] = bcolor
        mybutton['foreground'] = fcolor

    def on_leave(e):
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor

    mybutton = Button(screen, width=20, height=2, text=text,
                      fg=bcolor,
                      bg=fcolor,
                      border=0,
                      activeforeground=fcolor,
                      activebackground=bcolor,
                      borderwidth=bd,
                      command=command, )
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)
    mybutton.place(x=x, y=y)




def screen3():
    # screen 3
    game.destroy()
    screen3 = Tk()
    screen3.geometry('400x400')
    screen3.title('N-Queen')
    screen3.configure(bg='black')
    h = Label(screen3, text="ENTER VALUE OF N:", font=('Helvetica', 28, 'bold'), fg="#ffcc66", bg="#65573E")
    h.grid(padx=10, pady=20)

    # get user input for n
    def get_input():
        global valueN
        valueN.set(entry.get())
        print(entry.get())


    entry = Entry(screen3, width=42,bg='white',  bd=30, insertwidth=4)

    entry.place(relx=.5, rely=.3, anchor=CENTER)
    n = IntVar()

    # main function
    def main():
        #screen3.destroy()
        global n
        n =int(entry.get())
        pygame.init()
        board = create_board(n)
        solve_n_queens(board)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        solve_n_queens(board)


    btn(120, 200, "Start", "#ffcc66", "#141414", 9, screen3, main)
    screen3.mainloop()


# screen 2
def screen2():
    game.withdraw()
    root = tk.Tk()
    root.title("Instructions")
    root.geometry("600x500")
    root.configure(bg='black')

    h = Label(root, text="INSTRUCTIONS", font=('Helvetica', 28, 'bold'), fg="#ffcc66", bg="#65573E")
    h.pack()
    blabel = BulletLabel(root,
                         text='Select value of n which must be greater than 3\nClick on get started\nNow wait for the AI to complete the game',
                         font=('Helvetica', 18, 'bold'), fg="#ffcc66", bg="#65573E")
    blabel.pack()
    btn(230, 200, "Got it", "#ffcc66", "#141414", 9, root, screen3)
    root.mainloop()

#screen1

game=Tk()
game.title("N-Queen")
game.geometry('550x600')
game.configure(bg='black')

head=Label(game,text='N-Queen',bg='#65573E',fg='#ffcc66',font=('arial',30,'bold','italic'),width=10)
head.place(x=160,y=10)

btn(200, 100, "Get Help", "#ffcc66", "#141414", 9, game, screen2)
btn(200, 170, "Start", "#ffcc66", "#141414", 9, game, screen3)
canvas = Canvas(game, width = 500, height = 700)
canvas.place(x=25,y=250)
img = ImageTk.PhotoImage(Image.open("N-Queen.jpg"))
canvas.create_image(2, 2, anchor=NW, image=img)
game.mainloop()


#main()
