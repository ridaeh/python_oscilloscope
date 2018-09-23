from math import pi,sin
from observer import *

class Generator(Subject):
    # every signal have to be initialise with a frequency,magnitude,phase,
    # color to make the difference betwen signal
    # and name to update the correct signal when we use view->update methode
    def __init__(self,name,a=1.0,f=1.0,p=0.0,color="red"):
        Subject.__init__(self)
        self.signal=[]
        self.a,self.f,self.p=a,f,p
        self.color=color
        self.name=name
        self.generate_signal()
    def generate_signal(self):
        del self.signal[0:]
        samples=1000
        for t in range(0,samples,5):
            samples=float(samples)
            e=self.a*sin((2*pi*self.f*(t*1.0/samples))-self.p)
            self.signal.append((t*1.0/samples,e))
        self.notify()
    def set_magnitude(self,a):
        self.a=a
        self.generate_signal()
    def get_magnitude(self):
        return self.a
    def set_frequency(self,f):
        self.f=f
        self.generate_signal()
    def get_frequency(self):
        return self.f
    def set_phase(self,p):
        self.p=p
        self.generate_signal()
    def get_phase(self):
        return self.p
    def get_signal(self):
        return self.signal
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def get_name(self):
        return self.name
