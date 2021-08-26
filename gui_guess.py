from tkinter import *
import tkinter.messagebox as tmsg
import random
i=10
r=random.randint(1,99)
def check():
    global i
    i-=1
    if i>0:
        if r==int(s.get()):
            tmsg.showinfo('Guess game','Congrats!! you won $100')
            i=10
            s.set('')
            l['text']=f'you have {i} numbers of attempts left'
        elif r>int(s.get()):
            l['text']=f'you have {i} numbers of attempts left. choose greater number!'
        else:
            l['text']=f'you have {i} numbers of attempts left. choose lesser number!'
    else:
        tmsg.showinfo('Guess game',f'you lose the game!the guessing number is {r} Better luck next time!!')
        i=10
        l['text']=f'you have {i} numbers of attempts left'
root = Tk()
root.geometry('400x250')
root.title('Guess the number')
Label(root,text='Guess the number between 1 and 99').pack()
s=StringVar()
Entry(root,textvariable=s).pack()
Button(root,text='Check',command=check).pack()
Button(root,text='Quit',command=quit).pack()
l=Label(root,text='You have 10 attempts remaining! Good Luck!')
l.pack()


root.mainloop()

