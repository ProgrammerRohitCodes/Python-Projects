import tkinter as tk

app = tk.Tk()
app.configure(bg="#3a3a3a")

main_container = tk.Frame(app)
main_container.pack()

label_style = {
    "font": ("Segoe UI", 12, "bold"),
    "fg": "white",
    "bg": "#4A4A4A",
    "width": 30,
    "height": 2,
    "bd": 3,
    "relief": "groove"
}

info_style = {
    "font": ("Segoe UI", 10),
    "fg": "white",
    "bg": "#3a3a3a"
}

time_page = tk.Frame(main_container)
time_label = tk.Label(time_page, text="This is Page 1: Time", **label_style)
time_label.pack()

temperature_page = tk.Frame(main_container)
temperature_label = tk.Label(temperature_page, text="This is Page 2: Temperature", **label_style)
temperature_label.pack()

area_page = tk.Frame(main_container)
area_label = tk.Label(area_page, text="This is Page 3: Area", **label_style)
area_label.pack()

length_page = tk.Frame(main_container)
length_label = tk.Label(length_page, text="This is Page 4: Length", **label_style)
length_label.pack()

mass_page = tk.Frame(main_container)
mass_label = tk.Label(mass_page, text="This is Page 5: Mass", **label_style)
mass_label.pack()

data_page = tk.Frame(main_container)
data_label = tk.Label(data_page, text="This is Page 6: Data", **label_style)
data_label.pack()

speed_page = tk.Frame(main_container)
speed_label = tk.Label(speed_page, text="This is Page 7: Speed", **label_style)
speed_label.pack()

currency_page = tk.Frame(main_container)
currency_label = tk.Label(currency_page, text="This is Page 8: Currency", **label_style)
currency_label.pack()

page_list = [
    time_page,
    temperature_page,
    area_page,
    length_page,
    mass_page,
    data_page,
    speed_page,
    currency_page
]

info_list = [
    "seconds --> minutes",
    "Celsius --> Fahrenheit",
    "sq cm --> sq meter",
    "cm --> meter",
    "gram --> kilogram",
    "bytes --> kilobytes",
    "km/hr --> m/s",
    "Rupees --> Yen (approx)"
]

placeholder1 = "Enter Value..."
placeholder2 = "Converted Value..."
current_index = 0
info_label = tk.Label(app, text="", **info_style)

def display_page(index):
    global current_index
    current_index = index
    for page in page_list:
        page.pack_forget()
    page_list[index].pack()
    entry1.delete(0, tk.END)
    entry1.insert(0, placeholder1)
    entry1.config(fg="gray")
    entry2.delete(0, tk.END)
    entry2.insert(0, placeholder2)
    entry2.config(fg="gray")
    info_label.config(text=info_list[index])

def on_click_entry1(event):
    if entry1.get() == placeholder1:
        entry1.delete(0, tk.END)
        entry1.config(fg='black')

def on_focusout_entry1(event):
    if entry1.get() == "":
        entry1.insert(0, placeholder1)
        entry1.config(fg='gray')

def on_click_entry2(event):
    if entry2.get() == placeholder2:
        entry2.delete(0, tk.END)
        entry2.config(fg='black')

def on_focusout_entry2(event):
    if entry2.get() == "":
        entry2.insert(0, placeholder2)
        entry2.config(fg='gray')

def unit_conversion_logic():
    global current_index

    try:
        count1 = float(entry1.get())
    except ValueError:
        entry2.delete(0, tk.END)
        entry2.insert(0, "Invalid input")
        entry2.config(fg='red')
        return

    if current_index == 0:
        result = count1 / 60
    elif current_index == 1:
        result = count1 * 9/5 + 32
    elif current_index == 2:
        result = count1 / 1000000
    elif current_index == 3:
        result = count1 / 100
    elif current_index == 4:
        result = count1 / 1000
    elif current_index == 5:
        result = count1 / 1024
    elif current_index == 6:
        result = count1 * 1000 / 3600
    elif current_index == 7:
        result = count1 * 83
    else:
        entry2.delete(0, tk.END)
        entry2.insert(0, "Invalid page")
        entry2.config(fg='red')
        return

    entry2.delete(0, tk.END)
    entry2.insert(0, str(round(result, 4)))
    entry2.config(fg='black')

title_label = tk.Label(
    app,
    text="Welcome to the Unit Converter!",
    font=('Segoe UI', 9, 'bold'),
    background='#3a3a3a',
    foreground='#a0ff90',
    bd=6,
    relief='groove',
    padx=15,
    pady=15
)
title_label.pack(pady=10)

button_style = {
    "font": ("Segoe UI", 8, "bold"),
    "fg": "white",
    "width": 11,
    "height": 2,
    "bd": 3,
    "relief": "groove"
}

button_frame = tk.Frame(app, bg="#3a3a3a")
button_frame.pack(pady=20)

time_button = tk.Button(button_frame, text="Time", bg="#1e90ff", **button_style, command=lambda: display_page(0))
temperature_button = tk.Button(button_frame, text="Temperature", bg="#32cd32", **button_style, command=lambda: display_page(1))
area_button = tk.Button(button_frame, text="Area", bg="#94d2bd", **button_style, command=lambda: display_page(2))
length_button = tk.Button(button_frame, text="Length", bg="#ff7f50", **button_style, command=lambda: display_page(3))
mass_button = tk.Button(button_frame, text="Mass", bg="#9370db", **button_style, command=lambda: display_page(4))
data_button = tk.Button(button_frame, text="Data", bg="#bb3e03", **button_style, command=lambda: display_page(5))
speed_button = tk.Button(button_frame, text="Speed", bg="#ae2012", **button_style, command=lambda: display_page(6))
currency_button = tk.Button(button_frame, text="Currency", bg="#228b22", **button_style, command=lambda: display_page(7))

time_button.grid(row=0, column=0, padx=5, pady=5)
temperature_button.grid(row=0, column=1, padx=5, pady=5)
area_button.grid(row=1, column=0, padx=5, pady=5)
length_button.grid(row=1, column=1, padx=5, pady=5)
mass_button.grid(row=2, column=0, padx=5, pady=5)
data_button.grid(row=2, column=1, padx=5, pady=5)
speed_button.grid(row=3, column=0, padx=5, pady=5)
currency_button.grid(row=3, column=1, padx=5, pady=5)

convert_button = tk.Button(app, text="Convert", command=unit_conversion_logic, font=("Segoe UI", 10, "bold"), bg="#ffcc00", fg="black", bd=4, relief="raised")
convert_button.pack(pady=15)

entry_frame = tk.Frame(app, bg="#3a3a3a")
entry_frame.pack(pady=10)

entry1 = tk.Entry(entry_frame, fg='gray', width=15)
entry1.insert(0, placeholder1)
entry1.grid(row=0, column=0, padx=10)

entry2 = tk.Entry(entry_frame, fg='gray', width=15)
entry2.insert(0, placeholder2)
entry2.grid(row=0, column=1, padx=10)

entry1.bind("<FocusIn>", on_click_entry1)
entry1.bind("<FocusOut>", on_focusout_entry1)
entry2.bind("<FocusIn>", on_click_entry2)
entry2.bind("<FocusOut>", on_focusout_entry2)

info_label.pack(pady=(5, 20))

display_page(0)

app.mainloop()
