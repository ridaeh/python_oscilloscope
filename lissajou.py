from math import pi,sin
from observer import *

class Lissajou(Subject):
    # every signal have to be initialise with a frequency,magnitude,phase,
    # color to make the difference betwen signal
    # and name to update the correct signal when we use view->update methode
    def __init__(self,name,signalX,signalY,color="red"):
        Subject.__init__(self)
        self.signal=[]
        self.color=color
        self.name=name
        self.signalX,self.signalY=signalX,signalY
        self.generate_signal()
    def generate_signal(self):
        del self.signal[0:]
        samples=1000
        i=0
        for i in range(0, len(self.signalX)):
                self.signal.append((self.signalX[i][1], self.signalY[i][1]))

        self.notify()
    def get_signal(self):
        return self.signal
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
    def update(self,model):
        self.generate_signal()
