import tkinter as tk

def bigfunky(*args):
    print("big funky")
    
class Stupid_Class:
    
    def __init__(self, master):
        self.swin = tk.Toplevel(master)
        self.ss = tk.StringVar()
        self.entr = tk.Entry(self.swin, textvariable = self.ss)
        self.entr.pack()
        self.ss.trace_add('write', self.bigfunky2)
        
    def bigfunky2(*args):
        print("big funky 2")
    
    
        


win = tk.Tk()
s = Stupid_Class(win)
searv = tk.StringVar()
entr = tk.Entry(win, textvariable = searv)
entr.pack()
searv.trace_add('write', bigfunky)
win.mainloop()

