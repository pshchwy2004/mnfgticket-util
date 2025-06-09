import globals
import tkinter as tk

class Service:
    def __init__(self, id, name, n_price, c_price, tags):
        self.id = id
        self.name = name
        self.n = n_price
        self.c = c_price
        self.tags = tags
        
    def __str__(self):
        return self.name
        
class Ticket:
    def __init__(self, techs, services):
        self.tech_list = techs
        self.services = services
    
    def add_to_services(self, service):
        self.services.append(service)
    
    def remove_service(self, service_name):
        for service in self.services:
            if (service.name == service_name):
                self.services.remove(service)
                break
    
class Service_Manager:
    def __init__(self):
        self.smwin = tk.Tk()
        self.smwin.geometry("800x500")
        self.smwin.title("Service Manager")
        self.smlb = tk.Listbox(self.smwin, selectmode = "multiple")
        self.smlb.pack(expand = True, fill = "both")
        self.refresh_selection()
        self.addserbutton = tk.Button(self.smwin, text = "Add Service", font = ('Arial', 12))
        self.addserbutton.pack()
        self.remserbutton = tk.Button(self.smwin, text = "Remove Service(s)", font = ('Arial', 12))
        self.remserbutton.pack()
        self.smwin.mainloop()
        pass
    def refresh_selection(self):
        for index, service in enumerate(globals.service_list):
            self.index_to_service = {}
            self.smlb.insert(tk.END, str(service))
            self.index_to_service[index] = service
    