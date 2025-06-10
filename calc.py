import tkinter as tk
from tkinter import messagebox
from service import *
import globals

class Price_Calculator:
    def __init__(self):
        self.cp = 0
        self.np = 0
        self.cwin = tk.Tk()
        self.cwin.geometry("800x500")
        self.cwin.title("Price Calculator")
        self.calc_lb = tk.Listbox(self.cwin, selectmode = 'multiple')
        self.calc_lb.pack(expand = True, side = 'left', padx = 10, pady = 10, fill = 'y')
        self.index_to_service = {}
        for index, service in enumerate(globals.service_list):
            self.calc_lb.insert(tk.END, str(service))
            self.index_to_service[index] = service
            
        self.selected_lb = tk.Listbox(self.cwin, selectmode = 'multiple')
        self.selected_lb.pack(expand = True, side = 'right', padx = 10, pady = 10, fill = 'y')
        self.calc_button = tk.Button(self.cwin, text = "Add to Order", font = ('Arial', 12), command = self.add_to_selected)
        self.calc_button.pack()
        self.rem_button = tk.Button(self.cwin, text = "Remove from Order", font = ('Arial', 12), command = self.remove_from_selected)
        self.rem_button.pack()
        self.calc_closebutton = tk.Button(self.cwin, text = "Close", font = ('Arial', 12), command = self.cwin.destroy)
        self.calc_closebutton.pack()
        self.normpricelabel = tk.Label(self.cwin, text="Normal Price: " + str(self.np))
        self.normpricelabel.pack()
        self.cashpricelabel = tk.Label(self.cwin, text="Cash Price: " + str(self.cp))
        self.cashpricelabel.pack()
        
        self.cwin.mainloop()
    def service_lookup(self, name):
        for service in globals.service_list:
            if (name == service.name):
                return service
        return None
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
    
    def add_to_selected(self):
        selected_s_i = self.calc_lb.curselection()
        selected_s = [self.index_to_service[i] for i in selected_s_i]
        for service in selected_s:
            self.selected_lb.insert(tk.END, str(service))
            self.cp += service.c
            self.np += service.n
        self.normpricelabel.config(text = "Normal Price: " + str(self.np))
        self.cashpricelabel.config(text = "Cash Price: " + str(self.cp))
        
    def remove_from_selected(self):
        selected_s_i = self.selected_lb.curselection()
        for sindex in selected_s_i:
            sname = self.selected_lb.get(sindex)
            service = self.service_lookup(sname)
            if service != None:
                self.np -= service.n
                self.cp -= service.c
        for sindex in reversed(selected_s_i):
            self.selected_lb.delete(sindex)
        self.normpricelabel.config(text = "Normal Price: " + str(self.np))
        self.cashpricelabel.config(text = "Cash Price: " + str(self.cp))
        