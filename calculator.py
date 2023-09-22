import tkinter as tk


def add_digit(digit):
    current = display_var.get()

    display_var.set(current + str(digit))


def clear_display():
    display_var.set("")


def calculate():
    try:

        result = eval(display_var.get())

        display_var.set(result)



    except Exception:

        display_var.set("Error")

        # Clear the error message after 1 second

        window.after(1000, clear_display)


def cm_to_in():
    try:

        cm_value = float(display_var.get())

        inches = cm_value / 2.54

        display_var.set(f"{inches:.2f}")



    except ValueError:

        display_var.set("Error")

        # Clear the error message after 1 second

        window.after(1000, clear_display)


def in_to_cm():
    try:

        in_value = float(display_var.get())

        centimeters = in_value * 2.54

        display_var.set(f"{centimeters:.2f}")



    except ValueError:

        display_var.set("Error")

        # Clear the error message after 1 second

        window.after(1000, clear_display)


# Create the main window


window = tk.Tk()

window.title("Accounts Department Calculator")

window.configure(bg="light blue")

# Create the display entry


display_var = tk.StringVar()

display_entry = tk.Entry(window, textvariable=display_var, font=("Arial", 20), justify="right")

display_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nesw")

# Define button labels and their corresponding positions


button_labels = [

    ["Clear", "Cm", "In", "*"],

    ["7", "8", "9", "/"],

    ["4", "5", "6", "-"],

    ["1", "2", "3", "+"],

    [".", "0", "="]

]

# Create buttons based on the provided arrangement


for row, labels in enumerate(button_labels):

    for col, label in enumerate(labels):

        button = tk.Button(window, text=label, font=("Arial", 16), padx=20, pady=20, bg="white", fg="black")

        if label == "=":

            button.config(command=calculate, width=10)

            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nesw")



        elif label == "Clear":

            button.config(command=clear_display, width=10)

            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nesw")



        elif label == "Cm":

            button.config(command=cm_to_in, width=10)

            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nesw")



        elif label == "In":

            button.config(command=in_to_cm, width=10)

            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nesw")



        else:

            button.config(command=lambda digit=label: add_digit(digit), width=10)

            button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nesw")

# Create a white border around the calculator


window.grid_rowconfigure(0, minsize=20)

window.grid_rowconfigure(6, minsize=20)

window.grid_columnconfigure(0, minsize=20)

window.grid_columnconfigure(5, minsize=20)

# Configure the column and row weights to make the display entry expandable


for i in range(5):
    window.grid_columnconfigure(i, weight=1)

# Run the main event loop


window.mainloop()
