# Polyhedral dice roller
# By Jason VanDeventer

import tkinter as tk
from tkinter import ttk
import random


def roll_d2():
    d2_outcome = random.randint(1, 2)
    # xd2 = int(d2_quantity.get())
    d2_result.config(text=d2_outcome)


def roll_d4():
    d4_outcome = random.randint(1, 4)
    # xd4 = int(d4_quantity.get())
    d4_result.config(text=d4_outcome)


# Create window object
app = tk.Tk()
app.title('Dice Roller')
app.geometry('500x250')
app.iconbitmap('d20_icon.ico')

# Create d2 button, quantity selector, and result
d2_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d2_quantity.insert(0, 1)
d2_quantity.grid(column=2, row=1, padx=5, pady=10)
d2 = tk.Button(app, text="d2", command=roll_d2)
d2.grid(column=3, row=1)
d2_label = ttk.Label(app, text='Result:')
d2_label.grid(column=4, row=1)
d2_result = ttk.Label(app, text='', relief='sunken')
d2_result.grid(column=5, row=1, padx=5, sticky=tk.W)

# Create d4 button, quantity selector, and result
d4_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d4_quantity.insert(0, 1)
d4_quantity.grid(column=2, row=2, padx=5, pady=10)
d4 = tk.Button(app, text="d4", command=roll_d4)
d4.grid(column=3, row=2)
d4_label = ttk.Label(app, text='Result:')
d4_label.grid(column=4, row=2)
d4_result = ttk.Label(app, text='', relief='sunken')
d4_result.grid(column=5, row=2, padx=5, sticky=tk.W)

# Start program
app.mainloop()
