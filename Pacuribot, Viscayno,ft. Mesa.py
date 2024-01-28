import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.calculation = ""

        # Text field to display the current calculation
        self.text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=4)
        self.text_result.config(bg="#20B2AA")  # Set the background color to light sea green

        # Buttons for digits (0-9), basic operators, parentheses, clear, and equals
        buttons = [
            '(', ')', 'C', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', '⌫'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(row_val, col_val, button)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, row, column, text, command=None):
        button = tk.Button(root, text=text, command=lambda: self.button_click(text), width=4, font=("Arial", 14))
        button.grid(row=row, column=column)

    def button_click(self, symbol):
        if symbol == "=":
            self.evaluate_calculation()
        elif symbol == "C":
            self.clear_field()
        elif symbol == '⌫':
            self.backspace()
        else:
            self.add_to_calculation(symbol)

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)

    def evaluate_calculation(self):
        if self.calculation:
            try:
                self.calculation = str(eval(self.calculation))
                self.text_result.delete(1.0, "end")
                self.text_result.insert(1.0, self.calculation)
            except:
                self.clear_field()
                self.text_result.insert(1.0, "Error!")
        else:
            self.clear_field()

    def clear_field(self):
        self.calculation = ""
        self.text_result.delete(1.0, "end")

    def backspace(self):
        self.calculation = self.calculation[:-1]
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.calculation)


# Create GUI window
root = tk.Tk()
root.geometry("280x300")
root.title("Calculator G?")

# Set the background color of the main window
root.configure(bg="#808080")

# Create Calculator object
calculator = Calculator(root)

# Start the GUI main loop
root.mainloop()
