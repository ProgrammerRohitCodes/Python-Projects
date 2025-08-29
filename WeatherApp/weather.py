import tkinter as tk  
from tkinter import messagebox  
import requests  
  
API_KEY = "your_api_key_here"    
BASE_URL = "http://api.weatherapi.com/v1/current.json"  
  
def get_weather():  
    city = city_entry.get()  
    if not city:  
        messagebox.showwarning("Input Error", "Please enter a city name.")  
        return

    try:
        url = f"{BASE_URL}?key={API_KEY}&q={city}"
        response = requests.get(url)
        data = response.json()

        # Extract information
        location = f"{data['location']['name']}, {data['location']['country']}"
        temperature = f"{data['current']['temp_c']}°C"
        condition = data['current']['condition']['text']
 
        # Display on labels
        location_label.config(text=f"Location: {location}")
        temp_label.config(text=f"Temperature: {temperature}")
        cond_label.config(text=f"Condition: {condition}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to get weather data.\n{e}")  
  
# GUI Setup  
root = tk.Tk()  
root.title("Weather App")  
root.geometry("360x300")  
root.configure(bg="#eaf6fb")    
  
# Title  
title = tk.Label(root, text="Weather App", font=("Arial", 10, "bold"), bg="#eaf6fb")  
title.pack()  
  
# Input Entry  
city_entry = tk.Entry(root, font=("Arial", 13), width=15, justify="center")  
city_entry.pack()  
  
# Get Weather Button  
get_button = tk.Button(root, text="Get Weather", font=("Arial", 9), bg="#3498db", fg="white", padx=10, pady=5, command=get_weather)  
get_button.pack(pady=10)  
  
# Result Labels  
location_label = tk.Label(root, text="Location: ", font=("Arial", 9), bg="#eaf6fb", anchor="w")  
location_label.pack(pady=5)  
  
temp_label = tk.Label(root, text="Temperature: ", font=("Arial", 9), bg="#eaf6fb", anchor="w")  
temp_label.pack(pady=5)  
  
cond_label = tk.Label(root, text="Condition: ", font=("Arial", 9), bg="#eaf6fb", anchor="w")  
cond_label.pack(pady=5)  
  
root.mainloop()
