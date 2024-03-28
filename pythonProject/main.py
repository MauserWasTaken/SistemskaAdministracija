from tkinter import *
from math import sqrt
from fractions import Fraction

# Function to perform addition
def add():
    try:
        result_value = float(num1.get()) + float(num2.get())
        result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to perform subtraction
def subtract():
    try:
        result_value = float(num1.get()) - float(num2.get())
        result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to perform multiplication
def multiply():
    try:
        result_value = float(num1.get()) * float(num2.get())
        result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to perform division
def divide():
    try:
        if float(num2.get()) == 0:
            result.set("Error: Division by zero")
        else:
            result_value = float(num1.get()) / float(num2.get())
            result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to perform exponentiation
def exponentiate():
    try:
        result_value = float(num1.get()) ** float(num2.get())
        result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to perform square root
def square_root():
    try:
        result_value = sqrt(float(num1.get()))
        result.set(format_result(result_value))
    except ValueError:
        result.set("Error")

# Function to format the result as a fraction if possible
def format_result(value):
    if display_as_fraction.get():
        fraction = Fraction(value).limit_denominator()
        if fraction.denominator == 1:
            return str(fraction.numerator)
        else:
            return str(fraction)
    else:
        return str(value)

# Function to toggle between displaying results as fractions or not
def toggle_fraction():
    display_as_fraction.set(not display_as_fraction.get())
    update_fraction_label()

# Function to update the fraction label
def update_fraction_label():
    if display_as_fraction.get():
        fraction_label.config(text="Fractions: On")
    else:
        fraction_label.config(text="Fractions: Off")

# Create main window
window = Tk()
window.title("Simple Calculator")

# Variables to store user input and result
num1 = StringVar()
num2 = StringVar()
result = StringVar()
display_as_fraction = BooleanVar(value=False)

# Frame for the input fields
input_frame = Frame(window)
input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entry widgets for user input
Label(input_frame, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
Entry(input_frame, textvariable=num1, width=10).grid(row=0, column=1, padx=5, pady=5)

Label(input_frame, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
Entry(input_frame, textvariable=num2, width=10).grid(row=1, column=1, padx=5, pady=5)

# Frame for the buttons
button_frame = Frame(window)
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Button to perform addition
Button(button_frame, text="Add", command=add, width=10).grid(row=0, column=0, padx=5, pady=5)

# Button to perform subtraction
Button(button_frame, text="Subtract", command=subtract, width=10).grid(row=0, column=1, padx=5, pady=5)

# Button to perform multiplication
Button(button_frame, text="Multiply", command=multiply, width=10).grid(row=0, column=2, padx=5, pady=5)

# Button to perform square root
Button(button_frame, text="Square Root", command=square_root, width=10).grid(row=1, column=2, padx=5, pady=5)

# Button to perform division
Button(button_frame, text="Divide", command=divide, width=10).grid(row=0, column=3, padx=5, pady=5)

# Button to perform exponentiation
Button(button_frame, text="Exponentiate", command=exponentiate, width=10).grid(row=0, column=4, padx=5, pady=5)

# Button to toggle displaying results as fractions or not
fraction_button = Button(button_frame, text="Fraction", command=toggle_fraction, width=10)
fraction_button.grid(row=1, column=3, padx=5, pady=5)

# Label to indicate the state of displaying fractions
fraction_label = Label(button_frame, text="Fractions: Off")
fraction_label.grid(row=2, column=3, padx=5, pady=5)

# Display result
Label(window, text="Result:").grid(row=2, column=0, padx=5, pady=5)
Label(window, textvariable=result).grid(row=2, column=1, padx=5, pady=5)

# Run the main event loop
window.mainloop()
