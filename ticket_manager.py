from service import *
import tkinter as tk


class Ticket_Manager:
    def __init__(self, master):
        # Setting up toplevel
        self.tmwin = tk.Toplevel(master)
        self.tmwin.title("Ticket Manager")
        self.tmwin.geometry("800x500")
        
        # Tickets
        self.ticket_lb = tk.Listbox(self.tmwin, selectmode = "single")
        self.ticket_lb.pack(fill = "x")
        for ticket in globals.ticket_list:
            self.ticket_lb.insert(tk.END, str(ticket))
        
        # Add Ticket Button
        self.add_ticket_button = tk.Button(self.tmwin, text = "Add Ticket", font = ('Arial', 12), command = self.addtick_window)
        self.add_ticket_button.pack()
        
        # Edit Ticket Button
        self.edit_ticket_button = tk.Button(self.tmwin, text = "Edit Ticket", font = ('Arial', 12))
        self.edit_ticket_button.pack()
        
        # Close Button
        self.close_button = tk.Button(self.tmwin, text = "Close", font = ('Arial', 12), command = self.tmwin.destroy)
        self.close_button.pack()
        
    def addtick_window(self):
        def update_serv_list(*args):
            search_term = self.search_entry.get()
            self.servbox_lb.delete(0, tk.END)
            for service in globals.service_list:
                if (search_term.lower() in (service.tags.lower())) | (search_term.lower() in service.name):
                    self.servbox_lb.insert(tk.END, str(service))
        self.atwin = tk.Toplevel(self.tmwin)
        self.atwin.title("Add Ticket")
        # Technician Name
        self.tech_name_label = tk.Label(self.atwin, text = "Technician Name")
        self.tech_name_label.pack()
        self.tech_name_entry = tk.Entry(self.atwin)
        self.tech_name_entry.pack()
        self.tech_name_entry.focus()
        # Services Performed
        self.servframe = tk.Frame(self.atwin)
        self.servframe.pack()
        # Search Bar- place before Service Listbox to place above it
        self.searchframe = tk.Frame(self.servframe)
        self.searchframe.grid(row = 0, column = 0)
        self.search_var = tk.StringVar()
        self.search_label = tk.Label(self.searchframe, text = "Search: ")
        self.search_label.grid(row = 0, column = 0)
        self.search_entry = tk.Entry(self.searchframe, textvariable=self.search_var)
        self.search_entry.grid(row = 0, column = 1)
        self.search_entry.bind("<Return>", update_serv_list)
        self.search_var.trace_add('write', update_serv_list)
        # Service Listbox (aka Servbox)
        self.servbox_lb = tk.Listbox(self.servframe, selectmode = 'single', width = 30)
        self.servbox_lb.grid(row = 1, column = 0)
        # To update the Servbox
        update_serv_list()
        

    