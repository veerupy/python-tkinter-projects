from tkinter import *
root=Tk()
root.geometry("425x450")
root.title('CALCULATOR')
f=Frame(root)
s=StringVar()
w=Entry(root,textvariable=s,font='lucida 40')
w.pack(fill=X)
f.pack(fill=BOTH)


l=[['7','8','9','/','C'],['4','5','6','*','='],['1','2','3','-','00'],['0','.','%','+','//']]

def click(event):
    global s
    t=event.widget.cget('text')
    if t=='C':
        s.set("")
    elif t=='=':
        try:
            s.set(eval(s.get()))
        except:
            s.set('error')
    else:
        s.set(s.get()+t)
for i in range(4):
    f=Frame(root,bg='grey')
    b=Button(f,text=l[i][0],font='lucida 30',relief=SUNKEN)
    b.bind('<Button-1>',click)
    b.pack(padx=15,pady=15,side=LEFT)

    b=Button(f,text=l[i][1],font='lucida 30')
    b.bind('<Button-1>',click)
    b.pack(padx=15,pady=15,side=LEFT)
    

    b=Button(f,text=l[i][2],font='lucida 30')
    b.bind('<Button-1>',click)
    b.pack(padx=15,pady=15,side=LEFT)

    b=Button(f,text=l[i][3],font='lucida 30')
    b.bind('<Button-1>',click)
    b.pack(padx=15,pady=15,side=LEFT)

    b=Button(f,text=l[i][4],font='lucida 30')
    b.bind('<Button-1>',click)
    b.pack(padx=15,pady=15,side=LEFT)
    f.pack()




root.mainloop()
