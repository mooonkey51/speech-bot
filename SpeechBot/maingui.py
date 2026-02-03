from tkinter import *
from tkinter import ttk

class Choose:

    def __init__(self, root, streak="invalid"):
        self.streak= streak
        self.root = root

        root.title("Speech Bot")
        root.geometry("800x600")
        mainframe = ttk.Frame(root, padding=(3,3,12,12))
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))



        label = ttk.Label(mainframe, text="Talk About",font=('Arial',30,"bold")).grid(column=2,columnspan=10,row=1,sticky=(W,E))
        
        ttk.Button(mainframe,text="Random Topic",command=self.Topic).grid(column=1,row=2,sticky=E)
        ttk.Button(mainframe,text="Today's Day").grid(column=3,row=2,sticky=W)
        ttk.Label(mainframe, text="Streak "+self.streak,font=('Arial',20)).grid(column=3,row=3,sticky=(W,N))


        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5) 
        self.mainframe = mainframe


    def Topic(self):
        self.mainframe.destroy()
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
            if self.currframe == "prep":
                self.prepFrame.destroy()
                self.speechStart()
            

    def speechStart(self):
        
        self.speechFrame = ttk.Frame(self.root)
        self.speechFrame.grid(column=0,row=0)
        ttk.Label(self.speechFrame, text="Start", font=("Arial",30)).grid(column=2,row=1)
        self.mylabel = ttk.Label(self.speechFrame, text='')
        self.mylabel.grid(column=2,row=2)
        self.countdown = 10
        self.currframe = "start"
        self.timer()


root = Tk()
Choose(root)
root.mainloop()