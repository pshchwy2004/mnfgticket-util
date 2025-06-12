import tkinter as tk
from tkinter import messagebox
from service import *
import globals

class Price_Calculator:
    def __init__(self, master):
        # Price Index- to be updated upon add or removal
        self.cp = 0
        self.np = 0
        # Window Creation
        self.cwin = tk.Toplevel(master)
        self.cwin.title("Price Calculator")
        
        # Left Side Frame
        self.serv_frame = tk.Frame(self.cwin)
        self.serv_frame.grid(row = 0, column = 0)
        # Search Bar- place before Service Listbox to place above it
        self.searchbar_frame = tk.Frame(self.serv_frame)
        self.searchbar_frame.grid(row = 0, column = 0)
        self.search_label = tk.Label(self.searchbar_frame, text = "Search: ")
        self.search_label.grid(row = 0, column = 0)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.searchbar_frame, textvariable=self.search_var)
        self.search_entry.grid(row = 0, column = 1)
        self.search_entry.focus()
        self.search_entry.bind("<Return>", self.update_serv_list)
        self.search_var.trace_add('write', self.update_serv_list)
        
        # Service Listbox (aka Servbox)
        self.servbox_lb = tk.Listbox(self.serv_frame, selectmode = 'single', width = 30)
        self.servbox_lb.grid(row = 1, column = 0)
        self.servbox_lb.bind("<Double-Button-1>", self.add_to_selected)
        # To update the Servbox
        self.update_serv_list()
        
        # Selected Frame (right side)
        self.selected_frame = tk.Frame(self.cwin)
        self.selected_frame.grid(row = 0, column = 2)
        # Selected Listbox
        self.selected_label = tk.Label(self.selected_frame, text = "Selected Items")
        self.selected_label.grid(row = 0, column = 0)
        self.selected_lb = tk.Listbox(self.selected_frame, selectmode = 'single', width = 30)
        self.selected_lb.grid(row = 1, column = 0)
        self.selected_lb.bind("<Double-Button-1>", self.remove_from_selected)
        
        # Button Frame
        self.button_frame = tk.Frame(self.cwin)
        self.button_frame.grid(row = 0, column = 1)
        # Buttons
        self.calc_button = tk.Button(self.button_frame, text = "Add to Order", font = ('Arial', 12), command = self.add_to_selected)
        self.calc_button.pack()
        self.rem_button = tk.Button(self.button_frame, text = "Remove from Order", font = ('Arial', 12), command = self.remove_from_selected)
        self.rem_button.pack()
        self.calc_clearbutton = tk.Button(self.button_frame, text = "Clear Selection", font = ('Arial', 12), command = self.clear_selected)
        self.calc_clearbutton.pack()
        self.calc_closebutton = tk.Button(self.button_frame, text = "Close", font = ('Arial', 12), command = self.cwin.destroy)
        self.calc_closebutton.pack()
        
        
        # Prices
        self.normpricelabel = tk.Label(self.button_frame, text="Normal Price: " + str(self.np))
        self.normpricelabel.pack()
        self.cashpricelabel = tk.Label(self.button_frame, text="Cash Price: " + str(self.cp))
        self.cashpricelabel.pack()
        
        
    
    def update_serv_list(self, *args):
        search_term = self.search_entry.get()
        self.servbox_lb.delete(0, tk.END)
        for service in globals.service_list:
            if (search_term.lower() in (service.tags.lower())) | (search_term.lower() in service.name):
                self.servbox_lb.insert(tk.END, str(service))
           
    
    def add_to_selected(self, *args):
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
        
    def remove_from_selected(self, *args):
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
    
    def clear_selected(self, *args):
        self.selected_lb.delete(0, tk.END)
        self.np = 0
        self.cp = 0
        self.normpricelabel.config(text = "Normal Price: " + str(self.np))
        self.cashpricelabel.config(text = "Cash Price: " + str(self.cp))
        
    # Looks up the service by name and returns the Service object instance and None if unable to lookup
    def service_lookup(self, name):
        for service in globals.service_list:
            if (name == service.name):
                return service
        return None