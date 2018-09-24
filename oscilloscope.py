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
        self.parent.protocol("WM_DELETE_WINDOW", self.exit)
        self.modelX=Generator(name="X")
        self.modelY=Generator(name="Y",color="green")
        self.model_X_Y=Lissajou("X-Y",self.modelX.get_signal(),self.modelY.get_signal(),"blue")
        self.view=Screen(parent)
        self.view.grid(8,8)
        self.view.update(self.modelX)
        self.modelX.attach(self.view)
        self.ctrl=Controller(self.modelX,self.view)
        self.view.update(self.modelY)
        self.modelY.attach(self.view)
        self.ctrlY=Controller(self.modelY,self.view)
        self.view.update(self.model_X_Y)
        self.model_X_Y.attach(self.view)
        self.modelX.attach(self.model_X_Y)
        self.modelY.attach(self.model_X_Y)
        self.view.packing()
        self.createMenu()
    def createMenu(self):
        menubar = Menu(self.parent)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open",command=self.openFile)
        filemenu.add_command(label="Save",command=self.saveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=self.quite)

        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="about us",command=self.aboutUs)

        menubar.add_cascade(label="File", menu=filemenu)
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
                    datastore = {'signal': {'frequency': self.view.get_frequency().get(),
                         'magnitude': self.view.get_magnitude().get(),
                         'phase': self.view.get_phase().get()}}

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
            self.model.set_phase(datastore["signal"]["phase"])
            self.model.set_frequency(datastore["signal"]["frequency"])
            self.model.set_magnitude(datastore["signal"]["magnitude"])
            self.view.set_magnitude(datastore["signal"]["magnitude"])
            self.view.set_phase(datastore["signal"]["phase"])
            self.view.set_frequency(datastore["signal"]["frequency"])

            self.model.generate_signal()

    def aboutUs(self):
        tkMessageBox.showinfo("About US","This software is created by BreuhTeam company.\nDevelopers :\n - HAMDANI RIDAE")
    def quite(self):
        answer=tkMessageBox.askokcancel("Exit","are you sure you want to exit?")
        if answer  :
            self.parent.destroy()
    def exit(self) :
        if tkMessageBox.askyesno("Exit","are you sure you want to exit?"):
            self.parent.destroy()

if  __name__ == "__main__" :
    root=Tk()

    oscillo=Oscilloscope(root)
    root.mainloop()
