from __future__ import absolute_import
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import customtkinter
import os
import time
from FootballMatch.FootballMatch import hic_main as hic
import cv2
import imutils
import pandas as pd
from datetime import datetime
import winsound
PATH = os.path.dirname(os.path.realpath(__file__))

WIDTH = 1455
HEIGHT = 700
player = {}

class MainFrame(tk.Tk):
    """
    frmae object holding all of our different pages
    controller of my pages: setting up the ID, fun..
    """
    def __init__(self,*args, **kwargs) -> None:
        tk.Tk.__init__(self,*args,**kwargs)
        global WIDTH
        global HEIGHT
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        #print screen size
        print('Screen width:', screen_width)
        print('Screen Height:', screen_height)
        screenStr = str(screen_width) + 'x' + str(screen_height)
        WIDTH = screen_width
        HEIGHT = screen_height


        self.geometry(screenStr)
        #self.attributes('-fullscreen',True)

        self.titlefont = tkfont.Font(family='Verdana',size=12,
                        weight="bold",slant='roman')
        self.resizable(False, False)
        
        self.container = tk.Frame(self)
        self.container.pack(side="right", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.columnconfigure(0, weight=1)

        self.id = tk.StringVar()
        self.id.set("HawkIFootball")
        self.listing = {}
        self.pages = HomePage

        # GameStartPage, TimerPage, LiveViewPage, ScorePage,
        # for p in (HomePage, PlayerInfo, GameStartPage, TimerPage, LiveViewPage, ScorePage, LeaderBoardPage):
        #     page_name = p.__name__
        #     frame = p(parent = container, controller=self)
        #     frame.grid(row=0,column=0,sticky='nesw')
        #     self.listing[page_name] = frame

        self.up_frame(HomePage)
        
    def up_frame(self,p):
        page_name = p.__name__
        frame = p(parent = self.container, controller=self)
        frame.grid(row=0,column=0,sticky='nesw')
        page = frame
        page.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id  
        # self.place(x=50,y=80)   
        image = Image.open(PATH + "/StartPageBg.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        bou = customtkinter.CTkButton(master=self, text="START GAME",
                                                corner_radius=6, command=self.button_event,width=200,bg_color='#ffc000',text_font=('moonhouse',24,'bold'),fg_color='#ffc000',hover_color='#ca9a08')
        # bou.pack(padx=100)
        bou.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        

    def button_event(self):
        print("submit pressed")  
        self.controller.up_frame(PlayerInfo)    
        # self.controller.up_frame(LeaderBoardPage)    

    

class PlayerInfo(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = "player"
        # self.p = PlayerInfo
        
        # self.controller.pages = PlayerInfo

        image = Image.open(PATH + "/PlayerInfoBg.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # self.config(background='#000140')
        # self.grid(row=0,column=0)
        # label_msg = tk.canvas.create_text((410, 120), text="Earth Hour Countdown:", font="MSGothic 50 bold", fill="#652828")
        
        # self.label_1 = customtkinter.CTkLabel(master=self, width=200, height=50,
        #                                       fg_color=('#001256'), 
        #                                       text_font=('Berlin Sans FB Demi',60,'bold'),
        #                                       text="Player Info",text_color='white')
        # self.label_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.label_name = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#001256'), corner_radius=6,bg_color='#001256',
                                              text_font=('Berlin Sans FB Demi',16,'bold'),
                                              text="Firstname",text_color='white')
        self.label_name.place(relx=0.25, rely=0.34)

        self.entry_1 = customtkinter.CTkEntry(master=self, corner_radius=6, width=400, placeholder_text="Name",bg_color='#001256',fg_color='#001256',text_color='white')
        self.entry_1.place(relx=0.5, rely=0.36, anchor=tk.CENTER)

        self.label_lastname = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#001256'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),
                                              text="Lastname",text_color='white')
        self.label_lastname.place(relx=0.25, rely=0.40)

        self.entry_2 = customtkinter.CTkEntry(master=self, corner_radius=6, width=400, placeholder_text="Lastname",fg_color='#001256',text_color='white')
        self.entry_2.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

        self.label_email = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#001256'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),
                                              text="Email",text_color='white')
        self.label_email.place(relx=0.25, rely=0.46)

        self.entry_3 = customtkinter.CTkEntry(master=self, corner_radius=6, width=400, placeholder_text="Email",fg_color='#001256',text_color='white')
        self.entry_3.place(relx=0.5, rely=0.48, anchor=tk.CENTER)


        self.label_mobile = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#001256'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),
                                              text="Mobile No",text_color='white')
        self.label_mobile.place(relx=0.25, rely=0.52)

        self.entry_4 = customtkinter.CTkEntry(master=self, corner_radius=6, width=400, placeholder_text="Mobile",fg_color='#001256',text_color='white')
        self.entry_4.place(relx=0.5, rely=0.54, anchor=tk.CENTER)


        self.label_org = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#000140'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),
                                              text="Organization",text_color='white')
        self.label_org.place(relx=0.25, rely=0.58)
        self.entry_5 = customtkinter.CTkEntry(master=self, corner_radius=6, width=400, placeholder_text="Organization",fg_color='#001256',text_color='white')
        self.entry_5.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.button_2 = customtkinter.CTkButton(master=self, text="SUBMIT",
                                                corner_radius=6, command=self.button_event, width=200,height=10,bg_color='#ffc000',text_font=('moonhouse',24,'bold'),fg_color='#ffc000',hover_color='#ca9a08')
        self.button_2.place(relx=0.566, rely=0.7, anchor=tk.CENTER)
        # bou = tk.Button(self, text="to page main",command=lambda:controller.up_frame("HomePage"))
        # bou.pack()

    def button_event(self):
        print("submit pressed")
        name = self.entry_1.get()
        lastname = self.entry_2.get()
        email = self.entry_3.get()
        mobile = self.entry_4.get()
        organization = self.entry_5.get()
        player['firstname'] = name
        player['lastname'] = lastname
        player['email'] = email
        player['mobile'] = mobile
        player['organization'] = organization
        print(player)
        self.controller.up_frame(GameStartPage)

class GameStartPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        image = Image.open(PATH + "/GameStartBg.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        hic.get_metadata()
        meta_image = Image.open(PATH + "/FootballMatch/FootballMatch/position/positions.png").resize((WIDTH, HEIGHT))
        resized_image= meta_image.resize((900,550), Image.ANTIALIAS)
        self.pos_image = ImageTk.PhotoImage(resized_image)
        self.pos_image_label = tk.Label(master=self, image=self.pos_image)
        self.pos_image_label.place(relx=0.4, rely=0.6, anchor=tk.CENTER)


        seconds = tk.StringVar()
        seconds.set("10")
        self.label_time = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#141414'), 
                                              text_font=('Berlin Sans FB Demi',50,'bold'),bg_color="#141414",
                                              text="",text_color='white')
        self.label_time.place(relx=0.778, rely=0.55)
        # time.sleep(1)

        # t1=10
        # t=0
        # while t < 10:
        #     t = t + 1
        #     t1 = t1 - 1
        #     time.sleep(1)
        #     print(seconds,t1)
        #     seconds.set("{0}".format(t1))

        self.remaining = 0
        self.countdown(10)
        # time.sleep(1)

        
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label_time.configure(text="time's\nup!")
            self.controller.up_frame(TimerPage)
        else:
            self.label_time.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
    
    
    

class TimerPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        image = Image.open(PATH + "/LiveView.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        
        self.label_time = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#141414'), bg_color="#141414",
                                              text_font=('Berlin Sans FB Demi',100,'bold'),
                                              text="",text_color='white')
        self.label_time.place(relx=0.5, rely=0.48,anchor=tk.CENTER)

        self.remaining = 0
        self.countdown(20)
        # time.sleep(1)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
        print("inside timer")
        if self.remaining <= 0:
            self.label_time.configure(text="time's\nup!")
            cap,live_image = hic.liveView()
            winsound.Beep(2500, 2000)
            time.sleep(4)
            isDone = hic.cam(cap)
            print(isDone)
            cap.release()
            if isDone:
                self.controller.up_frame(LiveViewPage)
        else:
            self.label_time.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
            

class LiveViewPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        image = Image.open(PATH + "/Picture4.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        print("inside Livepage")
        
        self.image_cam = tk.Label(master=self)
        self.image_cam.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        live_image = Image.open(PATH + "/FootballMatch/FootballMatch/resultImages/recent_picture.jpg").resize((WIDTH, HEIGHT))
        self.live_image = ImageTk.PhotoImage(live_image)
        self.live_label = tk.Label(master=self, image=self.live_image)
        self.live_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.remaining = 0
        
        self.countdown(5)
        # time.sleep(1)

        
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            # self.label_time.configure(text="time's\nup!")
            self.controller.up_frame(ScorePage)
        else:
            # self.label_time.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
        

   




class ScorePage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        image = Image.open(PATH + "/ScoreBg.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        res = hic.process()
        player['score'] = res
        player['date'] = datetime.now()

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.score_label = customtkinter.CTkLabel(master=self, width=100,
                                              fg_color=('#ff3a17'), 
                                              text_font=('Berlin Sans FB Demi',30,'bold'),bg_color='#ff3a17',
                                              text=player.get('score',0),text_color='black')
        self.score_label.place(relx=0.49, rely=0.5, anchor=tk.CENTER)
        print(1,player)
        new = pd.DataFrame.from_dict([player])
        new.to_csv(PATH+"/FootballMatch/FootballMatch/scores/score_board.csv",mode='a', index=False,header=False)
        ##player to csv
        # time.sleep(3)
        self.remaining = 0

        self.countdown(5)
        # time.sleep(1)

        
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            # self.label_time.configure(text="time's\nup!")
            player = {}
            # self.controller.up_frame(HomePage) 1
            self.controller.up_frame(LeaderBoardPage)

        else:
            # self.label_time.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
        


        print(1)

class LeaderBoardPage(tk.Frame):
    
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.id = controller.id
        image = Image.open(PATH + "/LeaderBoardBg.jpg").resize((WIDTH, HEIGHT))
        self.bg_image = ImageTk.PhotoImage(image)

        self.image_label = tk.Label(master=self, image=self.bg_image)
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        df = pd.read_csv(PATH+'/FootballMatch/FootballMatch/scores/score_board.csv')
        print(df)
        df = df.sort_values(by='Score', ascending=False)
        print('df = ',df)
        res = df.head(8)
        print('First 5 : ',res)
        name1 = res.iloc[0]['Firstname']
        score1 = res.iloc[0]['Score']
        print(score1)
        name2 = res.iloc[1]['Firstname']
        score2 = res.iloc[1]['Score']
        name3 = res.iloc[2]['Firstname']
        score3 = res.iloc[2]['Score']
        name4 = res.iloc[3]['Firstname']
        score4 = res.iloc[3]['Score']
        name5 = res.iloc[4]['Firstname']
        score5 = res.iloc[4]['Score']
        name6 = res.iloc[5]['Firstname']
        score6 = res.iloc[5]['Score']
        name7 = res.iloc[6]['Firstname']
        score7 = res.iloc[6]['Score']
        name8 = res.iloc[7]['Firstname']
        score8 = res.iloc[7]['Score']
        self.name_label1 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="1. "+str(name1),text_color='black')
        self.name_label1.place(relx=0.26, rely=0.32)
        self.score_label1 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score1,text_color='black')
        self.score_label1.place(relx=0.65, rely=0.32)

        self.name_label2 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="2. "+str(name2),text_color='black')
        self.name_label2.place(relx=0.26, rely=0.40)
        self.score_label2 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score2,text_color='black')
        self.score_label2.place(relx=0.65, rely=0.40)


        self.name_label3 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="3. "+str(name3),text_color='black')
        self.name_label3.place(relx=0.26, rely=0.48)
        self.score_label3 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score3,text_color='black')
        self.score_label3.place(relx=0.65, rely=0.48)


        self.name_label4 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="4. "+str(name4),text_color='black')
        self.name_label4.place(relx=0.26, rely=0.56)
        self.score_label4 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score4,text_color='black')
        self.score_label4.place(relx=0.65, rely=0.56)


        self.name_label5 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="5. "+str(name5),text_color='black')
        self.name_label5.place(relx=0.26, rely=0.66)
        self.score_label5 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score5,text_color='black')
        self.score_label5.place(relx=0.65, rely=0.66)

        self.name_label6 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="6. "+str(name6),text_color='black')
        self.name_label6.place(relx=0.26, rely=0.74)
        self.score_label6 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score6,text_color='black')
        self.score_label6.place(relx=0.65, rely=0.74)

        self.name_label7 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="7. "+str(name7),text_color='black')
        self.name_label7.place(relx=0.26, rely=0.82)
        self.score_label7 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score7,text_color='black')
        self.score_label7.place(relx=0.65, rely=0.82)

        self.name_label8 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text="8. "+str(name8),text_color='black')
        self.name_label8.place(relx=0.26, rely=0.89)
        self.score_label8 = customtkinter.CTkLabel(master=self, width=150,
                                              fg_color=('#0c5db0'), 
                                              text_font=('Berlin Sans FB Demi',16,'bold'),bg_color='#0c5db0',
                                              text=score8,text_color='black')
        self.score_label8.place(relx=0.65, rely=0.89)

        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
                # self.label_time.configure(text="time's\nup!")
            player = {}
                # self.controller.up_frame(HomePage) 1
            # app.mainloop()

            self.controller.up_frame(HomePage)


        else:
                # self.label_time.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)



        # self.button_2 = customtkinter.CTkButton(master=self, text="RESTART",
        #                                         corner_radius=6, command=self.button_event, width=200,height=10,bg_color='#ffc000',text_font=('moonhouse',24,'bold'),fg_color='#ffc000',hover_color='#ca9a08')
        # self.button_2.place(relx=0.566, rely=0.7, anchor=tk.CENTER)

if __name__ == "__main__":

    app = MainFrame()

    app.mainloop()        
    