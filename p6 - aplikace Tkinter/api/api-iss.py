import requests
import datetime
from tkinter import *

# 1xx = ještě není konec
# 2xx = vše ok
# 3xx = přesměrování
# 4xx = chyba na straně uživatele
# 5xx = chyba na straně poskytovatele

# print(f"Poloha ISS je {latitude} zeměpisné šířky, {longitude} zeměpisné délky a aktuálně je {dt_object}")

# Function
def iss_coordinates():
    response  = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude=data["iss_position"]["longitude"]
    latitude=data["iss_position"]["latitude"]
    timestamp = data["timestamp"]
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    longitude_label.config(text=f"Zeměpisná délka ISS je: {longitude}")
    latitude_label.config(text=f"Zeměpisná šířka ISS je: {latitude}")
    date_label.config(text=f"Čas je: {dt_object}")


window = Tk()
window.minsize(700,400)
window.resizable(False, False)
window.title("Location ISS")

# Canva
canvas = Canvas(window, width=500, height=280)
canvas.pack()
img = PhotoImage(file="giphy.gif")
canvas.create_image(0,0,anchor="nw", image = img)

# Coordinate Frame
coordinates_frame = Frame(window)
coordinates_frame.pack()

recount_button = Button(coordinates_frame, text="Současné souřadnice ISS", command=iss_coordinates)
recount_button.pack()


# Labels
latitude_label = Label()
latitude_label.pack()
longitude_label = Label()
longitude_label.pack()
date_label = Label()
date_label.pack()



window.mainloop()