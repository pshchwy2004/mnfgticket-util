from service import *
import tkinter as tk
from pathlib import *
import sys
from calc import Price_Calculator

service_list = []

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
            tag = f.readline().strip()
            service_list.append(Service(id, name, np, cp, tag))
            print("Added", name)
    
def exit_app():
    root.destroy()
    
def calc_window():
    pc = Price_Calculator(service_list)
    

init()
root = tk.Tk()
root.geometry("800x500")
root.title("Service Management Utility")
button_frame = tk.Frame(root)
button_frame.pack(side = 'left')

sm_button = tk.Button(button_frame, text = "Service Management", font = ('Arial', 12))
sm_button.pack(padx = 5)
tm_button = tk.Button(button_frame, text = "Ticket Management", font = ('Arial', 12))
tm_button.pack(padx = 5)
cl_button = tk.Button(button_frame, text = "Price Calculations", font = ('Arial', 12), command = calc_window)
cl_button.pack(padx = 5)
ex_button = tk.Button(button_frame, text = "Exit", font = ('Arial', 12), command = exit_app)
ex_button.pack(padx = 5)
label = tk.Label(root, text = "choose a thing", font = ('Arial', 18))
label.pack(side = 'top')
root.mainloop()
