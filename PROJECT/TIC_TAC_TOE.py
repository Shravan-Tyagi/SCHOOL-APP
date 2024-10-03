#SARC INDUSTRIES
#TIC TAC TOE


from tkinter import *
from turtle import *
from tkinter.font import Font
import random as ran
import time
import os
root=Toplevel()
root.geometry("700x500+300+50")



#Turtle

def turt(): 
    t.pensize(15)
    t.speed(4)
    t.up()
    t.setpos(-173,80)
    t.down()
    t.forward(372)
    t.up()
    t.setpos(-173,-35)
    t.down()
    t.forward(372)

    t.up()
    t.setpos(-51,190)
    t.down()
    t.right(90)
    t.forward(335)
    t.up()
    t.setpos(79,190)
    t.down()
    t.forward(335)
    but()

#Buttons

def but():
    global b1
    global b2
    global b3
    global b4
    global b5
    global b6
    global b7
    global b8
    global b9
    if(choice==2):
        b1=Button(c,width=15, height=6, bg='snow', command=b1_)
        b2=Button(c,width=15, height=6, bg='snow', command=b2_)
        b3=Button(c,width=15, height=6, bg='snow', command=b3_)
        b4=Button(c,width=15, height=6, bg='snow', command=b4_)
        b5=Button(c,width=15, height=6, bg='snow', command=b5_)
        b6=Button(c,width=15, height=6, bg='snow', command=b6_)
        b7=Button(c,width=15, height=6, bg='snow', command=b7_)
        b8=Button(c,width=15, height=6, bg='snow', command=b8_)
        b9=Button(c,width=15, height=6, bg='snow', command=b9_)

        b1.place(x=175,y=60)
        b2.place(x=305,y=60)
        b3.place(x=435,y=60)
        b4.place(x=175,y=175)
        b5.place(x=305,y=175)
        b6.place(x=435,y=175)
        b7.place(x=175,y=290)
        b8.place(x=305,y=290)
        b9.place(x=435,y=290)

    if(choice==1):
        b1=Button(c,width=15, height=6, bg='snow', command=b1__)
        b2=Button(c,width=15, height=6, bg='snow', command=b2__)
        b3=Button(c,width=15, height=6, bg='snow', command=b3__)
        b4=Button(c,width=15, height=6, bg='snow', command=b4__)
        b5=Button(c,width=15, height=6, bg='snow', command=b5__)
        b6=Button(c,width=15, height=6, bg='snow', command=b6__)
        b7=Button(c,width=15, height=6, bg='snow', command=b7__)
        b8=Button(c,width=15, height=6, bg='snow', command=b8__)
        b9=Button(c,width=15, height=6, bg='snow', command=b9__)

        b1.place(x=175,y=60)
        b2.place(x=305,y=60)
        b3.place(x=435,y=60)
        b4.place(x=175,y=175)
        b5.place(x=305,y=175)
        b6.place(x=435,y=175)
        b7.place(x=175,y=290)
        b8.place(x=305,y=290)
        b9.place(x=435,y=290)

def pc_turn(a,b):
    root.update_idletasks()
    time.sleep(1.5)
    if a=='z':
        turn=ran.randrange(1,9)
        while turn in b[0]:
            while turn in b[1]:
                turn=ran.randrange(1,9)
                print(turn)
        chances[1].append(turn)
        print(chances)
        
        if len(chances[1])==4 or len(chances[0])==5 :
            end()
        
        if turn==1:
            b1.config(width=108, height=95,image=cross_)
        if turn==2:
            b2.config(width=108, height=95,image=cross_)
        if turn==3:
            b3.config(width=108, height=95,image=cross_)
        if turn==4:
            b4.config(width=108, height=95,image=cross_)
        if turn==5:
            b5.config(width=108, height=95,image=cross_)
        if turn==6:
            b6.config(width=108, height=95,image=cross_)
        if turn==7:
            b7.config(width=108, height=95,image=cross_)
        if turn==8:
            b8.config(width=108, height=95,image=cross_)
        if turn==9:
            b9.config(width=108, height=95,image=cross_)
    else:
        turn=ran.randrange(1,9)
        while turn in b[0]:
            while turn in b[1]:
                turn=ran.randrange(1,9)
        chances[1].append(turn)
        if len(chances)==9:
            end()
        if turn==1:
            b1.config(width=108, height=95,image=zero_)
        if turn==2:
            b2.config(width=108, height=95,image=zero_)
        if turn==3:
            b3.config(width=108, height=95,image=zero_)
        if turn==4:
            b4.config(width=108, height=95,image=zero_)
        if turn==5:
            b5.config(width=108, height=95,image=zero_)
        if turn==6:
            b6.config(width=108, height=95,image=zero_)
        if turn==7:
            b7.config(width=108, height=95,image=zero_)
        if turn==8:
            b8.config(width=108, height=95,image=zero_)
        if turn==9:
            b9.config(width=108, height=95,image=zero_)
        
def end():
    root.update_idletasks()
    time.sleep(0.5)
    for wi in c.winfo_children():
        wi.destroy()
    Label(c, text="Win", font=font1).place(x=300,y=300)
    root.update_idletasks()
    time.sleep(1)
    turt()
#Commands

rootpath=os.path.dirname(__file__)
rootpath=rootpath+"\\"
zero=PhotoImage(file=rootpath+"zero.png")
zero_=zero.subsample(2)
cross=PhotoImage(file=rootpath+"cross2.png")
cross_=cross.subsample(2)
def b1_():
    b1.config(width=108, height=95,image=zero_)
    chances[0].append(1)
    pc_turn('z',chances)
def b2_():
    b2.config(width=108, height=95,image=zero_)
    chances[0].append(2)
    pc_turn('z',chances)
def b3_():
    b3.config(width=108, height=95,image=zero_)
    chances[0].append(3)
    pc_turn('z',chances)
def b4_():
    b4.config(width=108, height=95,image=zero_)
    chances[0].append(4)
    pc_turn('z',chances)
def b5_():
    b5.config(width=108, height=95,image=zero_)
    chances[0].append(5)
    pc_turn('z',chances)
def b6_():
    b6.config(width=108, height=95,image=zero_)
    chances[0].append(6)
    pc_turn('z',chances)
def b7_():
    b7.config(width=108, height=95,image=zero_)
    chances[0].append(7)
    pc_turn('z',chances)
def b8_():
    b8.config(width=108, height=95,image=zero_)
    chances[0].append(8)
    pc_turn('z',chances)
def b9_():
    b9.config(width=108, height=95,image=zero_)
    chances[0].append(9)
    pc_turn('z',chances)


def b1__():
    b1.config(width=108, height=95,image=cross_)
    chances[0].append(1)
    pc_turn('c',chances)
def b2__():
    b2.config(width=108, height=95,image=cross_)
    chances[0].append(2)
    pc_turn('c',chances)
def b3__():
    b3.config(width=108, height=95,image=cross_)
    chances[0].append(3)
    pc_turn('c',chances)
def b4__():
    b4.config(width=108, height=95,image=cross_)
    chances[0].append(4)
    pc_turn('c',chances)
def b5__():
    b5.config(width=108, height=95,image=cross_)
    chances[0].append(5)
    pc_turn('c',chances)
def b6__():
    b6.config(width=108, height=95,image=cross_)
    chances[0].append(6)
    pc_turn('c',chances)
def b7__():
    b7.config(width=108, height=95,image=cross_)
    chances[0].append(7)
    pc_turn('c',chances)
def b8__():
    b8.config(width=108, height=95,image=cross_)
    chances[0].append(8)
    pc_turn('c',chances)
def b9__():
    b9.config(width=108, height=95,image=cross_)
    chances[0].append(9)
    pc_turn('c',chances)
    
#Canvas

c=Canvas(root, width=700, height=500)
c.pack()
l=Label(root, text="Best Viewed In '700x500' screen size" )
l.pack()

t=RawTurtle(c)
t.ht()
c.config(bg='snow')
t.pensize(15)
t.speed(1)
t.up()
t.setpos(-230,100)
t.down()
t.write('Tic Tac Toe', font=('times',70,'bold'))
t.up()
t.setpos(-200,-240)
t.down()
t.write('SARC INDUSTRIES', font=('times',30,'bold'))


def cro():
    global choice
    choice=1
    for wi in c.winfo_children():
        wi.destroy()
    turt()
def zer():
    global choice
    choice=2
    for wi in c.winfo_children():
        wi.destroy()
    turt()

choice=0
chances=[[],[]]
font1=Font(family='broadway', size=35)
l2=Label(c, text="OR", font=font1)
l2.place(x=290,y=230)

cr=Button(c,image=cross_, command=cro)
ze=Button(c,image=zero_, command=zer)
cr.place(x=150,y=200)
ze.place(x=400,y=200)



#End

root.mainloop()
