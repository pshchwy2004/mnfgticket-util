import tkinter as tk
import service

class Price_Calculator:
    def calculate_stuff(sussylist, cash):
        amt = 0
        for service in sussylist:
            if (cash == True):
                amt += service.c
            else:
                amt += service.n
        return amt