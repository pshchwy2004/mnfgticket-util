import tkinter as tk
from tkinter import messagebox
from service import *
import globals

class Price_Calculator:
    def __init__(self):
        # Price Index- to be updated upon add or removal
        self.cp = 0
        self.np = 0
        # Window Creation
        self.cwin = tk.Tk()
        self.cwin.geometry("800x500")
        self.cwin.title("Price Calculator")
        
        # Left Side Frame
        self.serv_frame = tk.Frame(self.cwin)
        self.serv_frame.pack(side = 'left', fill = 'y')
        # Search Bar- place before Service Listbox to place above it
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.serv_frame, textvariable=self.search_var)
        self.search_entry.pack()
        self.search_entry.focus()
        self.search_entry.bind("<Return>", self.update_serv_list)
       
        
        # Button to manually initiate search since this stupid search bar won't work and no AI is willing nor able to help me
        # self.search_button = tk.Button(self.serv_frame, text = "Search", font = ('Arial', 12), command = self.update_serv_list)
        # self.search_button.pack()
        
        # Service Listbox (aka Servbox)
        self.servbox_lb = tk.Listbox(self.serv_frame, selectmode = 'multiple', width = 30)
        self.servbox_lb.pack(expand = True, padx = 5, pady = 10, fill = 'y')
        # To update the Servbox
        self.update_serv_list()
        
        # Selected Listbox
        self.selected_lb = tk.Listbox(self.cwin, selectmode = 'multiple')
        self.selected_lb.pack(expand = True, side = 'right', padx = 5, pady = 10, fill = 'y')
        
        # Buttons
        self.calc_button = tk.Button(self.cwin, text = "Add to Order", font = ('Arial', 12), command = self.add_to_selected)
        self.calc_button.pack()
        self.rem_button = tk.Button(self.cwin, text = "Remove from Order", font = ('Arial', 12), command = self.remove_from_selected)
        self.rem_button.pack()
        self.calc_closebutton = tk.Button(self.cwin, text = "Close", font = ('Arial', 12), command = self.cwin.destroy)
        self.calc_closebutton.pack()
        
        # Prices
        self.normpricelabel = tk.Label(self.cwin, text="Normal Price: " + str(self.np))
        self.normpricelabel.pack()
        self.cashpricelabel = tk.Label(self.cwin, text="Cash Price: " + str(self.cp))
        self.cashpricelabel.pack()
        self.cwin.mainloop()
    
    def update_serv_list(self, *args):
        search_term = self.search_entry.get()
        self.servbox_lb.delete(0, tk.END)
        for service in globals.service_list:
            if search_term.lower() in str(service).lower():
                self.servbox_lb.insert(tk.END, str(service))
           
    
    def add_to_selected(self):
        selected_s_i = self.servbox_lb.curselection()
        for sindex in selected_s_i:
            sname = self.servbox_lb.get(sindex)
            service = self.service_lookup(sname)
            if service != None:
                self.np += service.n
                self.cp += service.c
            self.selected_lb.insert(tk.END, sname)
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
    
    # Looks up the service by name and returns the Service object instance and None if unable to lookup
    def service_lookup(self, name):
        for service in globals.service_list:
            if (name == service.name):
                return service
        return None