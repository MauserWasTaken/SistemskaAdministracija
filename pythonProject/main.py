from tkinter import *

# Function to perform addition
def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to perform subtraction
def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Error")

# Function to perform multiplication
def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Error")

# Create main window
window = Tk()
window.title("Simple Calculator")

# Variables to store user input and result
num1 = StringVar()
num2 = StringVar()
result = StringVar()

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

# Display result
Label(window, text="Result:").grid(row=2, column=0, padx=5, pady=5)
Label(window, textvariable=result).grid(row=2, column=1, padx=5, pady=5)

# Run the main event loop
window.mainloop()
