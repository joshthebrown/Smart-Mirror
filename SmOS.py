import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime
import requests
import datetime
import json
from pprint import pprint

# API KEY FOR OPENWEATHERMAP
# API_KEY = '3d64eb4f5299cb54cbcc53cdd96110fb'
# base_url = "http://api.openweathermap.org/data/2.5/weather?"

# city_name = 'San Diego'

# Final_url = base_url + "appid=" + API_KEY + "&q=" + city_name
# weather_data = requests.get(Final_url)
# x = weather_data.json()

# global/important vars
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
api_key = "your key here"

# Auxillary functions
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Clock functions
# This function is used to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000, time)

# getters for weather data
def get_weather_description():
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #temperature
        temperature = data["main"]["temp"]
        current_temperature_F = (((temperature - 273.15) * 9.0) / 5.0) + 32.0

        #description
        weather = data["weather"][0]["description"]

        return "Today in San Diego: {} at {:.0f}°F".format(weather, current_temperature_F)
    else:
        return "Error getting weather data"
    
def get_min_temp():
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_min = data["main"]["temp_min"]
        temp_min = float(temp_min)
        temp_min = (((temp_min - 273.15) * 9.0) / 5.0) + 32.0

        return "Today's Low: {:.0f}°F".format(temp_min)
    else:
        return "Error getting minimum temperature"
    
def get_max_temp():
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_max = data["main"]["temp_max"]
        temp_max = float(temp_max)
        temp_max = (((temp_max - 273.15) * 9.0) / 5.0) + 32.0

        return "Today's High: {:.0f}°F".format(temp_max)
    else:
        return "Error getting maximum temperature"
    
def get_humidity():
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        humidity = data["main"]["humidity"]

        return "Current Humidity: {:.0f}%".format(humidity)
    else:
        return "Error getting humidity data"
    
def get_sunrise(): 
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sunrise = data["sys"]["sunrise"]
        sunrise_time = datetime.datetime.utcfromtimestamp(sunrise)
        sunrise_time = sunrise_time.replace(tzinfo=datetime.timezone.utc).astimezone()

        return "Sun rises at: " + sunrise_time.strftime('%H:%M')
    else:
        return "Error getting sunrise data"
    
def get_sunset(): 
    url = "http://api.openweathermap.org/data/2.5/weather?q=San%20Diego&appid={}".format(api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        sunset = data["sys"]["sunset"]
        sunset_time = datetime.datetime.utcfromtimestamp(sunset)
        sunset_time = sunset_time.replace(tzinfo=datetime.timezone.utc).astimezone()

        return "Sun sets at: " + sunset_time.strftime('%H:%M')
    else:
        return "Error getting sunset data"
    
# used in rotate_display()
print_data = [
    get_weather_description(),
    get_min_temp(),
    get_max_temp(),
    get_humidity(),
    get_sunrise(),
    get_sunset()
]

current_index = 0 
def rotate_display():
    global current_index
    weather_label.config(text=print_data[current_index])
    current_index = (current_index + 1) % len(print_data)
    weather_label.after(3000, rotate_display) # rotate every 3000 ms (3 seconds)

# GUI code
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Define window
root = Tk()

# General appearance of "OS"
root.title("Group 1 Smart Mirror")
root.attributes("-fullscreen", 1)
root.resizable(0, 0)
root.config(bg='#000000')

# Frames
greeting_frame = tk.Frame()
info_frame = tk.Frame(bg='#000000')

# Labels
weather_label = tk.Label(master=info_frame, 
                         text="",
                         foreground='white',
                         background='black',
                         font=("Courier", 20, "bold")
                        )
weather_label.pack()

greeting_label = Label(master=greeting_frame, 
                       text="Hello Group 1!",
                       font=('Arial', 40, 'bold'),
                       foreground='white',
                       background='black')
greeting_label.pack()

# Styling the label widget so that clock
# will look more attractive
clock = Label(master= info_frame, 
              font=('arial black', 40, 'bold'),
              background='black',
              foreground='white')

# Placing clock at the centre
# of the tkinter window
clock.pack(anchor='center')
greeting_frame.pack()
info_frame.pack(padx=50,
                pady=50,
                )

# Execution Stage
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
time()
rotate_display()
root.mainloop() # Run root window | ideally should be the last line in the source code
