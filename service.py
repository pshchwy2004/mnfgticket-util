import globals
import tkinter as tk
from pathlib import *

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
        
    def __str__(self):
        return "Tech(s): " + ",".join(self.tech_list) + ", Services: "
        pass
    
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
        self.index_to_service = {}
        self.refresh_selection()
        self.addserbutton = tk.Button(self.smwin, text = "Add Service", font = ('Arial', 12), command = self.addser_window)
        self.addserbutton.pack()
        self.remserbutton = tk.Button(self.smwin, text = "Remove Service(s)", font = ('Arial', 12), command = self.remove_services)
        self.remserbutton.pack()
        self.closesmbutton = tk.Button(self.smwin, text = "Close", font = ('Arial', 12), command = self.smwin.destroy)
        self.closesmbutton.pack()
        self.smwin.mainloop()
        
    def remove_services(self):
        selected_s_i = self.smlb.curselection()
        if not selected_s_i:
            tk.messagebox.showerror(
                title="Error",
                message = "Nothing selected."
            )
        else:
            response = tk.messagebox.askyesno("Confirm removal", "Are you sure you want to delete these services?")
            if response:
                selected_s = [self.index_to_service[i] for i in selected_s_i]
                for service in selected_s:
                    try:
                        globals.service_list.remove(service)
                        directory = Path("services/" + service.id)
                        try:
                            directory.unlink()
                        except FileNotFoundError:
                            pass
                    except ValueError:
                        pass
                self.refresh_selection()
                tk.messagebox.showinfo(
                    title="Successful operation",
                    message = "Services deleted."
                )
            else:
                # Do nothing.
                pass
        
            
        
    def refresh_selection(self):
        self.smlb.delete(0, tk.END)
        self.index_to_service = {}
        for index, service in enumerate(globals.service_list):
            self.smlb.insert(tk.END, str(service))
            self.index_to_service[index] = service

    def addser_window(self):
        self.aswin = tk.Tk()
        self.aswin.title("Add Service")
        self.asidl = tk.Label(self.aswin, text = "ID")
        self.asidl.pack()
        self.aside = tk.Entry(self.aswin)
        self.aside.pack()
        self.asnamel = tk.Label(self.aswin, text = "Name")
        self.asnamel.pack()
        self.asnamee = tk.Entry(self.aswin)
        self.asnamee.pack()
        self.asnpl = tk.Label(self.aswin, text = "Normal Price")
        self.asnpl.pack()
        self.asnpe = tk.Entry(self.aswin)
        self.asnpe.pack()
        self.ascpl = tk.Label(self.aswin, text = "Cash Price")
        self.ascpl.pack()
        self.ascpe = tk.Entry(self.aswin)
        self.ascpe.pack()
        self.astagl = tk.Label(self.aswin, text = "Tags (to identify the service easier in searches)")
        self.astagl.pack()
        self.astage = tk.Text(self.aswin, height = 3)
        self.astage.pack()
        def add_service():
            try:
                id = self.aside.get()
                name = self.asnamee.get()
                np = int(self.asnpe.get())
                cp = int(self.ascpe.get())
                tags = self.astage.get("1.0", "end-1c")
                try:
                    with open(("services/" + id), 'x') as f:
                        f.write(name + "\n")
                        f.write(str(np) + "\n")
                        f.write(str(cp) + "\n")
                        f.write(tags)
                        globals.service_list.append(Service(id, name, np, cp, tags))
                        self.refresh_selection()
                        tk.messagebox.showinfo(
                            title="Service added",
                            message = "ID: " + id + "\n" + "Name: " + name + "\n" + "Normal Price: " + str(np) + "\n" + "Cash Price: " + str(cp) + "\n" + "Tags: " + tags + "\n"
                        )
                except FileExistsError:
                    tk.messagebox.showerror(
                        title="Error",
                        message = "File already exists!"
                    )
            except ValueError:
                tk.messagebox.showerror(
                    title="Error: Invalid values provided",
                    message = "normal and cash prices must be integer values!"
                )
        self.addbutton = tk.Button(self.aswin, text = "Add Service", font = ('Arial', 12), command = add_service)
        self.addbutton.pack()
        self.cancelbutton = tk.Button(self.aswin, text = "Close", font = ('Arial', 12), command = self.aswin.destroy)
        self.cancelbutton.pack()