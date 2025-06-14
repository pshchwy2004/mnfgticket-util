from service import *
import tkinter as tk
from pathlib import *
import sys
from calc import Price_Calculator
from ticket_manager import Ticket_Manager
import globals

def service_lookup_by_id(id):
    for service in globals.service_list:
        if service.id == id:
            return service
    return None

def init():
    print("Initializing")
    service_directory = Path("services/")
    if not service_directory.exists():
        print("Services directory does not exist. Creating directory...")
        try:
            service_directory.mkdir(parents = True, exist_ok = True)
            print("Services directory successfully created.")
        except PermissionError:
            print("Permission denied to create directory.")
            i = input("Press enter to exit:")
            sys.exit(1)
    for file in service_directory.iterdir():
        with file.open('r') as f:
            id = file.name
            name = f.readline().strip()
            np = int(f.readline().strip())
            cp = int(f.readline().strip())
            tag = (f.readline().strip()) + name
            globals.service_list.append(Service(id, name, np, cp, tag))
    print("All services loaded.")
    ticket_directory = Path("tickets/")
    if not ticket_directory.exists():
        print("Tickets directory does not exist. Creating directory...")
        try:
            ticket_directory.mkdir(parents = True, exist_ok = True)
            print("Tickets directory successfully created.")
        except PermissionError:
            print("Permission denied to create directory.")
            i = input("Press enter to exit:")
            sys.exit(1)
    for file in ticket_directory.iterdir():
        with file.open('r') as f:
            id = globals.ticket_id_counter
            tech = f.readline().strip()
            customer = f.readline().strip()
            open = bool(f.readline().strip())
            t_services = []
            for line in file:
                serv = service_lookup_by_id(line.strip())
                t_services.append(serv)
            globals.ticket_list.append(Ticket(id, tech, open, t_services, customer))
        globals.ticket_id_counter = globals.ticket_id_counter + 1
    print("All tickets loaded.")
    print("Opening window...")
    
def exit_app():
    root.destroy()
    


init()
root = tk.Tk()
root.geometry("800x500")
root.title("Service Management Utility")
button_frame = tk.Frame(root)
button_frame.pack(side = 'left')

# Toplevel defs

def calc_window():
    pc = Price_Calculator(root)

def sm_window():
    sm = Service_Manager(root)
    
def tm_window():
    tm = Ticket_Manager(root)

sm_button = tk.Button(button_frame, text = "Service Management", font = ('Arial', 12), command = sm_window)
sm_button.pack(padx = 5)
tm_button = tk.Button(button_frame, text = "Ticket Management", font = ('Arial', 12), command = tm_window)
tm_button.pack(padx = 5)
cl_button = tk.Button(button_frame, text = "Price Calculations", font = ('Arial', 12), command = calc_window)
cl_button.pack(padx = 5)
ex_button = tk.Button(button_frame, text = "Exit", font = ('Arial', 12), command = exit_app)
ex_button.pack(padx = 5)
label = tk.Label(root, text = "choose a thing", font = ('Arial', 18))
label.pack(side = 'top')
root.mainloop()
