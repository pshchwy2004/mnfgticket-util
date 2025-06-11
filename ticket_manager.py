from service import *
import tkinter as tk

class Ticket_Manager:
    def __init__(self, master):
        self.tmwin = tk.Toplevel(master)
        self.ticket_search_var = tk.StringVar()
        self.ticket_search_entry = tk.Entry(self.tmwin, textvariable = self.ticket_search_var)
        self.ticket_search_entry.pack()
        self.ticket_search_var.trace_add('write', print("hi"))

    