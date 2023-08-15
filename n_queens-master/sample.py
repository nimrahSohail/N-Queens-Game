from tkinter import *
from PIL import ImageTk,Image
# first screen
game=Tk()
game.title("N-Queen")
game.geometry('550x800')
game.configure(bg='cyan')
head=Label(game,text='N-Queen',bg='pink',font=('arial',30,'bold','italic'),width=10)
head.grid(padx=20,pady=20)
def help():
    print('helpp')
help=Button(game,text='Get help',bg='pink',font=('arial',10,'bold','italic'),command=help,width=20, height=2)
help.grid(padx=10,pady=20)

start=Button(game,text='Get Start',bg='pink',font=('arial',10,'bold','italic'),command=help,width=20, height=2)
start.grid(padx=10,pady=20)
canvas = Canvas(game, width = 500, height = 700)
canvas.grid(padx=20,pady=20)
img = ImageTk.PhotoImage(Image.open("N-Queen.jpg"))
canvas.create_image(2, 2, anchor=NW, image=img)
game.mainloop()

