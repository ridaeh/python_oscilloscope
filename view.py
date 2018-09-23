from Tkinter import Canvas,Scale,Menu,Frame
from observer import *

class Screen(Observer):
    def __init__(self,parent,bg="white"):
        self.canvas=Canvas(parent,bg=bg)
        print("parent",parent.cget("width"),parent.cget("height"))
        self.createOptionsFrame(parent)
        parent.bind("<Configure>", self.resize)
        self.magnitudeX.set(1)
        self.frequencyX.set(1)
        self.magnitudeY.set(1)
        self.frequencyY.set(1)
        self.parent=parent
        self.width=int(self.canvas.cget("width"))
        self.height=int(self.canvas.cget("height"))
        self.models=[]
    def update(self,model):
        if model not in self.models:
            self.models.append(model)
        print("View update")
        signal=model.get_signal()
        self.plot_signal(signal,model.get_color(),model.get_name())


    def get_magnitude(self,name):
        if name =="X" :
            return self.magnitudeX
        return self.magnitudeY
    def get_frequency(self,name):
        if name =="X" :
            return self.frequencyX
        return self.frequencyY
    def get_phase(self,name):
        if name =="X" :
            return self.phaseX
        return self.phaseY
    def set_magnitude(self,x,name):
        if name=="X" :
            self.magnitudeX.set(x)
        else :
            self.magnitudeY.set(x)

    def set_frequency(self,x):
        self.frequency.set(x)
    def set_phase(self,x):
        self.phase.set(x)
    def plot_signal(self,signal,color,name):
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        width,height=int(w),int(h)
        print(self.canvas.find_withtag("signal"+name))
        if self.canvas.find_withtag("signal"+name) :
            self.canvas.delete("signal"+name)
        if signal and len(signal) > 1:
            plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
            signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal"+name)
        return

    def packing(self) :

        self.canvas.pack(fill="both", expand=1)
        self.magnitudeX.grid(row=0,column=0)
        self.frequencyX.grid(row=1,column=0)
        self.phaseX.grid(row=2,column=0)
        self.magnitudeY.grid(row=0,column=1)
        self.frequencyY.grid(row=1,column=1)
        self.phaseY.grid(row=2,column=1)
        self.frame.pack(fill="both")

    def grid(self,n,m):
        self.n=n
        self.m=m
        w,h=self.canvas.winfo_width(),self.canvas.winfo_height()
        self.width,self.height=int(w),int(h)
        step1=self.width/n
        for t in range(1,n):
            x =t*step1
            self.canvas.create_line(x,0,x,self.height,tags="line")
        step=self.height/m
        for t in range(1,m):
            y =t*step
            self.canvas.create_line(0,y,self.width,y,tags="line")
    def resize(self,event):
        self.canvas.delete("line")
        #self.canvas.scale("all",0,0,float(event.width)/float(self.width),float(event.height)/self.height)
        self.grid(self.n,self.m)
        for model in self.models :
            self.plot_signal(model.get_signal(),
                model.get_color(),
                model.get_name())
    def createOptionsFrame(self,parent):
        self.frame = Frame(parent)
        self.magnitudeY=Scale(self.frame,length=250,orient="horizontal",
                         label="Y Magnitude", sliderlength=20,
                         showvalue=0,from_=0,to=4,
                         tickinterval=1)
        self.frequencyY=Scale(self.frame,length=250,orient="horizontal",
                         label="Y Frequence", sliderlength=20,
                         showvalue=0,from_=0,to=32,
                         tickinterval=6)
        self.phaseY=Scale(self.frame,length=250,orient="horizontal",
                         label="Y Phase", sliderlength=20,
                         showvalue=0,from_=-180,to=180,
                         tickinterval=90)
        self.magnitudeX=Scale(self.frame,length=250,orient="horizontal",
                         label="X Magnitude", sliderlength=20,
                         showvalue=0,from_=0,to=4,
                         tickinterval=1)
        self.frequencyX=Scale(self.frame,length=250,orient="horizontal",
                         label="X Frequence", sliderlength=20,
                         showvalue=0,from_=0,to=32,
                         tickinterval=6)
        self.phaseX=Scale(self.frame,length=250,orient="horizontal",
                         label="X Phase", sliderlength=20,
                         showvalue=0,from_=-180,to=180,
                         tickinterval=90)
