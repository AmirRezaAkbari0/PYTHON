from tkinter import *
from random  import choices

def coode():
    A=list("ABCDEF123567890")
    res='#'
    cod = choices(A,k=6)
    res += "".join(cod)
    return res
def W():
    c=coode()
    E.config(bg=c)
    E.delete(0,END)
    E.insert(0,c)
    root.config(bg = c)

root = Tk()   
root.geometry("250x150")
b=Button(text="RUN",command=W,bg='black',fg='white',width=10)
b.config(borderwidth=5)
b.place(x=70,y=75)

E=Entry(root,bd=8,bg='white',fg='black',font=('bold'))
E.place(x=5,y=20)

root.mainloop()



