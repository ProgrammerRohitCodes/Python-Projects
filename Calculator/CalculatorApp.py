import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#3a3a3a")

placeholder = "Enter your values here"
display_var = tk.StringVar(value=placeholder)

display = tk.Entry(root, font=("Helvetica", 14), bd=1, relief="sunken", justify="center",
                   bg="#36454F", fg="#a3a3a3", textvariable=display_var, state="readonly")
display.pack(pady=(20, 0), padx=10, fill="x")

display.bind("<FocusIn>", lambda e: None)
display.bind("<Key>", lambda e: "break")

button_frame = tk.Frame(root, bg="#3a3a3a")
button_frame.pack(pady=20)

button_style = {
    "font": ("Segoe UI", 8, "bold"),
    "fg": "white",
    "width": 3,
    "height": 3,
    "bd": 3,
    "relief": "groove"
}

num_color = "#2f4f4f"
op_color = "#006d77"
clear_color = "#b00020"

btn_1 = tk.Button(button_frame, text="1", bg=num_color, **button_style)
btn_2 = tk.Button(button_frame, text="2", bg=num_color, **button_style)
btn_3 = tk.Button(button_frame, text="3", bg=num_color, **button_style)
btn_4 = tk.Button(button_frame, text="4", bg=num_color, **button_style)
btn_5 = tk.Button(button_frame, text="5", bg=num_color, **button_style)
btn_6 = tk.Button(button_frame, text="6", bg=num_color, **button_style)
btn_7 = tk.Button(button_frame, text="7", bg=num_color, **button_style)
btn_8 = tk.Button(button_frame, text="8", bg=num_color, **button_style)
btn_9 = tk.Button(button_frame, text="9", bg=num_color, **button_style)
btn_0 = tk.Button(button_frame, text="0", bg=num_color, **button_style)
btn_plus = tk.Button(button_frame, text="+", bg=op_color, **button_style)
btn_minus = tk.Button(button_frame, text="-", bg=op_color, **button_style)
btn_divide = tk.Button(button_frame, text="÷", bg=op_color, **button_style)
btn_multiply = tk.Button(button_frame, text="×", bg=op_color, **button_style)
btn_clear = tk.Button(button_frame, text="Clear", bg=clear_color, **button_style)
btn_equal = tk.Button(button_frame, text="=", bg=op_color, **button_style)

btn_1.grid(row=0, column=0, padx=5, pady=5)
btn_2.grid(row=0, column=1, padx=5, pady=5)
btn_3.grid(row=0, column=2, padx=5, pady=5)
btn_4.grid(row=1, column=0, padx=5, pady=5)
btn_5.grid(row=1, column=1, padx=5, pady=5)
btn_6.grid(row=1, column=2, padx=5, pady=5)
btn_7.grid(row=2, column=0, padx=5, pady=5)
btn_8.grid(row=2, column=1, padx=5, pady=5)
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_0.grid(row=3, column=1, padx=5, pady=5)
btn_plus.grid(row=0, column=3, padx=5, pady=5)
btn_minus.grid(row=1, column=3, padx=5, pady=5)
btn_divide.grid(row=2, column=3, padx=5, pady=5)
btn_multiply.grid(row=3, column=3, padx=5, pady=5)
btn_clear.grid(row=3, column=0, padx=5, pady=5)
btn_equal.grid(row=3, column=2, padx=5, pady=5)

def button_click(value):
    current_text = display_var.get()
    if current_text == "Invalid Expression":
    	current_text = ""
		
    if current_text == placeholder:
        current_text = ""
    new_text = current_text + value
    display_var.set(new_text)

btn_0.config(command=lambda: button_click("0"))
btn_1.config(command=lambda: button_click("1"))
btn_2.config(command=lambda: button_click("2"))
btn_3.config(command=lambda: button_click("3"))
btn_4.config(command=lambda: button_click("4"))
btn_5.config(command=lambda: button_click("5"))
btn_6.config(command=lambda: button_click("6"))
btn_7.config(command=lambda: button_click("7"))
btn_8.config(command=lambda: button_click("8"))
btn_9.config(command=lambda: button_click("9"))

btn_plus.config(command=lambda: button_click("+"))
btn_minus.config(command=lambda: button_click("-"))
btn_multiply.config(command=lambda: button_click("×"))
btn_divide.config(command=lambda: button_click("÷"))
btn_clear.config(command=lambda: display_var.set(placeholder))

def equal():
    current_expression = display_var.get()
    current_expression = current_expression.replace("×", "*").replace("÷", "/")
    try:
        # Evaluate the expression safely
        result = eval(current_expression)
        display_var.set(result)
    except (SyntaxError, ZeroDivisionError, NameError, TypeError, ValueError):
        # If any known error happens, show "Invalid Expression"
        display_var.set("Invalid Expression")
btn_equal.config(command=equal)
	
root.mainloop()
