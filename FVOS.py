#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
import urllib.request
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path
import board
import busio
import adafruit_fingerprint
import serial
import math
import csv
import time
uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("FVOS.json",scope)
client = gspread.authorize(creds)
sheet= client.open("FVOS").sheet1


username = sheet.cell(1,2).value #that's the given username
password = sheet.cell(2,2).value #that's the given password

TITLE_FONT = ("Algerian", 35, "bold")
BUTTON_FONT = ("Algerian", 28, "bold")
DISPLAY_FONT = ("Arial", 18, "bold")

img0 = Image.open('./Wallpaper/0.gif')
img1 = Image.open('./Wallpaper/1.gif')
img2 = Image.open('./Wallpaper/2.gif')
img3 = Image.open('./Wallpaper/3.gif')
img4 = Image.open('./Wallpaper/4.gif')
img5 = Image.open('./Wallpaper/5.gif')
img6 = Image.open('./Wallpaper/6.gif')
img7 = Image.open('./Wallpaper/7.gif')



def get_fingerprint():    
    """Get a finger print image, template it, and see if it matches!"""
    
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    
    if finger.finger_fast_search() != adafruit_fingerprint.OK:
        return False
    
    
   
    if(finger.finger_id%9)==0:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)        
        sheet.update_cell(1,3,m)
               
    elif(finger.finger_id%9)==1:
      
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)        
        sheet.update_cell(1,3,m)
                
    elif(finger.finger_id%9)==2:
       
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)
        
    elif(finger.finger_id%9)==3:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)

    elif(finger.finger_id%9)==4:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)

    elif(finger.finger_id%9)==5:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)

    elif(finger.finger_id%9)==6:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)

    elif(finger.finger_id%9)==7:
        
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)
        
    else:
       
        p=finger.finger_id/9
        math.trunc(p)
        m=int(p+4)
        sheet.update_cell(1,3,m)

    return True

def file(t):
    with open('FVOS.txt','a') as f:
        f.writelines("%s"% line for line in t)
        f.writelines("\n")


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False


# test
def votecheck(self):
        msgox = messagebox.showwarning(title='Voted', message='You Have Already Voted',parent=self)
        if msgox == 'yes':
            page="FingPage"
            self.cancel()
        else :
            page="FingPage"
            self.cancel()
        return page

def thank(controller):
    mgbox = messagebox.showinfo(title='Voted', message='Thankyou For Voting',parent=controller)
    if mgbox == 'yes' :
        controller.show_frame("FingPage")
        
    else :
        controller.show_frame("FingPage")


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Fingerprint Voting Online System")
        self.geometry("1280x720")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        txt=open("/home/pi/Pictures/FVOS/fvos.txt","w+")                 
        
        self.arrow0 = ImageTk.PhotoImage(img0)
        self.arrow1 = ImageTk.PhotoImage(img1)
        self.arrow2 = ImageTk.PhotoImage(img2)
        self.arrow3 = ImageTk.PhotoImage(img3)
        self.arrow4 = ImageTk.PhotoImage(img4)
        self.arrow5 = ImageTk.PhotoImage(img5)
        self.arrow6 = ImageTk.PhotoImage(img6)
        self.arrow7 = ImageTk.PhotoImage(img7)
        
        
        self.frames = {}
        for F in (IntroPage, AdminPage, FingPage, ServerPage, ErrorPage, VoterPage, VotingPage, ConfirmPage1, ConfirmPage2, ConfirmPage3, ConfirmPage4, ConfirmPage5, ConfirmPage6, ConfirmPage7, ConfirmPage8, ConfirmPage9):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            
        self.show_frame("IntroPage" if connect() else "ServerPage")
        
   
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
        

   
class IntroPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow0)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="  WELCOME  ", font=TITLE_FONT, relief="ridge", fg="white",bg="black")
#        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top")
        label.place(x=500,y=0)
        button2 = tk.Button(self, text="ENTER", font=BUTTON_FONT, width=17, height=1,relief="raised",bg="lightgreen",
                            command=lambda: controller.show_frame("AdminPage"  if connect() else "ServerPage"))
        button2.pack(side="bottom")
        button2.place(x=420, y=470)
        
        

        
        
          

class AdminPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow1)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="  ADMIN PAGE  ", font=TITLE_FONT, relief="ridge", fg="white",bg="black")
#        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top")
        label.place(x=400,y=0)
        #username entry
        username_entry = tk.Entry(self, width=15, font= "Arial 32", bg="black", fg="white")
        username_entry.place(x= 400,y =218)
        label8 = tk.Label(self, text="ID", width=12, font="Arial 14", relief="sunken", bg="lightblue")
        label8.place(x=400,y=190)
        #password entry
        password_entry = tk.Entry(self, width =15 , font="Arial 32", show='*',bg="black", fg="white")
        password_entry.place(x=400, y=318)
        label9 = tk.Label(self, text="PASSWORD", width=12, font="Arial 14", relief="sunken",bg="lightblue")
        label9.place(x=400,y=290)
        button2 = tk.Button(self, text="Login", font=BUTTON_FONT, width=10, height=2,relief="groove",bg="white",
                            command=lambda: controller.show_frame("FingPage" if username == username_entry.get() and password == password_entry.get() and connect() else "AdminPage"))
        button2.pack(side="left")
        button2.place(x=960, y=520)


        
class FingPage(tk.Frame):
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow2)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top")
        label.place(x=400,y=0)
             
        button2 = tk.Button(self, text="SCAN", font=BUTTON_FONT, width=10, height=2,relief="groove",bg="white",
                            command=lambda :controller.show_frame("VoterPage" if get_fingerprint()  else "ErrorPage"))
        button2.pack(side="left")
        button2.place(x=960, y=520)


    
class ServerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow2 = tk.Label(self, image = self.controller.arrow3)
        arrow2.pack(side="top")
        arrow2.place(x=40,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
#        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top")
        label.place(x=400,y=0)
        button = tk.Button(self, text="CHECK FOR CONNECTION", font=BUTTON_FONT, width=25, height=1,relief="groove",bg="green",
                           command=lambda: controller.show_frame("FingPage" if connect() else "ServerPage"))
        button.pack(side="left")
        button.place(x=300, y=520)

class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow2 = tk.Label(self, image = self.controller.arrow7)
        arrow2.pack(side="top")
        arrow2.place(x=40,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
#        label.pack(side="top", fill="x", pady=10)
        label.pack(side="top")
        label.place(x=400,y=0)
        button = tk.Button(self, text="  TRY AGAIN   ", font=BUTTON_FONT, width=25, height=1,relief="groove",bg="green",
                           command=lambda: controller.show_frame("FingPage" if connect() else "ServerPage"))
        button.pack(side="left")
        button.place(x=300, y=520)
        
        
                         
 
class VoterPage(tk.Frame):
    
    def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         self.controller = controller
         self.controller.got_it1=tk.StringVar()
         self.controller.gotit1="LOADING"
         arrow1 = tk.Label(self, image = self.controller.arrow4)
         arrow1.pack(side="top")
         arrow1.place(x=0,y=0)
         label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
         #        label.pack(side="top", fill="x", pady=10)
         label.pack(side="top")
         label.place(x=400,y=0)
         
         arrow3 = tk.Label(self, textvariable = self.controller.got_it1, font=BUTTON_FONT, relief="ridge",width=20,height=7)
         arrow3.pack(side="right")
         arrow3.place(x=400,y=100)
         label = tk.Label(self, text="NAME : ", width=11, height=2, font=BUTTON_FONT, relief="sunken",bg="white")
         label.pack(side="top")
         label.place(x=70,y=100)
         label = tk.Label(self, text="AADHAR : ", width=11 ,height=2, font=BUTTON_FONT, relief="sunken",bg="white")
         label.pack(side="top")
         label.place(x=70,y=210)
         label = tk.Label(self, text="VOTER ID : ", width=11, height=2, font=BUTTON_FONT, relief="sunken",bg="white")
         label.pack(side="top")
         label.place(x=70,y=315)
         self.controller.TimerInterval=200
         self.controller.job=0
         
         button1 = tk.Button(self, text="GET DETAILS", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="blue",
                             command= lambda: self.gotvalue())
         button1.pack()
         button1.place(x=950, y=410)
         button1 = tk.Button(self, text="VOTE", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="blue",
                             command= lambda: [controller.show_frame("VotingPage" if sheet.cell(sheet.cell(1,3).value,5).value=='NOT DONE' else votecheck(self)),self.cancel()])
         button1.pack()
         button1.place(x=950, y=520)

    def cancel(self):
        if self.controller.job is not None:
            self.controller.gotit1= "LOADING"
            self.controller.after_cancel(self.controller.job)
            self.controller.job = None
                    
         
    def gotvalue(self):
        
        self.controller.got_it1.set(self.controller.gotit1)
        self.controller.gotit1=sheet.cell(sheet.cell(1,3).value,4).value
        self.controller.job=self.controller.after(self.controller.TimerInterval,self.gotvalue)
        
    
class VotingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow5)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)

        label = tk.Label(self, text="Whom Do You Want to Vote ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        button = tk.Button(self, text=sheet.cell(5,1).value , font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage1" if connect() else "ServerPage"))
        
        button.pack()
        button.place(x=150, y=200)
    
        button = tk.Button(self, text=sheet.cell(6,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage2" if connect() else "ServerPage"))
        button.pack()
        button.place(x=150, y=350)
        
        
        button = tk.Button(self, text=sheet.cell(7,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage3" if connect() else "ServerPage"))
        button.pack()
        button.place(x=150, y=500)
       
        
        button = tk.Button(self, text=sheet.cell(8,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage4" if connect() else "ServerPage"))
        button.pack()
        button.place(x=500, y=200)
        
        
        button = tk.Button(self, text=sheet.cell(9,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage5" if connect() else "ServerPage"))
        button.pack()
        button.place(x=500, y=350)
       

        button = tk.Button(self, text=sheet.cell(10,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage6" if connect() else "ServerPage"))
        button.pack()
        button.place(x=500, y=500)
        

        button = tk.Button(self, text=sheet.cell(11,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage7" if connect() else "ServerPage"))
        button.pack()
        button.place(x=850, y=200)
        
        
        button = tk.Button(self, text=sheet.cell(12,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage8" if connect() else "ServerPage"))
        button.pack()
        button.place(x=850, y=350)
        
        button = tk.Button(self, text=sheet.cell(13,1).value, font=BUTTON_FONT, width=9, height=2,relief="raised",fg="green",bg="yellow",
                           command=lambda: controller.show_frame("ConfirmPage9" if connect() else "ServerPage"))
        button.pack()
        button.place(x=850, y=500)
                      

class ConfirmPage1(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        global dd
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(5,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"5A3S4S3") and thank(controller), file("5A3S4S3")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage2(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(6,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"8S4D2") and thank(controller), file("8S4D2")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage3(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(7,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"6M3D2D3") and thank(controller), file("6M3D2D3")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage4(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(8,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"2M8D4") and thank(controller), file("2M8D4")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage5(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(9,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"7A7M2S3D5") and thank(controller), file("7A7M2S3D5")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage6(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(10,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"6M5A6D6") and thank(controller), file("6M5A6D6")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage7(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(11,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"6M7A8D7") and thank(controller), file("6M7A8D7")])
        button2.pack(side="left")
        button2.place(x=850, y=520)


class ConfirmPage8(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(12,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"8M6D12A4") and thank(controller), file("8M6D12A4")])
        button2.pack(side="left")
        button2.place(x=850, y=520)
        


class ConfirmPage9(tk.Frame):
   

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        arrow1 = tk.Label(self, image = self.controller.arrow6)
        arrow1.pack(side="top")
        arrow1.place(x=0,y=0)
        label = tk.Label(self, text="      VOTING       ", font=TITLE_FONT, relief="ridge", fg="red",bg="green")
        label.pack(side="top")
        label.place(x=400,y=0)
        label = tk.Label(self, text="CONFIRM ? ", width=35, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label.pack(side="top")
        label.place(x=60,y=70)
        label1 = tk.Label(self, text=sheet.cell(13,1).value, width=15, height=2, font=TITLE_FONT, relief="sunken",bg="white")
        label1.pack(side="top")
        label1.place(x=350,y=300)

        button1 = tk.Button(self, text="NO", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="red",
                            command=lambda: controller.show_frame("VotingPage" if connect() else "ServerPage"))
        button1.pack(side="left")
        button1.place(x=100, y=520)
        button2 = tk.Button(self, text="YES", font=BUTTON_FONT, width=9, height=2,relief="groove",bg="green",
                            command=lambda: [connect() and sheet.update_cell(sheet.cell(1,3).value,5,"DONE") and sheet.update_cell(sheet.cell(1,3).value,6,"9M5D15M3") and thank(controller), file("9M5D15M3")])
        button2.pack(side="left")
        button2.place(x=850, y=520)



if __name__ == "__main__":
    root = SampleApp()
    root.mainloop()

while True:
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError('Failed to read templates')
