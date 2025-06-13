import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Set window size to fit small/mobile-like screen
root.geometry("300x200") # width x height

# Function to update time every second
def time():
    a = strftime("%H:%M:%S %p\n%D") # Get current time + date
    label.config(text=a) # Update label text
    label.after(1000, time) # Call this function again after 1000 ms (1 sec)

# Create label with better font, color, and border for readability
label = tk.Label(
    root,
    font=('Helvetica', 20, 'bold'), # Clear and bold font
    background='black', # Background color
    foreground='lime', # Text color
    bd=8, # Border thickness
    relief='ridge', # Border style
    padx=10, pady=10 # Inner padding
)

# Center the label in the window
label.pack(anchor='center', expand=True)

# Start the clock function
time()

# Keep the window running
root.mainloop()
