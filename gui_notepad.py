from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
root.geometry("600x500")
def new():
    global file
    file=None
    root.title('Untitle - Notepad')
    text.delete(1.0,END)
def op():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if file == "":
        file=None
    else:
        root.title(os.path.basename(file)+' - Notepad')
        text.delete(1.0,END)
        f=open(file,'r')
        text.insert(1.0,f.read())
        f.close()
def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitle.txt',defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(text.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+' - Notepad')
    else:
        f=open(file,'w')
        f.write(text.get(1.0,END))
        f.close()

def cut():
    text.event_generate(('<<Cut>>'))
def copy():
    text.event_generate(('<<Copy>>'))
def paste():
    text.event_generate(('<<Paste>>'))
def about():
    tmsg.showinfo('about','notepad by codewithveer')
file=None
text=Text(root,font='lucida 12')
s=Scrollbar(root)
s.pack(side=RIGHT,fill=Y)
text.config(yscrollcommand=s.set)
s.config(command=text.yview)


m=Menu(root)
sm=Menu(m,tearoff=0)

sm.add_command(label='New file',command=new)
sm.add_command(label='Open',command=op)
sm.add_command(label='Save as',command=save)
sm.add_separator()
sm.add_command(label='Exit',command=quit)
m.add_cascade(label='File',menu=sm)

sm=Menu(m,tearoff=0)
sm.add_command(label='Cut',command=cut)
sm.add_command(label='Copy',command=copy)
sm.add_command(label='Paste',command=paste)
m.add_cascade(label='Edit',menu=sm)

sm=Menu(m,tearoff=0)
sm.add_command(label='About',command=about)
m.add_cascade(label='Help',menu=sm)

root.config(menu=m)
text.pack(fill=BOTH)


root.mainloop()
