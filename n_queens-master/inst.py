import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Instructions")
root.geometry("600x500")
root.configure(bg="#65573E")

h=Label(root,text="INSTRUCTIONS" ,font=('Helvetica', 28, 'bold'), fg="#ffcc66", bg="#65573E")
h.pack()

class BulletLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        text = kwargs.pop('text', '')
        kwargs['text'] = self.bulletise(text)
        tk.Label.__init__(self, master, *args, **kwargs)

    def bulletise(self, text):
        if len(text) == 0: # no text so no bullets
            return ''
        lines = text.split('\n')
        parts = []
        for line in lines: # for each line
            parts.extend(['\u2022', line, '\n']) # prepend bullet and re append newline removed by split
        return ''.join(parts)

    def configure(self, *args, **kwargs):
        text = kwargs.pop('text', '')
        if text != '':
            kwargs['text'] = self.bulletise(text)
        tk.Label.configure(*args, **kwargs)

def btn(x,y,text,bcolor,fcolor,bd):
    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor
 
    
    mybutton = Button(root,width=20, height=2, text=text,
                      fg=bcolor,
                      bg=fcolor,
                      border=0,
                      activeforeground=fcolor,
                      activebackground=bcolor,
                      borderwidth=bd,
                      command=None,)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>",on_leave)
    mybutton.place(x=x,y=y)

    
blabel = BulletLabel(root, text='Select value of n which must be greater than 3\nClick on get started\nNow wait for the AI to complete the game', font=('Helvetica', 18, 'bold'), fg="#ffcc66", bg="#65573E")
blabel.pack()
btn(230,200,"Got it","#ffcc66","#141414",9)
root.mainloop()

 
 


















