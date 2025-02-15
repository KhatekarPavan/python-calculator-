import tkinter as tk
from tkinter import font

def create_calculator():
    root = tk.Tk()
    root.title('Calculator')
    
    # Create display
    display_font = font.Font(size=14)
    entry = tk.Entry(root, font=display_font, justify='right', borderwidth=4)
    entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

    # Button configuration
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0)
    ]

    # Create buttons
    button_font = font.Font(size=12)
    for (text, row, col) in buttons:
        btn = tk.Button(root, text=text, font=button_font, padx=20, pady=10,
                       command=lambda t=text: button_click(t, entry))
        btn.grid(row=row, column=col, sticky='nsew')

    # Configure grid weights
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    return root

def button_click(char, entry):
    if char == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, 'Error')
    elif char == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

if __name__ == '__main__':
    calculator = create_calculator()
    calculator.mainloop()
