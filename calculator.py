import tkinter as tk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root 
        self.root.title("Smart Calculator")
        self.memory = None
        self.history = []

        self.input_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.input_var, font=("Arial", 18), bd=10, insertwidth=2, width=24, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        Button = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('/', 4, 3),
            ('√', 5, 0), ('log', 5, 1), ('M', 5, 2), ('MC', 5, 3),
            ('C', 6, 0), ('=', 6, 1), ('H', 6, 2), ('Exit', 6, 3)
        ]

        for (text, row, col) in Button:
            tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 12),
                       command=lambda t=text: self.on_click(t)).grid(row=row, column=col)
            
    def on_click(self, char):
        if char == '=':
            self.evaluate()
        elif char == 'C':
            self.input_var.set('')
        elif char == 'Exit':
            self.root.quit()
        elif char == 'M':
            if self.memory is not None:
                self.input_var.set(str(self.memory))
        elif char == 'MC':
            self.memory = None
            messagebox.showinfo("Memory", "Memory Cleared.")
        elif char == '√':
            try:
                value = float(self.input_var.get())
                result = math.sqrt(value)
                self.input_var.set(result)
                self.store_history(f"√({value}) = {result}")
            except:
                self.input_var.set("Error")
        elif char == 'log':
            try:
                value = float(self.input_var.get())
                result = math.log10(value)
                self.input_var.set(result)
                self.store_history(f"log({value}) = {result}")
            except:
                self.input_var.set("Error")
        elif char == 'H':
            self.show_history()
        else:
            current = self.input_var.get()
            self.input_var.set(current + char)

    def evaluate(self):
        try:
            expr = self.input_var.get().replace('^', '**')
            result = eval(expr)
            self.input_var.set(result)
            self.memory = result
            self.store_history(f"{expr} = {result}")
        except:
            self.input_var.set("Error")

    def store_history(self, record):
        self.history.append(record)
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No calculations yet.")
        else:
            hist_str = "\n".join(self.history)
            messagebox.showinfo("Calculation History", hist_str)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()




