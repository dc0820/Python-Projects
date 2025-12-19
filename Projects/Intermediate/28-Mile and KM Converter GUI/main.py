import tkinter

MILE_PER_KM = 1.60934
KM_PER_MILE = 0.621371
DEFAULT_VALUE = 0
DEFAULT_PAD = {"padx":10, "pady":10}

# Make window
window = tkinter.Tk()
window.title("Mile/Km Converter")
window.minsize(width=300, height=100)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# -------------------------------- #
def update_labels():
    """Instantly switch the labels when radio button changes."""
    if convert_state.get() == 1:
        converter_label.configure(text="Miles")
        convert_text.configure(text="Km")
    else:
        converter_label.configure(text="Km")
        convert_text.configure(text="Miles")

def convert_distance():
    """Conversion Km/Miles"""
    if convert_state.get() == 1:
        miles = float(input_num.get())
        km = round(miles * MILE_PER_KM, 2)
        convert_to.configure(text=f"{km}", **DEFAULT_PAD)

    elif convert_state.get() == 2:
        km = float(input_num.get())
        miles = round(km * KM_PER_MILE, 2)
        convert_to.configure(text=f"{miles}", **DEFAULT_PAD)

# Calculation button
calc_button = tkinter.Button(text="Calculate", command=convert_distance)
calc_button.grid(column=1, row=2, **DEFAULT_PAD)

# Text input
input_num = tkinter.Entry(width=10)
input_num.grid(column=1, row=0, **DEFAULT_PAD)

# Label for input type
converter_label = tkinter.Label(text="Miles")
converter_label.grid(column=2, row=0, **DEFAULT_PAD)

# "is equal to"
is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1, sticky="e")

# Result label
convert_to = tkinter.Label(text=DEFAULT_VALUE)
convert_to.grid(column=1, row=1, **DEFAULT_PAD)

# Output type (Km or Miles)
convert_text = tkinter.Label(text="Km")
convert_text.grid(column=2, row=1, **DEFAULT_PAD)

# Radio buttons
convert_state = tkinter.IntVar(value=1)  # default selection
km_button = tkinter.Radiobutton(text="Miles to Km", value=1, variable=convert_state, command=update_labels)
mile_button = tkinter.Radiobutton(text="Km to Miles", value=2, variable=convert_state, command=update_labels)

km_button.grid(column=0, row=2, sticky="e")
mile_button.grid(column=2, row=2, **DEFAULT_PAD)

window.mainloop()
