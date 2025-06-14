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
        
        self.refresh_tickets()
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
        
    def refresh_tickets(self):
        self.ticket_lb.delete(0, tk.END)
        for ticket in enumerate(globals.ticket_list):
            self.ticket_lb.insert(tk.END, str(ticket))
        
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
        # Customer Name
        self.customer_name_label = tk.Label(self.atwin, text = "Customer Name")
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(self.atwin)
        self.customer_name_entry.pack()
        # Open Checkbox
        self.open_frame = tk.Frame(self.atwin)
        self.open_frame.pack()
        self.open_label = tk.Label(self.open_frame, text = "Open?")
        self.open_label.grid(row = 0, column = 0)
        self.open_checkbox = tk.Checkbutton(self.open_frame)
        self.open_checkbox.select()
        self.open_checkbox.grid(row = 0, column = 1)
        # Available Services
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
        
        # Selected Services
        self.selectedframe = tk.Listbox(self.servframe, selectmode = 'single', width = 30)
        self.selectedframe.grid(row = 1, column = 1)
        # Service add function
        def add_to_selected(self, *args):
            selected_s_i = self.servbox_lb.curselection()
            for sindex in selected_s_i:
                sname = self.servbox_lb.get(sindex)
                self.selectedframe.insert(tk.END, sname)
            self.search_entry.focus()
            
        def remove_from_selected(self, *args):
            selected_s_i = self.selected_lb.curselection()
            for sindex in reversed(selected_s_i):
                self.selectedframe.delete(sindex)
            self.search_entry.focus()
        # Define Add Ticket Func
        def add_ticket(*args):
            try:
                techname = self.tech_name_entry.get()
                custname = self.customer_name_entry.get()
                servlist = []
                opn = self.open_checkbox.getboolean()
                selected_s_i = self.servbox_lb.curselection()
                for sindex in selected_s_i:
                    sname = self.servbox_lb.get(sindex)
                    service = globals.service_lookup(sname)
                    servlist.append(service)
                pass
                try:
                    with open(("tickets/" + globals.ticket_id_counter), 'x') as f:
                        f.write(techname + "\n")
                        f.write(custname + "\n")
                        f.write(str(opn) + "\n")
                        globals.service_list.append(Service(globals.ticket_id_counter, techname, servlist, opn, custname))
                        self.refresh_tickets()
                        
                except FileExistsError:
                    tk.messagebox.showerror(
                        title="Error",
                        message = "File already exists!"
                    )
            except ValueError:
                tk.messagebox.showerror(
                    title="Error: Invalid values provided",
                    message = "get outta here"
                )
        # Add Ticket Button for Add Ticket Window
        self.at_add_button = tk.Button(self.atwin, text = "Add Ticket", command = add_ticket)
        self.at_add_button.pack()
        
        
        

    