class Controller :
    def __init__(self,model,view):
        self.model=model
        self.view=view
        self.view.get_magnitude(model.get_name()).bind("<B1-Motion>",self.update_magnitude)
        self.view.get_frequency(model.get_name()).bind("<B1-Motion>",self.update_frequency)
        self.view.get_phase(model.get_name()).bind("<B1-Motion>",self.update_phase)
    def update_magnitude(self,event):
        print("update_magnitude")
        x=int(event.widget.get())
        self.model.set_magnitude(x)
        self.model.generate_signal()
    def update_frequency(self,event):
        print("update frequency")
        x=int(event.widget.get())
        self.model.set_frequency(x)
        self.model.generate_signal()
    def update_phase(self,event):
        print("update phase")
        x=int(event.widget.get())
        self.model.set_phase(x)
        self.model.generate_signal()
