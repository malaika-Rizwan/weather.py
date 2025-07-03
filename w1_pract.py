from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = com.get().strip()
    if not city:
        update_labels("No city selected", "-", "-", "-", "")
        return

    api_key = "890c90234e2535550f47c5c226d82679"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = round(data["main"]["temp"] - 273.15, 2)
        pressure = data["main"]["pressure"]

        icon = get_weather_icon(weather)
        update_labels(weather, description, f"{temp} °C", f"{pressure} hPa", icon)

    except:
        update_labels("Error", "-", "-", "-", "❌")

def update_labels(weather, description, temp, pressure, icon):
    W_label1.config(text=weather)
    Wb_label1.config(text=description)
    tem_label1.config(text=temp)
    pre_label1.config(text=pressure)
    icon_label.config(text=icon)

def get_weather_icon(weather):
    weather = weather.lower()
    if "rain" in weather:
        return "🌧️"
    elif "cloud" in weather:
        return "☁️"
    elif "clear" in weather:
        return "🌞"
    elif "snow" in weather:
        return "❄️"
    elif "storm" in weather:
        return "⛈️"
    else:
        return "🌈"

# GUI Setup
win = Tk()
win.title("Malaikoo Weather App")
win.geometry("500x600")
win.config(bg="#6ECEDA")  # Light blue background

# Title
name_label = Label(win, text="Malaikoo Weather App", font=("Comic Sans MS", 24, "bold"), bg="#6ECEDA", fg="white")
name_label.pack(pady=20)

# Dropdown
pakistan_cities = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Peshawar", "Quetta", "Faisalabad",
    "Multan", "Hyderabad", "Sialkot", "Gujranwala", "Bahawalpur", "Sukkur",
    "Abbottabad", "Mardan", "Sargodha", "Rahim Yar Khan", "Dera Ghazi Khan", "Chitral",
    "Swat", "Mirpur", "Muzaffarabad", "Gilgit", "Skardu"
]

com = ttk.Combobox(win, values=pakistan_cities, font=("Times New Roman", 16))
com.pack(pady=10)

done_button = Button(win, text="Check Weather", font=("Arial", 16, "bold"), command=data_get, bg="#4CAF50", fg="white")
done_button.pack(pady=10)

# Icon
icon_label = Label(win, text="", font=("Arial", 50), bg="#6ECEDA")
icon_label.pack(pady=10)

# Weather Info Labels
info_frame = Frame(win, bg="#6ECEDA")
info_frame.pack(pady=20)

def create_info_row(text, var_label):
    label = Label(info_frame, text=text, font=("Arial", 18), bg="#6ECEDA", fg="black")
    label.pack(pady=5)
    var_label.pack(pady=5)

W_label1 = Label(info_frame, text="", font=("Arial", 18), bg="#6ECEDA", fg="blue")
Wb_label1 = Label(info_frame, text="", font=("Arial", 16), bg="#6ECEDA", fg="navy")
tem_label1 = Label(info_frame, text="", font=("Arial", 18), bg="#6ECEDA", fg="red")
pre_label1 = Label(info_frame, text="", font=("Arial", 18), bg="#6ECEDA", fg="darkgreen")

create_info_row("Weather:", W_label1)
create_info_row("Description:", Wb_label1)
create_info_row("Temperature:", tem_label1)
create_info_row("Pressure:", pre_label1)

win.mainloop()
