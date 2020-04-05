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


def roll_d6():
    d6_outcome = random.randint(1, 6)
    # xd6 = int(d6_quantity.get())
    d6_result.config(text=d6_outcome)


def roll_d8():
    d8_outcome = random.randint(1, 8)
    # xd8 = int(d8_quantity.get())
    d8_result.config(text=d8_outcome)


def roll_d10():
    d10_outcome = random.randint(1, 10)
    # xd10 = int(d10_quantity.get())
    d10_result.config(text=d10_outcome)


def roll_dperc():
    dperc_outcome = random.randrange(0, 101, 10)
    # xdperc = int(dperc_quantity.get())
    dperc_result.config(text=dperc_outcome)


def roll_d12():
    d12_outcome = random.randint(1, 12)
    # xd12 = int(d12_quantity.get())
    d12_result.config(text=d12_outcome)


def roll_d20():
    d20_outcome = random.randint(1, 20)
    # xd20 = int(d20_quantity.get())
    d20_result.config(text=d20_outcome)


# Create window object
app = tk.Tk()
app.title('Dice Roller')
app.geometry('300x170')
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

# Create d6 button, quantity selector, and result
d6_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d6_quantity.insert(0, 1)
d6_quantity.grid(column=2, row=3, padx=5, pady=10)
d6 = tk.Button(app, text="d6", command=roll_d6)
d6.grid(column=3, row=3)
d6_label = ttk.Label(app, text='Result:')
d6_label.grid(column=4, row=3)
d6_result = ttk.Label(app, text='', relief='sunken')
d6_result.grid(column=5, row=3, padx=5, sticky=tk.W)

# Create d8 button, quantity selector, and result
d8_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d8_quantity.insert(0, 1)
d8_quantity.grid(column=2, row=4, padx=5, pady=10)
d8 = tk.Button(app, text="d8", command=roll_d8)
d8.grid(column=3, row=4)
d8_label = ttk.Label(app, text='Result:')
d8_label.grid(column=4, row=4)
d8_result = ttk.Label(app, text='', relief='sunken')
d8_result.grid(column=5, row=4, padx=5, sticky=tk.W)

# Create d10 button, quantity selector, and result
d10_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d10_quantity.insert(0, 1)
d10_quantity.grid(column=8, row=1, padx=5, pady=10)
d10 = tk.Button(app, text="d10", command=roll_d10)
d10.grid(column=9, row=1)
d10_label = ttk.Label(app, text='Result:')
d10_label.grid(column=10, row=1)
d10_result = ttk.Label(app, text='', relief='sunken')
d10_result.grid(column=11, row=1, padx=5, sticky=tk.W)

# Create dperc button, quantity selector, and result
dperc_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
dperc_quantity.insert(0, 1)
dperc_quantity.grid(column=8, row=2, padx=5, pady=10)
dperc = tk.Button(app, text="d%", command=roll_dperc)
dperc.grid(column=9, row=2)
dperc_label = ttk.Label(app, text='Result:')
dperc_label.grid(column=10, row=2)
dperc_result = ttk.Label(app, text='', relief='sunken')
dperc_result.grid(column=11, row=2, padx=5, sticky=tk.W)

# Create d12 button, quantity selector, and result
d12_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d12_quantity.insert(0, 1)
d12_quantity.grid(column=8, row=3, padx=5, pady=10)
d12 = tk.Button(app, text="d12", command=roll_d12)
d12.grid(column=9, row=3)
d12_label = ttk.Label(app, text='Result:')
d12_label.grid(column=10, row=3)
d12_result = ttk.Label(app, text='', relief='sunken')
d12_result.grid(column=11, row=3, padx=5, sticky=tk.W)

# Create d20 button, quantity selector, and result
d20_quantity = ttk.Spinbox(app, from_=1, to=100, width=5)
d20_quantity.insert(0, 1)
d20_quantity.grid(column=8, row=4, padx=5, pady=10)
d20 = tk.Button(app, text="d20", command=roll_d20)
d20.grid(column=9, row=4)
d20_label = ttk.Label(app, text='Result:')
d20_label.grid(column=10, row=4)
d20_result = ttk.Label(app, text='', relief='sunken')
d20_result.grid(column=11, row=4, padx=5, sticky=tk.W)

# Start program
app.mainloop()
