from Tkinter import Tk,Toplevel,Canvas,Scale,Frame
from tkFileDialog   import *
from observer import *
from generator import *
from view import *
from lissajou import *
from controller import *
import json
import tkMessageBox
class Oscilloscope :
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("Oscilloscope")
        self.parent.protocol("WM_DELETE_WINDOW", self.exit)
        self.modelX=Generator(name="X",color="red",a=0.0,f=1.0)
        self.modelY=Generator(name="Y",color="green",a=0.0,f=1.0)
        self.model_X_Y=Lissajou("X-Y",self.modelX.get_signal(),self.modelY.get_signal(),"blue")
        self.view=View(parent)
        self.view.grid(8,8)
        self.view.update(self.modelX)
        self.modelX.attach(self.view)
        self.ctrl=Controller(self.modelX,self.view)
        self.view.update(self.modelY)
        self.modelY.attach(self.view)
        self.ctrlY=Controller(self.modelY,self.view)
        self.modelX.attach(self.model_X_Y)
        self.modelY.attach(self.model_X_Y)
        self.view.packing()
        self.createMenu()
        self.createLissajouTK()
    def createMenu(self):
        menubar = Menu(self.parent)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open",command=self.openFile)
        filemenu.add_command(label="Save",command=self.saveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=self.exit)

        viewMenu = Menu(menubar, tearoff=0)
        viewMenu.add_command(label="Show lissajou",command=self.show_lissajou)

        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="about us",command=self.aboutUs)

        menubar.add_cascade(label="File", menu=filemenu)
        menubar.add_cascade(label="View", menu=viewMenu)
        menubar.add_cascade(label="Help", menu=helpMenu)

        self.parent.configure(menu=menubar)
    def saveFile(self):
        mesFormats = [ ('Texte','*.json')
               ]
        nomFichier = asksaveasfilename(parent=self.parent,filetypes=mesFormats,title="Sauvez le signal sous...")
        if len(nomFichier) > 0:
            print "Sauvegarde en cours dans %s" % nomFichier
            if nomFichier:

                # Writing JSON data
                with open(nomFichier, 'w') as f:
                    signalX={'frequency': self.view.get_frequency("X").get(),
                         'magnitude': self.view.get_magnitude("X").get(),
                         'phase': self.view.get_phase("X").get(),
                         'name':"X",'color':"red"}
                    signalY={'frequency': self.view.get_frequency("Y").get(),
                         'magnitude': self.view.get_magnitude("Y").get(),
                         'phase': self.view.get_phase("Y").get(),
                         'name':"Y",'color':"green"}
                    signals=[]
                    signals.append(signalX)
                    signals.append(signalY)
                    datastore = {'signal': signals}

                    json.dump(datastore, f)
    def openFile(self):
        mesFormats = [ ('Texte','*.json')]
        nomFichier = askopenfilename(parent=self.parent,filetypes=mesFormats,title="Ouvrire un signal")
        if len(nomFichier) > 0:
            print "open file  dans %s" % nomFichier
                #Read JSON data into the datastore variable
        if nomFichier:
            with open(nomFichier, 'r') as f:
                datastore = json.load(f)
            for signal in datastore["signal"] :
                if signal['name']=="X" :
                    self.modelX.set_phase(signal["phase"])
                    self.modelX.set_frequency(signal["frequency"])
                    self.modelX.set_magnitude(signal["magnitude"])
                    self.view.set_magnitude(signal["magnitude"],"X")
                    self.view.set_phase(signal["phase"],"X")
                    self.view.set_frequency(signal["frequency"],"X")
                elif signal['name']=="Y" :
                    self.modelY.set_phase(signal["phase"])
                    self.modelY.set_frequency(signal["frequency"])
                    self.modelY.set_magnitude(signal["magnitude"])
                    self.view.set_magnitude(signal["magnitude"],"Y")
                    self.view.set_phase(signal["phase"],"Y")
                    self.view.set_frequency(signal["frequency"],"Y")

            self.modelX.generate_signal()
            self.modelY.generate_signal()


    def aboutUs(self):
        tkMessageBox.showinfo("About US","This software is created by BreuhTeam company.\nDevelopers :\n - HAMDANI RIDAE")
    def exit(self) :
        if tkMessageBox.askyesno("Exit","are you sure you want to exit?"):
            self.parent.destroy()

    def createLissajouTK(self) :
        self.top=Toplevel(self.parent)
        self.top.title("Lissajou")
        self.lissajou=Screen(self.top)
        self.lissajou.grid(8,8)
        self.lissajou.update(self.model_X_Y)
        self.model_X_Y.attach(self.lissajou)
        self.lissajou.packing()
        self.top.protocol("WM_DELETE_WINDOW", self.exit_lissajou)
    def exit_lissajou(self):
        self.model_X_Y.detach(self.lissajou)
        self.top.destroy()
    def show_lissajou(self):
        if not self.top.winfo_exists():
            self.createLissajouTK()

if  __name__ == "__main__" :
    
    root=Tk()
    root.geometry("+300+100")
    oscillo=Oscilloscope(root)
    root.mainloop()
