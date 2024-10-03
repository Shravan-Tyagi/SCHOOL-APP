#SARC INDUSTRIES™
#CS PROJECT
#BY SHRAVAN TYAGI
#1st JUNE 2019



''' IMPORTS: '''



#import matplotlib.pyplot as plt
import PIL.Image as pi
import PIL.ImageTk as pik
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog 
from turtle import *
import os, platform, subprocess, re	
import time
import calendar as cald
import sqlite3 
import random


import speech_recognition as sr
import gtts
import pyttsx3
from gtts import gTTS
from playsound import playsound
from tempfile import TemporaryFile
from pygame import mixer
import requests
import urllib.request
import urllib.parse
import textwrap
import wikipedia as wp
import webbrowser
#import pafy
#import vlc



 #INITIALISING:

time.sleep(1)
print("\n\n")
print("                                                 SARC ",end="")
time.sleep(1.2)
print("  INDUSTRIES",end="\r")
#print("\n\n\n\n")
time.sleep(1.5)
print("                                               C.S.    PROJECT    2019\n\n")
time.sleep(1)
print("                                             MADE   BY   SHRAVAN\n")
time.sleep(2)
print() 
time.sleep(1)

a="##"    
b="  "*10
c=9
d=10 
print("  Initiating "+" "*22+"0%",end="\r") 
time.sleep(1)
for i in range(10):
    e=random.randrange(20)
    print("  Initiating "+a+b+str(d)+"%",end="\r") 
    time.sleep(e/10) 
    a+="##" 
    b="  "*c
    c-=1
    d+=10
time.sleep(0.6)


rootpath2=os.path.dirname(__file__)
#rootpath2=rootpath2+"/"
rootpath=rootpath2
connection =sqlite3.connect(os.path.join(rootpath2,'Hogwards.db'))
crsr = connection.cursor() 

try:
    times_used=open(os.path.join(rootpath2,"Run_times.txt"),'r') 
    saved=times_used.read()
    numbr=int(saved)
except:
    numbr=0
numbr+=1
saved=str(numbr)
times_used =open(os.path.join(rootpath2,"Run_times.txt"),'w') 
times_used.write(saved)
times_used.flush()



''' ROOT WINDOW START: '''

print(rootpath+"logo.png")
print(rootpath2)
#tur=Turtle() 
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
#root.geometry("%dx%d+0+0"%(w, h)) 
root.state("zoomed")
poto=PhotoImage(file=rootpath+"logo.png")
root.iconphoto(False, poto)
root.title("HOGWARDS INTERNATIONAL SCHOOL") 


''' SARC INDUSTRIES™: '''

inicanvas=Canvas(root,width=1280,height=720)
inicanvas.pack()
initurt=RawTurtle(inicanvas)
initurt.ht()
initurt.penup()
initurt.setpos(150,80)

initurt.pendown()
initurt.pensize(10)
initurt.speed(5)
initurt.pencolor('red')
time.sleep(1)

for i in range(3):
    inicanvas.config(bg='lavender')
    root.update_idletasks()
    time.sleep(0.1)
    inicanvas.config(bg='yellow')
    root.update_idletasks()
    time.sleep(0.1)
    inicanvas.config(bg='black')
    root.update_idletasks()
    time.sleep(0.1)
    inicanvas.config(bg='blue')
    root.update_idletasks()
    time.sleep(0.1)
    inicanvas.config(bg='red')
    root.update_idletasks()
    time.sleep(0.1)
    inicanvas.config(bg='white')
    root.update_idletasks()
    time.sleep(0.1)
    


initurt.speed(3)
initurt.pencolor('blue')
initurt.backward(400)
initurt.left(80)
initurt.forward(55)
initurt.speed(5)
initurt.left(100)
initurt.speed(12)
initurt.forward(10)
initurt.right(105)
initurt.forward(45)
initurt.left(140)
for i in range(10):
    initurt.left(i-1)
    initurt.forward(i+2)
initurt.forward(2)
initurt.left(1)
initurt.forward(2)
initurt.left(1)
initurt.forward(2)
initurt.left(110)
initurt.forward(10)
initurt.right(105)
initurt.forward(35)
initurt.right(80)
initurt.forward(10)
initurt.left(80)
initurt.speed(5)
initurt.forward(45)
initurt.left(107)
initurt.forward(450)

initurt.speed(2)
inicanvas.config(bg='black')
initurt.penup()
initurt.setpos(-230,80)
initurt.pendown()
initurt.write('S', font=('times',70,'bold'))
initurt.penup()
initurt.setpos(-175,80)
initurt.pendown()
initurt.write('A', font=('times',70,'bold'))
initurt.penup()
initurt.setpos(-115,80)
initurt.pendown()
initurt.write('R', font=('times',70,'bold'))
initurt.penup()
initurt.setpos(-50,80)
initurt.pendown()
initurt.write('C', font=('times',70,'bold'))

initurt.speed(2)
initurt.penup()
initurt.setpos(-250,-20)
initurt.pendown()
initurt.write('INDUSTRIES', font=('broadway',50,'bold'))


time.sleep(0.8)
initurt.pencolor('grey')
initurt.penup()
initurt.setpos(15,150)
initurt.pendown()
initurt.write('TM', font=('broadway',20))

time.sleep(3)
inicanvas.destroy()


#HOMEWORK:

homework=[]
subjecthw=[]

try:
    file=open(os.path.join(rootpath2,"homework.txt"),'r')
    mess=file.readlines()
    for i in mess:
        a=i.split(":")
        homework.append(a[1])
        subjecthw.append(a[0])
    file.close()
except:
    homework=[]
    subjecthw=[]


#COMMUNICATIONS:

feedback=[]
feedstud=[]
try:
    file=open(os.path.join(rootpath2,"communications.txt"),'r')
    mess=file.readlines()
    for i in mess:
        a=i.split(":")
        feedback.append(a[1])
        feedstud.append(a[0])
    file.close()
except:
    feedback=[]
    feedstud=[]


#ATTENDANCE:

attendance=[]
try:
    file=open(os.path.join(rootpath2,"attendance.txt"),'r')
    mess=file.readlines()
    for i in mess:
        a=i.split(":")
        listt=[]
        listt.append(a[0])
        b=a[1].split(",")
        listt.append(b)
        attendance.append(listt)
    file.close()
except:
    attendance=[]


#COMMANDS:

def manage():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2200, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="MANAGEMENT", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=300,y=100)
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='black') 
    C.place(x=270,y=550)
    global p1_
    p1=pi.open(rootpath+"ts2.jpeg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""The Hogwards International registered under the Societies Registration Act 1860 is an apex body of Hogwards International School. The Society was established in the year 1965 by eminent magicians and social workers.  
They have played a key role in setting up this Institution. The society is serving the noble cause of Children's education and have earned a name in the "CALIFORNIA AREA."\n
Anthony Stark, Director started his journey with Hogwards School, California in 1979. At that time, it was a middle school running in Tents and sheds with the strength of 743 students. He with his untiring efforts could make it a Secondary School in 1984 and Sr. Secondary School in 1985 and International school in 1999.\n
He is a man of sensitive Heart, well behaved, loving nature and pleasing personality. With his commitment, dedication and thorough involvement for the progress and development of the school, he sorted out even the most complicated issues with his iron will, knowledge and competency and also his money.\n
 Always motivating, encouraging and appreciating, he puts fresh energy into all who are associated with the school. Under his guidance, the school with over 62500 students is ready to reach new pinnacles of success.\n""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1250)
    
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
def principal():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2400, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="PRINCIPAL", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=350,y=100)
    
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='cornflower blue') 
    C.place(x=270,y=550)
    global p1_
    p1=pi.open(rootpath+"dum.jpeg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""OBJECTIVES :
To select a curriculum that prepares the students for the high standards required of them.
To organize the course of study in a sequential and graded manner.
To lay the foundation for International study courses.
To raise the standard of English to meet the demands of the high level of proficiency required in the language as the medium of instruction and study.
To create an environment conducive to the holistic development of the students.
To ensure that the students are equipped with the life skills required to face future challenges with fortitude.
To inspire the students to take independent and valuable decisions.
To encourage self study under the guidance of a teacher facilitator.
To nurture the Indianness of the students within a multi cultural ethnic framework.
To encourage the spiritual growth of every child through value based education.
To inculcate the best in the student by providing an environment in which every student discover and realizes his or her potential.
To communicate regularly and work closely with the parents of every student towards his/her academic, emotional and spiritual growth.
To evoke brotherhood consiousness amongst Children and maintain a congenial and peaceful atmosphere and live in a cohesive manner.
To create the atmosphere where students are ignited with a quest for learning, Spirt of enquiry and scientific temperament.
To arrange workshops to update the knowledge base and latest trends in education.
To follow a unique strategy to keep our academic processes as exhilarating as possible.
To focous on the uncompromising standards of our academic quality.
To channelize the immense energy of children through a plethora of activities for their overall development.
To nurture  in our students that love is more precious asset than success; Compassion is more of a prized possession than any of the professional expertise.""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1250)
    
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
def faculty():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2000, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="FACULTY", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=360,y=100)
    

    Label(lc, text="ALL STAFF MEMBERS OF HOGWARDS \nINTERNATIONAL SCHOOL", font=Font(family='berlin sans fb', size=30), bg='snow', fg="cornflower blue").place(x=130,y=400)
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='black') 
    C.place(x=270,y=650)
    global p1_
    p1=pi.open(rootpath+"staff.jpg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
   
def isa():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

        
    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2200, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="ISA CERTIFICATION", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=240,y=100)
    
     #PHOTO:
    
    C=Canvas(frame,width=800, height=400, bg='black',bd=0) 
    C.place(x=220,y=550)
    global p1_
    p1=pi.open(rootpath+"bc.png")
    p1=p1.resize((800,400), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    

    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""To expose our students to the world -one community in the borderless world and to keep pace with the global scenario in education, our school is constantly upgrading the learning process and updating the international practices in education. So, we have embarked upon the ISA Journey.

The ISA is the British Council's principal accreditation scheme and has been running successfully in U.K for over ten years. The aim of ISA is to encourage and support the students to develop an international ethos and a collaborative curriculum- based work with a number of partner schools i.e involvement of the wider community, fostering an international dimensions in the curriculum is at the heart of the british council’s work with school, so that the young people can gain the cultural understanding and international skills. They need to live and work as global citizen. In this world of globalization, international skill is very important. So, everything the school is doing is a vital preparation for life in a global society and work in a global economy.

Our international activities are making the children more aware of community and global issues. We will continue to expand and develop our international work which is now embedded in the culture of the school.""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1150)
    
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
def adm2019():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

        
    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=1500, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="ADMISSION 2019", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=270,y=100)

    Label(lc, text="Admission closed for 2019", font=Font(family='times new roman', size=20), bg='snow', fg="cornflower blue").place(x=150,y=500)

    #PHOTO:
    
    C=Canvas(frame,width=350, height=500, bg='snow',bd=0) 
    C.place(x=720,y=500)
    global p1_
    p1=pi.open(rootpath+"add.png")
    p1=p1.resize((350,500), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
def reg2019():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

        
    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=1500, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="REGISTRATION 2019", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=270,y=100)

    Label(lc, text="Registration closed for 2019", font=Font(family='times new roman', size=20), bg='snow', fg="cornflower blue").place(x=150,y=500)


    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
def acad():
    print("yo")

def calendar(event):
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()



    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2400, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="CALENDAR", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=350,y=100)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    #CALENDAR:
    pcal= cald.TextCalendar(firstweekday = 0) 
    global year
    year=2019
    ft=Font(family='bernard mt', size=14)
    txt=Message(lc, text=pcal.formatyear(2019,w=4,l=1,c=8,m=2),bg="snow",width=900, font=ft) 
    txt.place(x=200,y=450)
    
    def nxt():
        global year
        year+=1
        txt=Message(lc, text=pcal.formatyear(year,3),bg="snow",width=900, font=ft) 
        txt.place(x=200,y=450)
        global nimg, nimg_
        Button(lc,image=nimg, command=nxt).place(x=800,y=450)
        Button(lc,image=nimg_, command=prev).place(x=100,y=450)
    
    def prev():
        global year
        year-=1
        txt=Message(lc, text=pcal.formatyear(year,3),bg="snow",width=900, font=ft) 
        txt.place(x=200,y=450)   
        global nimg, nimg_
        Button(lc,image=nimg, command=nxt).place(x=800,y=450)
        Button(lc,image=nimg_, command=prev).place(x=100,y=450)
     
    global nimg, nimg_
    nimg=PhotoImage(file=rootpath+"next.png")
    nimg=nimg.subsample(2,2)
    nimg_=nimg.subsample(-1,1)
    Button(lc,image=nimg, command=nxt).place(x=800,y=450)
    Button(lc,image=nimg_, command=prev).place(x=100,y=450)
    

def exam():
    time.sleep(1)
    for wi in frame.winfo_children():
        wi.destroy()
    examcanvas=Canvas(frame,width=500, height=500, bg='black') 
    examcanvas.place(x=600,y=150)
def result():
    print("yo")
def rules():
    print("yo")
def classroom():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2300, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="CLASS ROOMS", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=300,y=100)
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='black') 
    C.place(x=270,y=550)
    global p1_
    p1=pi.open(rootpath+"class5.jpg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""There are 250 class rooms in the school which are fully equipped with required furniture according to age group of the children. The fully ventilated class rooms provide a congenial environment for a purposeful life and future, on philosophy of "Child Centered" education aiming at growth of child's personality, body, mind and soul so as to make him a good citizen of the nation.\n""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1150)
    
    C2=Canvas(frame,width=700, height=600, bg='black') 
    C2.place(x=270,y=1550)
    global p2_
    p2=pi.open(rootpath+"class4.jpg")
    p2=p2.resize((700,600), pi.ANTIALIAS)
    p2_=pik.PhotoImage(p2) 
    C2.create_image(0,0, image=p2_, anchor=NW)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
def lab():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2300, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="LABORATORIES", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=300,y=100)
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='black') 
    C.place(x=270,y=550)
    global p1_
    p1=pi.open(rootpath+"lab3.jpg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""The School has Physics, Chemistry, Biology and Home Science well equipped Laboratories. The classes for practicals for respective subjects are regularly conducted in these laboratories.\n""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1150)
    
    C2=Canvas(frame,width=700, height=600, bg='black') 
    C2.place(x=270,y=1550)
    global p2_
    p2=pi.open(rootpath+"cs2.jpg")
    p2=p2.resize((700,600), pi.ANTIALIAS)
    p2_=pik.PhotoImage(p2) 
    C2.create_image(0,0, image=p2_, anchor=NW)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
def lib():
    print("yo")
def trans():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2300, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="TRANSPORT", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=300,y=100)
    
    #PHOTO:
    
    C=Canvas(frame,width=700, height=600, bg='black') 
    C.place(x=270,y=550)
    global p1_
    p1=pi.open(rootpath+"bus.jpg")
    p1=p1.resize((700,600), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    C.create_image(0,0, image=p1_, anchor=NW)
    
    #Text:
    
    ft=Font(family='times new roman', size=20)
    txt=Message(lc, text="""The School has 200 Buses and 100 Vans of Mercedes. The Buses are fully air conditioned with air bags in all the seats with parachute.\n""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=1150)
    
    C2=Canvas(frame,width=700, height=600, bg='black') 
    C2.place(x=270,y=1550)
    global p2_
    p2=pi.open(rootpath+"bus2.jpg")
    p2=p2.resize((700,600), pi.ANTIALIAS)
    p2_=pik.PhotoImage(p2) 
    C2.create_image(0,0, image=p2_, anchor=NW)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
def policy():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()

        
    #wall:
    wall=PhotoImage(file=rootpath+"wall2_2.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2100, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="TERMS & CONDITIONS", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=160,y=100)


    #Text:
    
    ft=Font(family='times new roman', size=18)
    txt=Message(lc, text="""Welcome to our website. If you continue to browse and use this website you are agreeing to comply with and be bound by the following terms and conditions of use, which govern Hogwards International School relationship with you in relation to this website.

The term 'Hogwards International School' or 'us' or 'we' refer to the owner of the website whose registered office is Hogwards International School, C-Block, California. The term 'you' refers to the user or viewer of our website.

The use of this website is subject to the following terms for use:

The content of the page(s) of this website is for your general information and use only. It is subject to change without notice.

Neither we nor any third party(s) provide any warranty or guarantee as to the accuracy, timeliness, performance, completeness or suitability of the information and materials found or offered on this website for any particular purpose. You acknowledge that such information and materials may contain inaccuracies or errors and we expressly exclude liability for any such inaccuracies or errors to the fullest extent permitted by law.

Your use of any information or materials on this website is entirely at your own risk, for which we shall not be liable. It shall be your own responsibility to ensure that any products, services or information available through this website meet your specific requirements.

This website contains material which is owned by or licensed to us. This material includes, but is not limited to, the design, layout, look, appearance and graphics. Reproduction is prohibited other than in accordance with the copyright notice, which forms part of these terms and conditions.

All trademarks reproduced in this website which are not the property of, or licensed to, the operator are acknowledged on the website.

Unauthorised use of this website may give rise to a claim for damages and/or be a criminal offence.

From time to time this website may also include links to other websites. These links are provided for your convenience to provide further information. They do not signify that we endorse the website(s). We have no responsibility for the content of the linked website(s).

You may not create a link to this website from another website or document without Hogwards International School prior written consent.

Your use of this website and any dispute arising out of such use of the website is subject to the law(s) of India or other regulatory authority.

We shall be under no liability whatsoever in respect of any loss or damage arising directly or indirectly out of the decline of authorization for any Transaction, on Account of the Cardholder having exceeded the present limit mutually agreed by us with our acquiring bank from time to time""", font=ft,width=900,bg='snow') 
    txt.place(x=50,y=400)
    
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)

    
def facil():
    print("yo") 
    
def gallery(event):
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()


    #wall:
    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)

    #canvas:
    lc=Canvas(frame, width=1000, height=2400, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,250, width=1, fill="snow" ) 
    
    #Label:
    fnt=Font(family='berlin sans fb', size=50)
    lb=Label(lc, text="GALLERY", font=fnt, bg='snow', fg="cornflower blue") 
    lb.place(x=300,y=100)
    
    
    
    def gall(event):
        global rt, n, n_
        rt=Toplevel() 
        rt.geometry("600x600")
        rt.title("GALLERY") 
        
        def nxt():
            global p_,n,n_,pict
            for i in range(0,len(extras)):
               try:
                   if(extras[i]==pict):
                       nxtimg=extras[i+1]
                       pict=nxtimg
                       break
               except:
                   nxtimg=extras[0]
                   pict=nxtimg
               
            p=pi.open(rootpath+""+nxtimg)
            p=p.resize((600,600), pi.ANTIALIAS)
            p_=pik.PhotoImage(p) 
            cf.create_image(0,0, image=p_, anchor=NW)
        
            n=PhotoImage(file=rootpath+"next.png")
            n=n.subsample(2,2)
            n_=n.subsample(-1,1)
            Button(rt,image=n, command=nxt).place(x=550,y=250)
            Button(rt,image=n_, command=prev).place(x=0,y=250)
         
        def prev():
            global p__,n,n_,pict
            for i in range(0,len(extras)):
                try:
                    if(extras[i]==pict):
                        preimg=extras[i-1]
                        pict=preimg
                        break
                except:
                    nxtimg=extras[-1]
                    pict=nxtimg
            
            p2=pi.open(rootpath+""+preimg)
            p2=p2.resize((600,600), pi.ANTIALIAS)
            p__=pik.PhotoImage(p2) 
            cf.create_image(0,0, image=p__, anchor=NW)
        
            n=PhotoImage(file=rootpath+"next.png")
            n=n.subsample(2,2)
            n_=n.subsample(-1,1)
            Button(rt,image=n, command=nxt).place(x=550,y=250)
            Button(rt,image=n_, command=prev).place(x=0,y=250)
         
        
        cf=Canvas(rt,width=600, height=600,bg='black') 
        cf.place(x=0,y=0)
        
        global p_,pict
        pict=event.widget.extra
        p=pi.open(rootpath+""+pict)
        p=p.resize((600,600), pi.ANTIALIAS)
        p_=pik.PhotoImage(p) 
        cf.create_image(0,0, image=p_, anchor=NW)
        
        n=PhotoImage(file=rootpath+"next.png")
        n=n.subsample(2,2)
        n_=n.subsample(-1,1)
        Button(rt,image=n, command=nxt).place(x=550,y=250)
        Button(rt,image=n_, command=prev).place(x=0,y=250)
        
        rt.mainloop() 

        
    #PHOTO:
    
    global p1_, p2_, p3_, p4_, p5_, p6_, p7_, p8_, p9_,p10_, p11_, p12_, p13_, extras
    extras=["trip.jpeg","trip2.jpg","trip3.jpeg","trip4.jpeg","trip5.jpeg","dance2.jpeg","func.jpg","func2.jpg","func3.jpg","award.jpeg","award2.jpeg","award3.jpeg","award4.jpeg"]
    
    
    cf=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf.place(x=50,y=500)
    p1=pi.open(rootpath+"trip.jpeg")
    p1=p1.resize((300,300), pi.ANTIALIAS)
    p1_=pik.PhotoImage(p1) 
    cf.create_image(0,0, image=p1_, anchor=NW)
    cf.extra=extras[0]
    cf.create_rectangle(0,0,300,300, width=10)
    cf.bind("<Button-1>",gall) 
    
    cf2=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf2.place(x=400,y=500)
    p2=pi.open(rootpath+"trip2.jpg")
    p2=p2.resize((300,300), pi.ANTIALIAS)
    p2_=pik.PhotoImage(p2) 
    cf2.create_image(0,0, image=p2_, anchor=NW)
    cf2.extra=extras[1]
    cf2.create_rectangle(0,0,300,300, width=10)
    cf2.bind("<Button-1>",gall) 
    
    cf3=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf3.place(x=750,y=500)
    p3=pi.open(rootpath+"trip3.jpeg")
    p3=p3.resize((300,300), pi.ANTIALIAS)
    p3_=pik.PhotoImage(p3) 
    cf3.create_image(0,0, image=p3_, anchor=NW)
    cf3.extra=extras[2]
    cf3.create_rectangle(0,0,300,300, width=10)
    cf3.bind("<Button-1>",gall) 
    
    cf4=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf4.place(x=50,y=850)
    p4=pi.open(rootpath+"trip4.jpeg")
    p4=p4.resize((300,300), pi.ANTIALIAS)
    p4_=pik.PhotoImage(p4) 
    cf4.create_image(0,0, image=p4_, anchor=NW)
    cf4.extra=extras[3]
    cf4.create_rectangle(0,0,300,300, width=10)
    cf4.bind("<Button-1>",gall) 
    
    cf5=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf5.place(x=400,y=850)
    p5=pi.open(rootpath+"trip5.jpeg")
    p5=p5.resize((300,300), pi.ANTIALIAS)
    p5_=pik.PhotoImage(p5) 
    cf5.create_image(0,0, image=p5_, anchor=NW)
    cf5.extra=extras[4]
    cf5.create_rectangle(0,0,300,300, width=10)
    cf5.bind("<Button-1>",gall) 
    
    cf6=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf6.place(x=750,y=850)
    p6=pi.open(rootpath+"dance2.jpeg")
    p6=p6.resize((300,300), pi.ANTIALIAS)
    p6_=pik.PhotoImage(p6) 
    cf6.create_image(0,0, image=p6_, anchor=NW)
    cf6.extra=extras[5]
    cf6.create_rectangle(0,0,300,300, width=10)
    cf6.bind("<Button-1>",gall) 
    
    cf7=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf7.place(x=50,y=1200)
    p7=pi.open(rootpath+"func.jpg")
    p7=p7.resize((300,300), pi.ANTIALIAS)
    p7_=pik.PhotoImage(p7) 
    cf7.create_image(0,0, image=p7_, anchor=NW)
    cf7.extra=extras[6]
    cf7.create_rectangle(0,0,300,300, width=10)
    cf7.bind("<Button-1>",gall) 
    
    cf8=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf8.place(x=400,y=1200)
    p8=pi.open(rootpath+"func2.jpg")
    p8=p8.resize((300,300), pi.ANTIALIAS)
    p8_=pik.PhotoImage(p8) 
    cf8.create_image(0,0, image=p8_, anchor=NW)
    cf8.extra=extras[7]
    cf8.create_rectangle(0,0,300,300, width=10)
    cf8.bind("<Button-1>",gall) 

    cf9=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf9.place(x=750,y=1200)
    p9=pi.open(rootpath+"func3.jpg")
    p9=p9.resize((300,300), pi.ANTIALIAS)
    p9_=pik.PhotoImage(p9) 
    cf9.create_image(0,0, image=p9_, anchor=NW)
    cf9.extra=extras[8]
    cf9.create_rectangle(0,0,300,300, width=10)
    cf9.bind("<Button-1>",gall) 
    
    cf10=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf10.place(x=50,y=1200)
    p10=pi.open(rootpath+"award.jpeg")
    p10=p10.resize((300,300), pi.ANTIALIAS)
    p10_=pik.PhotoImage(p10) 
    cf10.create_image(0,0, image=p10_, anchor=NW)
    cf10.extra=extras[9]
    cf10.create_rectangle(0,0,300,300, width=10)
    cf10.bind("<Button-1>",gall) 
    
    cf11=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf11.place(x=400,y=1200)
    p11=pi.open(rootpath+"award2.jpeg")
    p11=p11.resize((300,300), pi.ANTIALIAS)
    p11_=pik.PhotoImage(p11) 
    cf11.create_image(0,0, image=p11_, anchor=NW)
    cf11.extra=extras[10]
    cf11.create_rectangle(0,0,300,300, width=10)
    cf11.bind("<Button-1>",gall) 

    cf12=Canvas(frame,width=300, height=300,bg='cornflower blue') 
    cf12.place(x=750,y=1200)
    p12=pi.open(rootpath+"award3.jpeg")
    p12=p12.resize((300,300), pi.ANTIALIAS)
    p12_=pik.PhotoImage(p12) 
    cf12.create_image(0,0, image=p12_, anchor=NW)
    cf12.extra=extras[11]
    cf12.create_rectangle(0,0,300,300, width=10)
    cf12.bind("<Button-1>",gall) 
    #"award4.jpeg"
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
def sports(event):
    print("yo")
def activity(event):
    print("yo")



def col_():
    global colour,cs
    cho=cs.get()
    cc=colorchooser.askcolor(title="Select Colour") 
    colour=cc[1]
    print(colour)
    if(cho=="Top Canvas"):
        canvas.config(bg=colour)
        txt.config(bg=colour)
        txt2.config(bg=colour)
    elif(cho=="School Name"):
        txt.config(fg=colour)
    elif(cho=="School Info"):
        txt2.config(fg=colour)
    elif(cho=="App Info Canvas"):
        canvasf3.config(bg=colour)
    elif(cho=="Pages"):
        frame.config(bg=colour)
    
def col():
    global cs,f
    for wi in f.winfo_children():
        wi.destroy()
    
    list=["School Name","School Info","Top Canvas","App Info Canvas","Pages"] 
    entryfont=('verdana',7)
    font1=('verdana',10)
    cs=Combobox(f, values=list, font=entryfont) 
    cs.place(x=100,y=300)
    
    Label(f,text="Set Colour For:").place(x=100,y=200)
    Label(f,text="Colour Settings", font=font1).place(x=200,y=20)
    Button(f, text="Choose Colour", command=col_).place(x=100,y=400)
    
    
def setting(event):
    global root2,f
    root2=Toplevel() 
    root2.geometry("500x500")
    root2.title("SETTINGS") 
    f=Frame(root2,bg="#004ac6",width=500,height=500)
    f.place(x=0,y=0)
    Label(f, text="SETTINGS",bg="#004ac6", font=('britannic',30)).place(x=150,y=20)
    
    b1=Button(f, text="Change Colour",font=('arial rounded mt',20), command=col) 
    b1.place(x=100,y=200)
    
    
    root2.mainloop() 

def developer(event):
    global root3
    root3=Tk() 
    root3.geometry("800x600")
    root3.title("DEVELOPER MODE") 
    
    Label(root3, text="DEVELOPER MODE", font=('verdana',10)).pack()
    
    b1=Button(root3, text="SYSTEM INFO", command=sysfo) 
    b1.place(x=100,y=200)
    
    
    root3.mainloop() 
    
def sysfo():
    for wi in root3.winfo_children():
        wi.destroy()


    #import psutil
    #psutil.sensors_temperatures()


    def gpn():
        if platform.system() == "Windows":
            return platform.processor()
        elif platform.system() == "Darwin":
            command ="/usr/sbin/sysctl -n machdep.cpu.brand_string" 
            return os.popen(command).read().strip()
        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo"
            return os.popen(command).read().strip()
        return "Platform Not Identified"
     
    #ft=Font(family='times new roman', size=10)
    #txt=Message(frame, text=, font=ft) 
    #txt.place(x=200,y=800)
    
    Label(root3,text="System:"+platform.system()).place(x=100,y=200)
    Label(root3,text="Version:"+platform.version()).place(x=200,y=20)
    Label(root3,text="Platform:"+platform.platform()).place(x=100,y=300)
    Label(root3,text="Processor:"+gpn()).place(x=200,y=400)
    
        
def load():
    t.speed(5)
    t.penup()
    t.setpos(-1000,0)
    t.pendown()
    t.pensize(10)
    t.pencolor("#446dfb")
    t.forward(2000)
    t.setpos(-1000,0)

def backb():
    load() 
    t.clear()
    for wi in frame.winfo_children():
        wi.destroy()
    
    home() 
    
    
def loginb():
    load() 
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    
    
    
    #FRAME WALL:


    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
    #LOGIN CANVAS:
       
    
    lc=Canvas(frame, width=700, height=650,bd=0, bg="snow") 
    lc.place(x=270,y=200)
    lc.create_rectangle(0,0,700,175, width=0, fill="cornflower blue" )
    
    
    lfont=Font(family='arial rounded mt', size=35)
    loginlabel=Label(lc, text="Login", font=lfont,fg="white", bg='cornflower blue') 
    loginlabel.place(x=280,y=70)
    
    
    def sub():
        global p, i
        p=password.get()
        i=id_.get()
        
        if(p.isspace() or i.isspace() or p=="" or i==""):
            if(p.isspace() or p=="" ):
                password.config(background="red")
                messagebox.showerror("ERROR", "EMPTY PASSWORD!") 
            if(i.isspace() or i=="" ):
                id_.config(background="red")
                messagebox.showerror("ERROR", "EMPTY ID!") 
            
        else:
            id_.config(background="white")   
            password.config(background="white")
            try:
                crsr.execute("select ID,PASSWORD,CHOICE from people")
            except:
                messagebox.showerror("ERROR", "NO ACCOUNT EXIST! PLEASE SIGN IN FIRST.")
                return
            crsr.execute("select ID,PASSWORD,CHOICE from people") 
            output=crsr.fetchall()
            no=0
            for j in output:
                if(p==j[1] and i==j[0]):
                    if(j[2]=="student"):
                        log_s(i)
                    elif(j[2]=="parent"):
                        log_p(i)
                    elif(j[2]=="teacher"):
                        log_t(i)        
                    no=1
            if(no==0):
                id_.config(background="red")   
                password.config(background="red")
                messagebox.showerror("LOGIN ERROR", "WRONG ID AND PASSWORD!")

            
    #ENTRY BOX FOR ID:
        
    global id_
    entryfont=('comic sans ms',17)
    entrylabelfont=Font(family='arial rounded mt', size=25)
    id_=Entry(lc, font=entryfont,bd=3) 
    id_.place(x=290,y=275)
    il=Label(lc, text="LOGIN ID     :", bg='snow', font=entrylabelfont) 
    il.place(x=75,y=275)
    
    #ENTRY BOX FOR PASSWORD:
    
    global password 
    password=Entry(lc, font=entryfont, show='*', bd=3)
    password.place(x=290,y=375)
    passlabel=Label(lc, text="PASSWORD:", bg='snow', font=entrylabelfont) 
    passlabel.place(x=75,y=375)
    
    
    
    remember=Checkbutton(lc,text="Remember Me",font=('bahnschrift',15), bg='snow', activebackground='snow', selectcolor='snow') 
    remember.place(x=120,y=500)
    
    
    #SUBMIT BUTTON:
        
    simg=PhotoImage(file=rootpath+"submit1.png")
    simgphotoed=simg.subsample(1)  
      
    submit=Button(lc, image=simgphotoed, bg="white", activebackground='lightsteelblue1', command=sub) 
    submit.image=simgphotoed
    submit.place(x=350,y=550)
    

def log_s(i):
    load()
    t.clear()
    
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    

    crsr.execute("select * from people where ID="+"'"+i+"'") 
    output=crsr.fetchall()
    j=output[0]
    name=j[0]
    class_=j[1]
    gender=j[4]
    choice=j[5]
    age=j[6]
    name_child=j[7]
    tid=j[8]
         
         
    #ATTENDANCE:

    if attendance==[]:
        attend=[0,0]
    else:
        for i in attendance:
            if i[0]==name:
                attend=i[1]
            else:
                attend=[0,0]
    att=['Absent','Present']
    colour=("#ff7171","#40ff40")
    plt.pie(attend,labels=att,colors=colour,autopct="%1.1f%%")
    centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.axis('equal')
    pic=rootpath2+"'"+name+"'"+"_att.png"
    plt.savefig(pic) 
    
    
    def logimg(event):
        global rt, n_,n2_
        rt=Toplevel() 
        rt.geometry("650x650")
        rt.title(name) 
        
        def edit():
            f=filedialog.askopenfilename() 
            if f is None:
                messagebox.showerror("ERROR", "THE IMAGE WAS UNABLE TO OPEN!") 
                return 
            file=open(os.path.join(rootpath2,name+".txt"),'w') 
            file.write(f)
            file.flush()
            global photo_, p_
            photo=pi.open(f)
            photo=photo.resize((250,250), pi.ANTIALIAS)
            photo_=pik.PhotoImage(photo) 
            pc.create_image(50,50, image=photo_, anchor=NW)
            pc.create_oval(17,17,343,343, width=80, outline="cornflower blue")
            pc.create_oval(55,55,300,300, width=5)
     
            p=photo.resize((650,650), pi.ANTIALIAS)
            p_=pik.PhotoImage(p) 
            cf.create_image(0,0, image=p_, anchor=NW)
            file.close()
            
        def save():
            f=filedialog.asksaveasfile(mode="w",defaultextension=".jpg")
            #,defaultextension=".jpg"
            if f is None:
                messagebox.showerror("ERROR", "THE IMAGE WAS UNABLE TO SAVE!") 
                return 
            p__.save(f)
         
        
        cf=Canvas(rt,bg='black',width=650,height=650) 
        cf.place(x=0,y=0)
        
        global p_, p__
        file=open(os.path.join(rootpath2,name+".txt"),'r') 
        f=file.read()
        p__=pi.open(f)
        p=p__.resize((650,650), pi.ANTIALIAS)
        p_=pik.PhotoImage(p) 
        cf.create_image(0,0, image=p_, anchor=NW)
        
        n=PhotoImage(file=rootpath+"save.png")
        n_=n.subsample(2)
        n2=PhotoImage(file=rootpath+"addimg.png")
        n2_=n2.subsample(2)
        Button(rt,image=n_, command=save).place(x=600,y=10)
        Button(rt,image=n2_, command=edit).place(x=600,y=80)
        
        rt.mainloop() 
    
    
    #FRAME WALL:
        
        
    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)
    
    
    #INFO CANVAS:
        
    lc=Canvas(frame, width=1000, height=2400, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,350, width=1, fill="cornflower blue" )
    pc=Canvas(lc, width=1000, height=350, bg="cornflower blue") 
    pc.place(x=0,y=0)
    pc.bind("<Button-1>",logimg) 
    
    #NAME:
        
    lb=Label(lc, text=name, font=('berlin sans fb',50), bg='cornflower blue') 
    lb.place(x=445,y=130)
    Label(lc, text=class_, font=Font(family='berlin sans fb', size=35), bg='cornflower blue').place(x=450,y=220)
    

    #PHOTO:
    
    global photo_
    try:
        file=open(os.path.join(rootpath2,name+".txt"),'r') 
        f1=file.read()
        photo=pi.open(f1)
        x,y=0,0
    except:
        file=open(os.path.join(rootpath2,name+".txt"),'w+') 
        file.write(rootpath+"profile.png")
        file.flush()
        photo=pi.open(rootpath+"profile.png")
        x,y=20,10
    photo=photo.resize((250,250), pi.ANTIALIAS)
    photo_=pik.PhotoImage(photo) 
    pc.create_image(50+x,50+y, image=photo_, anchor=NW)
    
    pc.create_oval(17,17,343,343, width=80, outline="cornflower blue")
    pc.create_oval(55,55,300,300, width=5)
    
    
    Label(frame, text="Profile",font=Font(family='harlow solid', size=40), bg='snow').place(x=550,y=580)
    Label(frame, text="Academic Year" , font=Font(family='harlow solid', size=30), bg='snow').place(x=485,y=720)
    Label(frame, text="2019-2020",font=Font(family='harlow solid', size=20), bg='snow').place(x=550,y=830)
    Label(frame, text="Age" , font=Font(family='harlow solid', size=30), bg='snow').place(x=580,y=900)
    Label(frame, text=age,font=Font(family='harlow solid', size=20), bg='snow').place(x=595,y=1010)
    Label(frame, text="Gender" , font=Font(family='harlow solid', size=30), bg='snow').place(x=545,y=1080)
    Label(frame, text=gender,font=Font(family='harlow solid', size=20), bg='snow').place(x=575,y=1190)
    
    lc.create_rectangle(50,650,950,730, width=5)
    lc.create_rectangle(50,830,950,910, width=5)
    lc.create_rectangle(50,1010,950,1090, width=5)
    
      
    
    #ATTENDANCE:
    
    Label(frame, text="Attendance" , font=Font(family='harlow solid', size=30), bg='snow').place(x=520,y=1310)
    
    global attp_
    if attendance==[] or attend==[0,0]:
        Label(frame, text="No Attendance" , font=Font(family='harlow solid', size=20), bg='snow').place(x=500,y=1500)
    else:
        pic=rootpath2+"'"+name+"'"+"_att.png"
        attp=pi.open(pic) 
        attp=attp.resize((590,590), pi.ANTIALIAS)
        attp_=pik.PhotoImage(attp)  
        lc.create_image(205,1255, image=attp_, anchor=NW)
    lc.create_rectangle(200,1250,800,1850, width=5)
    
    #HOMEWORK:
    global homework,subjecthw
    Label(frame, text="Homework" , font=Font(family='harlow solid', size=30), bg='snow').place(x=525,y=2080)
    lc.create_rectangle(150,2010,850,2210, width=5)
    
    mess=""
    if homework==[]:
        mess="No Homework"
    else:
        for i in range(0,len(homework)):
            mess+=subjecthw[i]+" : "+homework[i]+"\n"
    #hmwrk=Message(lc,text=mess,font=Font(family='comic sans ms',size=20),width=730,bg="blue")
    hmwrk=Text(lc,font=Font(family='comic sans ms',size=20),width=43,height=5)
    hmwrk.insert(END,mess)
    hmwrk.place(x=155,y=2015)
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    file.close()
    
def log_p(i):
    load()
    t.clear()
    
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    

def log_t(i):
    load()
    t.clear()
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    
    
    crsr.execute("select * from people where ID="+"'"+i+"'") 
    output=crsr.fetchall()
    j=output[0]
    name=j[0]
    class_=j[1]
    gender=j[4]
    choice=j[5]
    age=j[6]
    name_child=j[7]
    tid=j[8]

    crsr.execute("select * from people where CHOICE='student' ") 
    output=crsr.fetchall()
    lst=[]
    for i in output:
        lst.append(i[0])
    
    
    def logimg(event):
        global rt, n_,n2_
        rt=Toplevel() 
        rt.geometry("650x650")
        rt.title(name) 
        
        def edit():
            f=filedialog.askopenfilename() 
            if f is None:
                messagebox.showerror("ERROR", "THE IMAGE WAS UNABLE TO OPEN!") 
                return 
            file=open(os.path.join(rootpath2,name+".txt"),'w') 
            file.write(f)
            file.flush()
            global photo_, p_
            photo=pi.open(f)
            photo=photo.resize((250,250), pi.ANTIALIAS)
            photo_=pik.PhotoImage(photo) 
            pc.create_image(50,50, image=photo_, anchor=NW)
            pc.create_oval(17,17,343,343, width=80, outline="cornflower blue")
            pc.create_oval(55,55,300,300, width=5)
     
            p=photo.resize((650,650), pi.ANTIALIAS)
            p_=pik.PhotoImage(p) 
            cf.create_image(0,0, image=p_, anchor=NW)
            file.close()
            
        def save():
            f=filedialog.asksaveasfile(mode="w",defaultextension=".jpg")
            #,defaultextension=".jpg"
            if f is None:
                messagebox.showerror("ERROR", "THE IMAGE WAS UNABLE TO SAVE!") 
                return 
            p__.save(f)
         
        
        cf=Canvas(rt,bg='black',width=650,height=650) 
        cf.place(x=0,y=0)
        
        global p_, p__
        file=open(os.path.join(rootpath2,name+".txt"),'r') 
        f=file.read()
        p__=pi.open(f)
        p=p__.resize((650,650), pi.ANTIALIAS)
        p_=pik.PhotoImage(p) 
        cf.create_image(0,0, image=p_, anchor=NW)
        
        n=PhotoImage(file=rootpath+"save.png")
        n_=n.subsample(2)
        n2=PhotoImage(file=rootpath+"addimg.png")
        n2_=n2.subsample(2)
        Button(rt,image=n_, command=save).place(x=600,y=10)
        Button(rt,image=n2_, command=edit).place(x=600,y=80)
        
        rt.mainloop() 
    
    
    #FRAME WALL:
        
        
    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)
    
    
    #INFO CANVAS:
        
    lc=Canvas(frame, width=1000, height=2100, bg="snow") 
    lc.place(x=125,y=150)
    lc.create_rectangle(0,0,1000,350, width=1, fill="cornflower blue" )
    pc=Canvas(lc, width=1000, height=350, bg="cornflower blue") 
    pc.place(x=0,y=0)
    pc.bind("<Button-1>",logimg) 
    
    #NAME:
        
    lb=Label(lc, text=name, font=('berlin sans fb',50), bg='cornflower blue') 
    lb.place(x=445,y=130)
    Label(lc, text=tid, font=Font(family='berlin sans fb', size=35), bg='cornflower blue').place(x=450,y=220)
    
    
    #PHOTO:
    global photo_
    try:
        file=open(os.path.join(rootpath2,name+".txt"),'r') 
        f1=file.read()
        photo=pi.open(f1)
        x,y=0,0
    except:
        file=open(os.path.join(rootpath2,name+".txt"),'w+') 
        file.write(rootpath+"profile.png")
        file.flush()
        photo=pi.open(rootpath+"profile.png")
        x,y=20,10
    photo=photo.resize((250,250), pi.ANTIALIAS)
    photo_=pik.PhotoImage(photo) 
    pc.create_image(50+x,50+y, image=photo_, anchor=NW)

    pc.create_oval(17,17,343,343, width=80, outline="cornflower blue")
    pc.create_oval(55,55,300,300, width=5)
    
    
    Label(frame, text="Profile",font=Font(family='harlow solid', size=40), bg='snow').place(x=550,y=580)
    Label(frame, text="Age" , font=Font(family='harlow solid', size=30), bg='snow').place(x=580,y=720)
    Label(frame, text=age,font=Font(family='harlow solid', size=20), bg='snow').place(x=595,y=830)
    Label(frame, text="Gender" , font=Font(family='harlow solid', size=30), bg='snow').place(x=545,y=900)
    Label(frame, text=gender,font=Font(family='harlow solid', size=20), bg='snow').place(x=575,y=1010)
    
    lc.create_rectangle(50,650,950,730, width=5)
    lc.create_rectangle(50,830,950,910, width=5)
    
      
    def subhome():
        global homework,subjecthw
        homework.append(hmwrk.get(1.0,END))
        print(homework)
        subjecthw.append(subjects.get())
        file=open(os.path.join(rootpath2,"homework.txt"),'a')
        top=len(homework)-1
        mess=subjecthw[top]+":"+homework[top]
        print(mess)
        file.write(mess)
        file.flush()
        file.close()
    def subfeed():
        global feedback,feedstud
        feedback.append(feed.get())
        feedstud.append(studnt.get())
        file=open(os.path.join(rootpath2,"communications.txt"),'a')
        top=len(feedback)-1
        mess=feedstud[top]+":"+feedback[top]
        file.write(mess)
        file.flush()
        file.close()
    def subatt():
        global attendance
        listt=[]
        listt.append(stud.get())
        print(type(atten.get()))
        listtt=[ str(100-int(atten.get())) , atten.get() ]
        listt.append(listtt)
        attendance.append(listt)
        file=open(os.path.join(rootpath2,"attendance.txt"),'a')
        for i in attendance:
            mess=i[0]+":"+i[1][0]+","+i[1][1]
            file.write(mess)
        file.flush()
        file.close()


    
    #ATTENDANCE:

    stud=Combobox(frame, values=lst, font=Font(family='comic sans ms',size=20)) 
    stud.place(x=550,y=1300)
    Label(frame, text="Choose Student :", bg='snow', font=Font(family='harlow solid', size=20)).place(x=330,y=1300)
    Label(frame, text="Attendance" , font=Font(family='harlow solid', size=30), bg='snow').place(x=525,y=1200)

    lc.create_rectangle(150,1140,850,1290, width=5)
    Label(frame, text="Select Attendance(%) :", bg='snow', font=Font(family='harlow solid', size=20)).place(x=330,y=1380)
    atten=Spinbox(frame, from_=0, to=100) 
    atten.place(x=620,y=1380)

    submit0=Button(frame,text="Submit",bg="snow",command=subatt)
    submit0.place(x=780,y=1380)
    
    #HOMEWORK:
    lst2=["Defence Against Dark Arts","Charms","Potions","Herbology","Astronomy","Flying"]
    subjects=Combobox(frame, values=lst2, font=Font(family='comic sans ms',size=20)) 
    subjects.place(x=550,y=1670)
    Label(frame, text="Choose Subject :", bg='snow', font=Font(family='harlow solid', size=20)).place(x=330,y=1670)
    Label(frame, text="Homework" , font=Font(family='harlow solid', size=30), bg='snow').place(x=525,y=1590)

    lc.create_rectangle(150,1500,850,1770, width=5)
    hmwrk=Text(lc,font=Font(family='comic sans ms',size=24),width=34,height=4)
    hmwrk.place(x=155,y=1575)

    submit=Button(frame,text="Send",bg="snow",command=subhome)
    submit.place(x=915,y=1680)


    #COMMUNICATIONS:
    '''
    studnt=Combobox(frame, values=lst, font=Font(family='comic sans ms',size=20)) 
    studnt.place(x=400,y=2100)
    Label(frame, text="Choose Student :", bg='snow', font=Font(family='harlow solid', size=20)).place(x=200,y=2100)
    Label(frame, text="Communications" , font=Font(family='harlow solid', size=30), bg='snow').place(x=525,y=1880)

    lc.create_rectangle(150,1210,850,2210, width=5)
    feed=Text(lc,font=Font(family='comic sans ms',size=25),width=35,height=4)
    feed.place(x=155,y=1915)

    submit2=Button(frame,text="Send",bg="snow",command=subfeed)
    submit2.place(x=550,y=2200)

    '''
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    file.close() 

def signinb():
    load()
    t.clear()
    
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    
   
    
    #FRAME WALL:
        
        
    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)
    
    def sub2():
        global a,b,c,d_
        a=id_.get()
        b=password.get()
        c=cpassword.get()
        d=choice.get()
        d_=d.lower()
        try:
            crsr.execute("select ID from people") 
            output=crsr.fetchall()
            if(a in output[0]):
                messagebox.showerror("ERROR", "ID ALREADY TAKEN!\nCHOOSE ANOTHER ID.") 
                id_.config(bg="red")
            elif(b!=c):
                messagebox.showerror("ERROR", "PASSWORD IS WRONG!\nENTER CORRECT PASSWORD.") 
                password.config(bg="red")
                cpassword.config(bg="red")
            elif("teacher" not in d_ and "student" not in d_ and "parent" not in d_):
                messagebox.showerror("ERROR", "INCORRECT CHOICE!") 
                style =ttk.Style()
                style.configure("BW.TLabel", background="red" )
                choice.configure(style="BW.TLabel")
            elif(a.isspace() or b.isspace() or c.isspace() or d.isspace() or a=="" or b=="" or c=="" or d==""):
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
                if(a.isspace() or a=="" ):
                    id_.config(background="red")
                if(b.isspace() or b=="" ):
                    password.config(background="red")
                if(c.isspace() or c=="" ):
                    cpassword.config(background="red")
                if(d.isspace() or d=="" ):
                    choice.config(background="red")
            
            else:
                password.config(bg="white")
                cpassword.config(bg="white")
                id_.config(bg="white")
                style =ttk.Style()
                style.configure("BW.TLabel", background="white" )
                choice.configure(style="BW.TLabel")
                signin_()
        except:
            if(b!=c):
                messagebox.showerror("ERROR", "PASSWORD IS WRONG!\nENTER CORRECT PASSWORD.") 
                password.config(bg="red")
                cpassword.config(bg="red")
            elif("teacher" not in d_ and "student" not in d_ and "parent" not in d_):
                messagebox.showerror("ERROR", "INCORRECT CHOICE!") 
                style =ttk.Style()
                style.configure("BW.TLabel", background="red" )
                choice.configure(style="BW.TLabel")
            
            elif(a.isspace() or b.isspace() or c.isspace() or d.isspace() or a=="" or b=="" or c=="" or d==""):
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
                if(a.isspace() or a=="" ):
                    id_.config(background="red")
                if(b.isspace() or b=="" ):
                    password.config(background="red")
                if(c.isspace() or c=="" ):
                    cpassword.config(background="red")
                if(d.isspace() or d=="" ):
                    choice.config(background="red")
            
            else:
                password.config(bg="white")
                cpassword.config(bg="white")
                id_.config(bg="white")
                style =ttk.Style()
                style.configure("BW.TLabel", background="white" )
                choice.configure(style="BW.TLabel")
                signin_()
   
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    
    
    #SIGN IN CANVAS:
    lc=Canvas(frame, width=800, height=1050,bd=0, bg="snow") 
    lc.place(x=220,y=200)
    lc.create_rectangle(0,0,800,175, width=0, fill="cornflower blue" )
    
    
    lfont=Font(family='arial rounded mt', size=35)
    loginlabel=Label(lc, text="SIGN IN", font=lfont,fg="white", bg='cornflower blue') 
    loginlabel.place(x=310,y=70)
    

    #ENTRY BOX FOR SIGN IN AS:
        
    entryfont=('comic sans ms',17)
    entrylabelfont=Font(family='arial rounded mt', size=18)
    list1=["TEACHER","STUDENT"] 
    choice=Combobox(lc, values=list1, font=entryfont) 
    choice.place(x=400,y=275)
    clabel=Label(lc, text="SIGN IN AS:", bg='snow', font=entrylabelfont) 
    clabel.place(x=125,y=275)
    
    
    #ENTRY BOX FOR ID:
    
    id_=Entry(lc, font=entryfont, bd=3) 
    id_.place(x=440,y=415)
    il=Label(lc, text="CREATE YOUR ID:", bg='snow', font=entrylabelfont) 
    il.place(x=65,y=415)
    
    #ENTRY BOX FOR PASSWORD:
    
    password=Entry(lc, font=entryfont, bd=3)
    password.place(x=440,y=555)
    passlabel=Label(lc, text="CREATE YOUR PASSWORD:", bg='snow', font=entrylabelfont) 
    passlabel.place(x=65,y=555)
    
    #ENTRY BOX FOR CONFIRM PASSWORD:
        
    cpassword=Entry(lc, font=entryfont, bd=3)
    cpassword.place(x=440,y=695)
    cpasslabel=Label(lc, text="CONFIRM YOUR PASSWORD:", bg='snow', font=entrylabelfont) 
    cpasslabel.place(x=65,y=695)
    
    robot=Checkbutton(lc,text="I AM NOT A ROBOT", bg='snow',activebackground='snow', selectcolor='snow') 
    robot.place(x=200,y=850)
    
    
    #SUBMIT BUTTON:
        
    simg=PhotoImage(file=rootpath+"submit1.png")
    simgphotoed=simg.subsample(1)
      
    submit=Button(lc, image=simgphotoed, bg="white", activebackground='lightsteelblue1', command=sub2) 
    submit.image=simgphotoed
    submit.place(x=350,y=920)
    
def signin_():
    #CLEARING FRAME:
        
    for wi in frame.winfo_children():
        wi.destroy()
    
    
    #FRAME WALL:
        
        
    wall=PhotoImage(file=rootpath+"wall3.png")    
    wall_=wall.zoom(2)
    
    
    wlabel=Label(frame, image=wall_) 
    wlabel.image=wall_
    wlabel.place(x=0,y=0)
    
    wlabel2=Label(frame, image=wall_) 
    wlabel2.image=wall_
    wlabel2.place(x=0,y=1400)
    
    def sub3():
        
        a_=name.get()
        b_=age.get()
        if(i.get()==1):
            g="Male"
        else:
            g="Female" 
        rr=0
        if(d_=="student"):
            c_=class_.get()
            e_="None" 
            f="None" 
            if(c_.isspace() or c_=="" ):
                style =ttk.Style()
                style.configure("BW.TLabel", background="red" )
                class_.configure(style="BW.TLabel")
                rr=1
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
        elif(d_=="parent"):
            c_=class_.get()
            e_=name_.get()
            f="None"
            if(c_.isspace() or c_=="" ):
                style =ttk.Style()
                style.configure("BW.TLabel", background="red" )
                class_.configure(style="BW.TLabel")
                rr=1
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
            if(e_.isspace() or e_=="" ):
                name_.config(background="red")
                if(rr==0):
                    messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
                rr=1
        elif(d_=="teacher"):
            f=tid.get()
            c_="None" 
            e_="None" 
            if(f.isspace() or f=="" ):
                tid.config(background="red")    
                rr=1
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
        
        if(a_.isspace() or a_=="" ):
            name.config(background="red")
            if(rr==0):
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
            rr=1
        if(b_.isspace() or b_=="" ):
            age.config(background="red")
            if(rr==0):
                messagebox.showerror("ERROR", "FILL ALL THE CREDENTIALS!") 
        
        else:
            y="," 
            x="'" 
            try:
                crsr.execute("CREATE TABLE PEOPLE(NAME VARCHAR(50) NOT NULL, CLASS VARCHAR(10), ID VARCHAR(50) NOT NULL UNIQUE, PASSWORD VARCHAR(25) NOT NULL, GENDER CHAR(1) NOT NULL,CHOICE CHAR(1) NOT NULL, AGE INTEGER, NAMECHILD VARCHAR(50), TEACHERID VARCHAR(30))") 
            except:
                pass
            crsr.execute("insert into people values("+x+a_+x+y+x+c_+x+y+x+a+x+y+x+b+x+y+x+g+x+y+x+d_+x+y+x+b_+x+y+x+e_+x+y+x+f+x+")") 
            crsr.execute("select * from people") 
            output=crsr.fetchall()
            connection.commit()
            if(d_=="student"):
                log_s(a) 
            elif(d_=="teacher"):
                log_t(a)
            elif(d_=="parent"):
                log_p(a)   
        
    
    #BACK BUTTON:
        
    bimg=PhotoImage(file=rootpath+"back2.png")
    bimg=bimg.subsample(2)
    back=Button(frame, text="BACK", image=bimg, command=backb, bg="antiquewhite2")
    back.image=bimg
    back.place(x=50,y=50)
    

    #SIGN IN NEXT CANVAS:
    
    lc=Canvas(frame, width=800, height=950,bd=0, bg="snow") 
    lc.place(x=220,y=200)
    lc.create_rectangle(0,0,800,175, width=0, fill="cornflower blue" )
    
    
    lfont=Font(family='arial rounded mt', size=35)
    loginlabel=Label(lc, text="SIGN IN", font=lfont,fg="white", bg='cornflower blue') 
    loginlabel.place(x=330,y=70)
    
    #ENTRY BOX FOR NAME:
      
    entryfont=('comic sans ms',17)
    entrylabelfont=Font(family='arial rounded mt', size=18)   
    name=Entry(lc, font=entryfont, bd=3) 
    name.place(x=440,y=275)
    nl=Label(lc, text="ENTER YOUR FULL NAME:", bg='snow', font=entrylabelfont) 
    nl.place(x=75,y=275)
    
    
    #ENTRY BOX FOR AGE:
        
    age=Spinbox(lc, from_=3, to=50) 
    age.place(x=440,y=415)
    al=Label(lc, text="SELECT YOUR AGE:", bg='snow', font=entrylabelfont) 
    al.place(x=75,y=415)
    
    #ENTRY BOX FOR T/S/P:
      
    if(d_=="student"):
        list1=["PRE-NURSERY","NURSERY","MONT.1","MONT.2","I-A","I-B","II-A","II-B","III-A","III-B","IV-A","IV-B","V-A","V-B","VI-A","VI-B","VII-A","VII-B","VIII-A","VIII-B","IX-A","IX-B","X-A","X-B","XI-A","XI-B","XII-A","XII-B"] 
        class_=Combobox(lc, values=list1, font=entryfont) 
        class_.place(x=440,y=555)
        clabel=Label(lc, text="SELECT YOUR CLASS:", bg='snow', font=entrylabelfont) 
        clabel.place(x=75,y=555)
    
    elif(d_=="teacher"):
        tid=Entry(lc, font=entryfont, bd=3)
        tid.place(x=440,y=555)
        tlabel=Label(lc, text="ENTER TEACHER ID:", bg='snow', font=entrylabelfont) 
        tlabel.place(x=75,y=555)    
    '''
    elif(d_=="parent"):
        name_=Entry(frame, font=entryfont, bd=10, bg='white')
        name_.place(x=450,y=990)
        nlabel=Label(frame, text="ENTER YOUR CHILD'S NAME:", bg='snow', font=entrylabelfont) 
        nlabel.place(x=450,y=890)
        
        list1=["PRE-NURSERY","NURSERY","MONT.1","MONT.2","I-A","I-B","II-A","II-B","III-A","III-B","IV-A","IV-B","V-A","V-B","VI-A","VI-B","VII-A","VII-B","VIII-A","VIII-B","IX-A","IX-B","X-A","X-B","XI-A","XI-B","XII-A","XII-B"] 
        class_=Combobox(frame, values=list1, font=entryfont) 
        class_.place(x=450,y=1240)
        clabel=Label(frame, text="SELECT YOUR CHILD'S CLASS:", bg='snow', font=entrylabelfont) 
        clabel.place(x=450,y=1140)
    ''' 
        
    i=IntVar()  
    gen=Radiobutton(lc, text="Male",bg="snow",activebackground='snow', variable=i, value=1)
    gen2=Radiobutton(lc, text="Female",bg="snow",activebackground='snow', variable=i, value=2)
    gen.place(x=200,y=740)
    gen2.place(x=300,y=740)
    
    
    #SUBMIT BUTTON:
        
    simg=PhotoImage(file=rootpath+"submit1.png")
    simgphotoed=simg.subsample(1)  
      
    submit=Button(lc, image=simgphotoed, bg="white", command=sub3) 
    submit.image=simgphotoed
    submit.place(x=350,y=800) 

def search_():
    a=search.get()
    if(a=="Management"):
        manage()
    elif(a=="Principal"):
        principal()
    elif(a=="Faculty"):
        faculty()
    elif(a=="ISA Certification"):
        isa()
    elif(a=="Admission 2019"):
        adm2019()
    elif(a=="Registration 2019"):
        reg2019()
    elif(a=="Class Rooms"):
        classroom()
    elif(a=="Laboratories"):
        lab()
    elif(a=="Transport"):
        trans()
    elif(a=="Policy"):
        policy()
     

def home():
    backg=Canvas(frame,width=1280, height=2650,bg='lavender') 
    backg.place(x=0,y=0)
    backg.create_image(0,0, image=pht_, anchor=NW)
    backg.create_image(0,700, image=pht_, anchor=NW)
    backg.create_image(0,1400, image=pht_, anchor=NW)
    backg.create_image(0,2100, image=pht_, anchor=NW)

    #canvas:
    global lcpho_
    lc=Canvas(frame, width=985, height=1105,bd=4, bg="black")
    lc.place(x=0,y=0)
    lcpho=pi.open(rootpath+"wall01.jpg")
    lcpho=lcpho.resize((985,1105), pi.ANTIALIAS)
    lcpho_=pik.PhotoImage(lcpho) 
    lc.create_image(0,0, image=lcpho_, anchor=NW) 
    
    
    global ph1_, ph2_, ph3_, ph4_,ph5_,ph6_
    ft=("comic sans ms",30)
    ft2=("comic sans ms",16)
    #
    cf=Canvas(frame,width=350, height=350,bg='cornflower blue') 
    cf.place(x=70,y=150)
    ph1=pi.open(rootpath+"activity2.jpeg")
    p1=ph1.resize((350,275), pi.ANTIALIAS)
    ph1_=pik.PhotoImage(p1) 
    cf.create_image(0,0, image=ph1_, anchor=NW)
    cf.create_rectangle(0,0,350,350, width=10)
    cf.create_rectangle(5,275,345,345,fill='cornflower blue')
    cf.bind("<Button-1>",activity) 
    label1=Label(cf, text="ACTIVITIES",font=ft ,bg="cornflower blue" ) 
    label1.place(x=50,y=275)
    #

    #
    cf2=Canvas(frame,width=350, height=350,bg='cornflower blue') 
    cf2.place(x=565,y=150)
    ph2=pi.open(rootpath+"sports.jpg")
    p2=ph2.resize((350,275), pi.ANTIALIAS)
    ph2_=pik.PhotoImage(p2) 
    cf2.create_image(0,0, image=ph2_, anchor=NW)
    label2=Label(cf2, text="       SPORTS       ",font=ft , bg="cornflower blue" ) 
    label2.place(x=5,y=275)
    cf2.create_rectangle(0,0,350,350, width=10)
    cf.create_rectangle(5,275,345,345,fill='cornflower blue')
    #cf.create_line(340,245,345,345,fill='cornflower blue')
    cf2.bind("<Button-1>",sports) 
    #

    #
    cf3=Canvas(frame,width=350, height=350,bg='cornflower blue') 
    cf3.place(x=70,y=650)
    ph3=pi.open(rootpath+"calendar.jpg")
    p3=ph3.resize((350,275), pi.ANTIALIAS)
    ph3_=pik.PhotoImage(p3) 
    cf3.create_image(0,0, image=ph3_, anchor=NW)
    label3=Label(cf3, text="     CALENDAR    ",font=ft , bg="cornflower blue" ) 
    label3.place(x=5,y=275)
    cf3.create_rectangle(0,0,350,350, width=10)
    cf.create_rectangle(5,275,345,345,fill='cornflower blue')
    cf3.bind("<Button-1>",calendar)
    #

    #
    cf4=Canvas(frame,width=350, height=350,bg='cornflower blue') 
    cf4.place(x=565,y=650)
    ph4=pi.open(rootpath+"gallery.jpg")
    p4=ph4.resize((350,275), pi.ANTIALIAS)
    ph4_=pik.PhotoImage(p4) 
    cf4.create_image(0,0, image=ph4_, anchor=NW)
    label4=Label(cf4, text="       GALLERY      ",font=ft , bg="cornflower blue" ) 
    label4.place(x=5,y=275)
    cf4.create_rectangle(0,0,350,350, width=10)
    cf.create_rectangle(5,275,345,345,fill='cornflower blue')
    cf4.bind("<Button-1>",gallery)
    #

    #
    cf5=Canvas(frame,width=1280, height=960,bg='cornflower blue',bd=0) 
    cf5.place(x=0,y=1106)
    ph5=pi.open(rootpath+"educationquote2.gif")
    p5=ph5.resize((1280,960), pi.ANTIALIAS)
    ph5_=pik.PhotoImage(p5) 
    cf5.create_image(0,0, image=ph5_, anchor=NW)
    #
    cf6=Canvas(frame,width=500, height=600,bg='cornflower blue',bd=0) 
    cf6.place(x=780,y=2067)
    ph6=pi.open(rootpath+"quote.jpg")
    p6=ph6.resize((500,600), pi.ANTIALIAS)
    ph6_=pik.PhotoImage(p6) 
    cf6.create_image(0,0, image=ph6_, anchor=NW)
    '''
    frames=[PhotoImage(file=rootpath+"educationquote2.gif",format = 'gif -index %i' %(i)) for i in range(100)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        label.configure(image=frame)
        root.after(100, update, ind)
        root.update_idletasks()
    label = Label(frame)
    label.place(x=600,y=800)
    root.update_idletasks()
    root.after(1000, update, 0)
    '''
    
    global gif_turn
    gif_turn=0
    
    #gif()
    
    #LOGIN/SIGN IN (CANVAS 4):
    
    """
    canvasf4=Canvas(frame,width=450, height=1695, bg='lemon chiffon') 
    canvasf4.place(x=1500,y=0)
    canvasf4.create_rectangle(0,0,480,1695,width=10)
    """
    global logimg_
    logimg=pi.open(rootpath+"login1.png")
    logimg=logimg.resize((50,30), pi.ANTIALIAS)
    logimg_=pik.PhotoImage(logimg) 

    login=Button(frame,text="  LOGIN        ",font=ft2 , relief=GROOVE, bd=0, command=loginb, activebackground="dodger blue", fg="white", bg="cornflower blue", highlightcolor="red") 
    login.place(x=1070,y=240)

    signin=Button(frame,text=" SIGN IN      ",font=ft2 , relief=GROOVE, bd=0, command=signinb, activebackground="dodger blue", fg="white", bg="cornflower blue") 
    signin.place(x=1070,y=370)
    
    admission=Button(frame,text=" ADMISSION    ",font=ft2 , relief=GROOVE, bd=0, command=adm2019, activebackground="dodger blue", fg="white", bg="cornflower blue") 
    admission.place(x=1070,y=500)

    gallery_=Button(frame,text=" FACULTY     ",font=ft2 , relief=GROOVE, bd=0, command=faculty, activebackground="dodger blue", fg="white", bg="cornflower blue") 
    gallery_.place(x=1070,y=630)


#CLOCK:

def clock():
    tym=time.ctime() 
    timefont=Font(family='broadway', size=4)   
    #tim=canvas.create_text(100,-100,text=tym, font=timefont)
    tim=Label(canvas, text=tym, font=timefont, bg='lavender') 
    tim.place(x=1600,y=10)
    tim.after(1000,clock)

def gif():
    global gif_turn, gif_
    gif_turn+=1
    #+str(gif_turn)
    gifimg=PhotoImage(file=rootpath+"educationquote2.gif",format = 'gif -index '+str(gif_turn))
    #gifimg=PhotoImage(file=rootpath+"educationquote2.gif")
    #root.update_idletasks()
    gif_=gifimg.subsample(1)
    canvasframe5=Canvas(frame,width=450, height=350) 
    canvasframe5.place(x=400,y=1050)
    canvasframe5.create_image(0,0, image=gif_, anchor=NW)
    canvasframe5.after(1000,gif)
    
#SASHA:
    
def sasha(event):
    import SASHA_AI
def tictactoe(event):
    import TIC_TAC_TOE

    
#SHORTCUTS:

root.bind('<Control-s>',setting)
root.bind('<Control-d>',developer)
root.bind('<Shift-Up>',sasha)
root.bind('<Control-t>',tictactoe)



#START PROGRAM:


#SCROLLBAR:

scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)


#INITIAL CANVAS:

loadc=Canvas(root, width=1280, height=3,bg="white")
loadc.pack(side=TOP)


fcanvas=Canvas(root, width=1280, height=3500, yscrollcommand=scroll.set)
fcanvas.pack()

def configure(event):
    fcanvas.configure(scrollregion=fcanvas.bbox('all'))
    
scroll.config(command=fcanvas.yview)

fcanvas.bind('<Configure>', configure)


#FRAME ON CANVAS:

fframe=Frame(fcanvas, width=1280, height=3500)
fcanvas.create_window((0,0), window= fframe, anchor=NW)
#fcanvas.create_rectangle(0,0,1280,2500,width=15)



frame=Frame(fframe, width=1280, height=2650)
frame.place(x=0,y=350)


pht=pi.open(rootpath+"wall4.jpg")
pht=pht.resize((1280,700), pi.ANTIALIAS)
#pht=pht.rotate(90)
pht_=pik.PhotoImage(pht) 

backg=Canvas(frame,width=1280, height=2650,bg='lavender') 
backg.place(x=0,y=0)
backg.create_image(0,0, image=pht_, anchor=NW)
backg.create_image(0,700, image=pht_, anchor=NW)


''' SCHOOL LOGO (CANVAS 1): '''


#APPLICATION INFO (CANVAS 3):

afont=Font(family='agency fb', size=25)
afont2=Font(family='bahnschrift', size=20)
afont3=Font(family='bahnschrift', size=10)
canvasf3=Canvas(fframe,width=1280, height=450, bg='grey') 
canvasf3.place(x=0,y=3000)
canvasf3.create_rectangle(0,0,1280,100, width=1, fill="steelblue" )
canvasf3.create_rectangle(0,100,1280,350, width=1, fill="cornflower blue" )
canvasf3.create_rectangle(0,350,1280,450, width=1, fill="grey" )
Label(canvasf3, text="LOCATION",font=afont2, bg="cornflower blue" ).place(x=100,y=150)
Label(canvasf3, text="CONTACTS",font=afont2, bg="cornflower blue" ).place(x=500,y=150)
Label(canvasf3, text="LATEST NEWS",font=afont2, bg="cornflower blue" ).place(x=900,y=150)
Label(canvasf3, text="You Are Visitor Number "+saved,font=afont, bg="steelblue" ).place(x=150,y=40)
Label(canvasf3, text="Groove Street , California , USA",font=afont3, bg="cornflower blue" ).place(x=100,y=210)
Label(canvasf3, text="E-mail : hogwardschool@gmail.com\nContact : +55 6256256250",font=afont3, bg="cornflower blue" ).place(x=500,y=210)
Label(canvasf3, text="School Camp 2019\nPre-Boards 2019\nSchool Trip to France",font=afont3, bg="cornflower blue" ).place(x=900,y=210)
Label(canvasf3, text="All Rights Reserved © Hogwards International School   |   Powered By SARC INDUSTRIES",font=afont2,fg="white", bg="grey" ).place(x=100,y=400)

picture=pi.open(rootpath+"gmail.png")
picture=picture.resize((30,30), pi.ANTIALIAS)
picture_=pik.PhotoImage(picture) 
canvasf3.create_image(900,300, image=picture_, anchor=NW)
picture2=pi.open(rootpath+"insta3.jpg")
picture2=picture2.resize((30,30), pi.ANTIALIAS)
picture2_=pik.PhotoImage(picture2) 
canvasf3.create_image(1000,300, image=picture2_, anchor=NW)
picture3=pi.open(rootpath+"youtube.jpg")
picture3=picture3.resize((30,30), pi.ANTIALIAS)
picture3_=pik.PhotoImage(picture3) 
canvasf3.create_image(1100,300, image=picture3_, anchor=NW) 

canvas=Canvas(fframe,width=1280, height=150,bg='#800000') 
canvas.place(x=0,y=0)
t=RawTurtle(loadc) 
t.ht()
clock() 

#SCHOOL LABEL:
   


#schoolfont=Font(family='broadway', size=15)
schoolfont=Font(family='broadway', size=40)

#schoolfont2=Font(family='broadway', size=7)
schoolfont2=Font(family='broadway', size=15)

txt=Label(canvas, text="HOGWARDS INTERNATIONAL SCHOOL", font=schoolfont, bg='#800000' , fg="midnightblue" )
txt.place(x=155,y=30)

txt2=Label(canvas, text="CBSE AFFILIATED", font=schoolfont2, bg='#800000', fg="red" )
txt2.place(x=350,y=110)


#SCHOOL LOGO:


photo=PhotoImage(file=rootpath+"logo.png")
photoed=photo.subsample(20)
#canvas.create_image(-960,-135, image=photoed, anchor=NW) 
canvas.create_image(10,10, image=photoed, anchor=NW) 

#SERACH BAR:

largefont=('comic sans ms',10)
#largefont=('verdana',20)
list=["Management","Principal","Faculty","ISA Certification","Admission 2019","Registration 2019","Class Rooms","Laboratories","Transport","Policy"]
search=Combobox(canvas, values=list, width=40, font=largefont)
search.place(x=860,y=110)


img=pi.open(rootpath+"search.png")
img=img.resize((20,20), pi.ANTIALIAS)
img=pik.PhotoImage(img)
b=Button(canvas, image=img, command=search_, bg="white") 
b.place(x=1203,y=108)


    
''' SCHOOL IMAGES (CANVAS 2): '''



canvas2=Canvas(fframe,width=1280, height=200,bd=0) 
canvas2.place(x=0,y=150)
    
canvas2.bind('<Button-1>',gallery)

    
photo2=pi.open(rootpath+"pupil2.jpg")
p1=photo2.resize((220,200), pi.ANTIALIAS)
photo2_=pik.PhotoImage(p1) 
canvas2.create_image(0,0, image=photo2_, anchor=NW)


photo3=pi.open(rootpath+"lab.jpeg")
p2=photo3.resize((220,200), pi.ANTIALIAS)
photo3_=pik.PhotoImage(p2) 
canvas2.create_image(220,0, image=photo3_, anchor=NW)


photo4=pi.open(rootpath+"build3.jpg")
p3=photo4.resize((220,200), pi.ANTIALIAS)
photo4_=pik.PhotoImage(p3) 
canvas2.create_image(440,0, image=photo4_, anchor=NW)


photo5=pi.open(rootpath+"sports2.jpg")
p4=photo5.resize((220,200), pi.ANTIALIAS)
photo5_=pik.PhotoImage(p4) 
canvas2.create_image(660,0, image=photo5_, anchor=NW)


photo6=pi.open(rootpath+"pool.jpeg")
p5=photo6.resize((200,200), pi.ANTIALIAS)
photo6_=pik.PhotoImage(p5) 
canvas2.create_image(860,0, image=photo6_, anchor=NW)


photo7=pi.open(rootpath+"cs.jpg")
p6=photo7.resize((205,200), pi.ANTIALIAS)
photo7_=pik.PhotoImage(p6) 
canvas2.create_image(1060,0, image=photo7_, anchor=NW)

canvas2.create_rectangle(0,0,1280,200,width=2)



''' MENU: '''



top_menu=Menu(root) 
root.config(menu=top_menu)


#MENU ITEMS:
               
home_menu=Menu(top_menu) 
top_menu.add_cascade(label="HOME", menu=home_menu, background="gray") 

about_menu=Menu(top_menu) 
top_menu.add_cascade(label="ABOUT US", menu=about_menu, background="gray") 

adm_menu=Menu(top_menu) 
top_menu.add_cascade(label="ADMISSION", menu=adm_menu, background="gray") 
'''
acad_menu=Menu(top_menu) 
top_menu.add_cascade(label="ACADEMICS", menu=acad_menu, background="gray") 
'''
fac_menu=Menu(top_menu) 
top_menu.add_cascade(label="FACILITIES", menu=fac_menu, background="gray") 

pol_menu=Menu(top_menu) 
top_menu.add_cascade(label="OUR POLICIES", menu=pol_menu, background="gray") 


home_menu.add_command(label="Home", command=backb) 


        
#ABOUT MENU:
about_menu.add_command(label="Management", command=manage) 
about_menu.add_command(label="Principal", command=principal) 
about_menu.add_command(label="Faculty", command=faculty) 
about_menu.add_command(label="ISA Certification", command=isa) 

#ADMISSION MENU:
adm_menu.add_command(label="Policy", command=policy) 
adm_menu.add_command(label="Admission 2019", command=adm2019) 
adm_menu.add_command(label="Registration 2019", command=reg2019) 
'''
#ACADEMICS MENU:
acad_menu.add_command(label="Academic Programs", command=acad) 
acad_menu.add_command(label="Exam Schedules", command=exam) 
acad_menu.add_command(label="Result", command=result) 
acad_menu.add_command(label="Rules & Regulations", command=rules) 
'''
#FACILITIES MENU:
fac_menu.add_command(label="Class Rooms", command=classroom) 
fac_menu.add_command(label="Laboratories", command=lab) 
#fac_menu.add_command(label="Library", command=lib) 
fac_menu.add_command(label="Transport", command=trans)

#POLICY MENU:
pol_menu.add_command(label="Terms & Conditions", command=policy)




home() 


root.mainloop()


''' ROOT END: '''
time.sleep(4)
print("THANK YOU FOR VISITING OUR PROJECT\n.\n.")
time.sleep(2)
print("MADE BY SHRAVAN & ANSH\n.\n.")
time.sleep(2)
print("HAIL SARC\n")
time.sleep(5)
