from tkinter import *
from tkinter import ttk
import threading
import time
from main import Back


class Choose:

    def __init__(self, root, streak="invalid"):
        self.streak= streak
        self.root = root
        self.rec = Back(self)
        self.currframe = "frame"
        

        root.title("Speech Bot")
        root.geometry("800x600")
        mainframe = ttk.Frame(root, padding=(3,3,12,12))
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))



        label = ttk.Label(mainframe, text="Talk About",font=('Arial',30,"bold")).grid(column=2,columnspan=10,row=1,sticky=(W,E))
        
        ttk.Button(mainframe,text="Random Topic",command=self.Topic).grid(column=1,row=2,sticky=E)
        ttk.Button(mainframe,text="Today's Day", command=self.speechStart).grid(column=3,row=2,sticky=W)
        ttk.Label(mainframe, text="Streak "+self.streak,font=('Arial',20)).grid(column=3,row=3,sticky=(W,N))
         
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5) 
        self.mainframe = mainframe
        


    def Topic(self):
        try:
            self.mainframe.destroy()
        except:
            pass
        self.prepFrame = ttk.Frame(self.root)
        self.prepFrame.grid(column=0,row=0)

        ttk.Label(self.prepFrame, text="Random TOpic",font=("Arial",30)).grid(column=2,row=1)
        ttk.Label(self.prepFrame, text="Prepration time").grid(column=1,row=2)
        self.mylabel = ttk.Label(self.prepFrame,text="")
        ttk.Label(self.prepFrame, text="You have to speak for 5 min",font=("Arial",30)).grid(column=2,row=3)
        self.mylabel.grid(column=2,row=2)
        self.countdown = 5
        self.currframe = "prep"
        self.timer()

    def timer(self):  
        if self.countdown >= 0:
            self.mylabel.config(text = str(self.countdown), font=30)
            self.countdown -= 1
            self.mylabel.after(1000, self.timer)
        else:
            time.sleep(0.1)
            if self.currframe == "prep":
                self.prepFrame.destroy()
                self.speechStart()
            elif self.currframe == "start":
                self.speechFrame.destroy()
                self.Recording()
                self.currframe = ""
            else:
                self.recordingFrame.destroy()
                self.waiting(self.rec.transcribe) 
                
            

    def speechStart(self):
        try:
            self.mainframe.destroy()
        except:
            pass
        self.speechFrame = ttk.Frame(self.root)
        self.speechFrame.grid(column=0,row=0)
        ttk.Label(self.speechFrame, text="Start", font=("Arial",30)).grid(column=2,row=1)
        self.mylabel = ttk.Label(self.speechFrame, text='')
        self.mylabel.grid(column=2,row=2)
        self.countdown = 5
        self.currframe = "start"
        self.timer()
        
    def Recording(self):
        self.recordingFrame = ttk.Frame(self.root)
        self.recordingFrame.grid(column=0,row=0)
        ttk.Label(self.recordingFrame, text="Recording Started", font=("Arial",30)).grid(column=2,row=1)
        self.countdown = 5
        self.mylabel = ttk.Label(self.recordingFrame, text='')
        self.mylabel.grid(column=2,row=2)
        threading.Thread(target=self.rec.voiceRecording).start()
        self.timer()
        
        
    
    def waiting(self,functoCall):
        self.waitingFrame = ttk.Frame(self.root)
        self.waitingFrame.grid(column=0,row=0)
        label = ttk.Label(self.waitingFrame, text="Loading", font=("Arial",30))
        label.grid(column=2,row=2)
        label.after(5000, functoCall)
        
            
    def speechDisplay(self,text):
        self.waitingFrame.destroy()
        self.speechFrame = ttk.Frame(self.root)
        self.speechFrame.grid(column=0,row=0)
        ttk.Label(self.speechFrame, text=text, font=("Arial",30), wraplength= 700).grid(column=2,row=1)
        
        ttk.Button(self.speechFrame,text = "Next",command=self.rec.analyseSpeech).grid(column = 3, row = 3)
        
        
    def analysisDisplay(self,text):
        self.speechFrame.destroy()
        self.analysisFrame = ttk.Frame(self.root)
        self.analysisFrame.grid(column=0,row=0)
        ttk.Label(self.analysisFrame, text=text, font=("Arial",30), wraplength= 700).grid(column=2,row=1)
        
        ttk.Button(self.analysisFrame,text = "Next").grid(column = 3, row = 3)
    
    
        
    


root = Tk()
Choose(root)
root.mainloop()