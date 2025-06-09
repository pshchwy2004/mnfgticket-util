import tkinter as tk
from tkinter import messagebox
from service import *
import globals

class Price_Calculator:
    def __init__(self):
        self.cwin = tk.Tk()
        self.cwin.geometry("800x500")
        self.cwin.title("Price Calculator")
        self.calc_lb = tk.Listbox(self.cwin, selectmode = "multiple")
        self.calc_lb.pack(expand = True, fill = "both")
        self.index_to_service = {}
        for index, service in enumerate(globals.service_list):
            self.calc_lb.insert(tk.END, str(service))
            self.index_to_service[index] = service
        self.calc_button = tk.Button(self.cwin, text = "Calculate Prices", font = ('Arial', 12), command = self.calculate_stuff_func)
        self.calc_button.pack()
        self.calc_closebutton = tk.Button(self.cwin, text = "Close", font = ('Arial', 12), command = self.cwin.destroy)
        self.calc_closebutton.pack()
        self.cwin.mainloop()
    def service_lookup(self, name):
        for service in globals.service_list:
            if (name == service.name):
                return service
        return Service("invalid", "invalid service", 0, 0, "invalid")
    def calculate_stuff_func(self):
        selected_s_i = self.calc_lb.curselection()
        selected_s = [self.index_to_service[i] for i in selected_s_i]
        
        namt, camt = self.calculate_stuff(selected_s)
        msg = "Cash Price: " + str(camt) + "\nStandard Price: " + str(namt)
        tk.messagebox.showinfo(
            title="Calculated Amount",
            message = msg
        )
        
    def calculate_stuff(self, sussylist):
        namt = 0
        camt = 0
        for service in sussylist:
            camt += service.c
            namt += service.n
        return namt, camt
    