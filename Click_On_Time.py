import pyautogui as automouse
import time

from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import font
from pynput import mouse 

root = Tk() 				# create object
root.title("Click_on_time")				#set Title
root.geometry("250x400") 	#set Size
root.resizable(0,0)

text_var=StringVar()

########################################

#targetX set
targetX = ttk.Label(root, text = "Target X:").place(x = 40, y = 25)	
targetXdp = ttk.Label(root, text="")
targetXdp.place(x=90, y=25)
#targetY set
targetY = ttk.Label(root, text = "Target Y:").place(x = 120, y = 25) 
targetYdp = ttk.Label(root, text="")
targetYdp.place(x=170, y=25)

#place hour label and Entry for input
hour = ttk.Label(root, text = "hour").place(x = 30,y = 100) 
entry3 = ttk.Entry(root,width=10)
entry3.place(x = 90,y = 100)
entry3.insert("0",time.localtime(time.time()).tm_hour)


#place minute label and Entry for input 
minute = ttk.Label(root, text = "minute").place(x = 30, y = 140)  
entry4 = ttk.Entry(root,width=10)
entry4.place(x = 90,y = 140)
entry4.insert("0",time.localtime(time.time()).tm_min)


#place sec label and Entry for input   
sec = ttk.Label(root, text = "sec").place(x = 30, y = 180)  
entry5 = ttk.Entry(root,width=10)	#place나 pack을하면 null을 반환하여 null obj가됨 주의
entry5.place(x = 90,y = 180)
entry5.insert("0",time.localtime(time.time()).tm_sec)

#place tidesc to display left time to execute
timedesc = ttk.Label(root, text="Left time:").place(x=50,y=210)
timedescdp = ttk.Label(root, text="")
timedescdp.place(x=110,y=210)


#place buttons and set clickevent
button1 = ttk.Button(root, text="Click Target Point!",  
				command = lambda:buttonClicked())
button1.place(x=70,y=50)

button2 = ttk.Button(root, text="Launch!!",
		 command = lambda:buttonClicked2())
button2.place(x=80,y=230)

#description
desc = Label(root, text = "1.Click \"Click Target!\" button\n"+
	"2.Put Hour,Minute,Second of the time\n that you want the program\n"+
	"to click the target\n"+
	"3.Click \"Launch!!\" button").place(x =20, y = 260) 

copyrightfont =font.Font(size=8)
copyright = ttk.Label(root, text = "Copyright 2020, MINJUN PARK, All rights reserved. "
			,font=copyrightfont).place(x=2,y=360)



########################################  
global currentHour
global currentMin
global leftSec



def buttonClicked2():
	if x1:
		global hour
		global minute
		hour=int(entry3.get())
		minute=int(entry4.get())
		sec=int(entry5.get())
		currentHour=time.localtime(time.time()).tm_hour
		currentMin=time.localtime(time.time()).tm_min
		currentsec=time.localtime(time.time()).tm_sec
		leftSec=(hour-currentHour)*3600+(minute-currentMin)*60+sec-currentsec
		print(leftSec)
		threadCallback=Thread(target=callback2, args=(leftSec,))
		threadCallback.daemon=True
		threadCallback.start()
		# if(currentHour==hour and currentMin==minute and currentsec==sec):
		# 	print("if")
		# 	m.moveTo(x1,y1)
		# 	m.doubleClick
		# 	break

	else: 
		return False

def callback2(leftSec):
	for i in range(leftSec):
		print(leftSec)
		h=int(leftSec/3600)
		tmp_leftSec=leftSec-3600*h
		m=int(tmp_leftSec/60)
		tmp_leftSec=tmp_leftSec-60*m
		s=int(tmp_leftSec)
		desc=str(h)+"h "+str(m)+"min "+str(s)+"sec"
		timedescdp.configure(text=desc)
		leftSec-=1
		time.sleep(1)
	print("end")
	print("execute?")
	automouse.moveTo(x1,y1)
	automouse.doubleClick()

def set(x,y):
	targetXdp.configure(text=str(x))
	targetYdp.configure(text=str(y))


def buttonClicked():
    with mouse.Listener( #마우스 모니터링 
        on_click=onclick
        ) as listener:
        listener.join()
        set(automouse.position().x,automouse.position().y)
   
 
def onclick(x, y, button, pressed):
    if pressed:
        global x1
        global y1
        global text_var
        x1 = x
        y1 = y
        #set(x,y)  //이것도 멈추네;;
        #넣으면 멈춤 그이유는?targetXdp.configure(text='aaa')
		
    if not pressed:
        return False
 
def editEntry():
    entry3.delete(0,"end") #처음부터 끝까지 삭
    entry4.delete(0,"end")
    #entry5.insert("end",x1) #끝에 입력
 

root.mainloop()