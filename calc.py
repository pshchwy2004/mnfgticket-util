import tkinter as tk
import service

class Price_Calculator:
    def __init__(self, service_list):
        self.slist = service_list
        self.cwin = tk.Tk()
        self.cwin.geometry("800x500")
        self.cwin.title("Price Calculator")
        self.calc_lb = tk.Listbox(self.cwin, selectmode = "multiple")
        self.calc_lb.pack(expand = True, fill = "both")
        for service in service_list:
            self.calc_lb.insert(tk.END, service.name)
            
        self.calc_button = tk.Button(self.cwin, text = "Ticket Management", font = ('Arial', 12), command = self.calculate_stuff_func)
        self.calc_button.pack()
        self.cwin.mainloop()
    def service_lookup(self, name):
        for service in self.slist:
            if (name == service.name):
                return service
        return service.Service("invalid", "invalid service", 0, 0, "invalid")
    def calculate_stuff_func(self):
        list = self.calc_lb.get(0)
        camt = self.calculate_stuff(list, True)
        namt = self.calculate_stuff(list, False)
        msg = "Cash Price: " + camt + "\nStandard Price: " + namt
        tk.messagebox.showinfo(
            title="Calculated Amount",
            # Get the text of each selected item and
            # show them separated by commas.
            message = msg
        )
        
    def calculate_stuff(self, sussylist, cash):
        amt = 0
        for service_name in sussylist:
            if (cash == True):
                amt += (self.service_lookup(service_name)).c
            else:
                amt += (self.service_lookup(service_name)).n
        return amt
    