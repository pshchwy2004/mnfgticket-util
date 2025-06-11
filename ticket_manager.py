from service import *
import tkinter as tk


class Ticket_Manager:
    def __init__(self, master):
        # Setting up toplevel
        self.tmwin = tk.Toplevel(master)
        self.tmwin.title("Ticket Manager")
        self.tmwin.geometry("800x500")
        
        self.ticket_lb = tk.Listbox(self.tmwin)
        self.ticket_lb.pack(fill = "x")
        for ticket in globals.ticket_list:
            self.ticket_lb.insert(tk.END, str(ticket))
        
        

    