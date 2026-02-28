import requests
import datetime
from tkinter import *

# =========================
# Převod souřadnic na pixely
# =========================
def latlon_to_xy(lat, lon, width, height):
    x = (lon + 180) * (width / 360)
    y = (90 - lat) * (height / 180)
    return x, y


def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    timestamp = data["timestamp"]

    dt_object = datetime.datetime.fromtimestamp(timestamp)

    longitude_label.config(text=f"Zeměpisná délka ISS je: {longitude}")
    latitude_label.config(text=f"Zeměpisná šířka ISS je: {latitude}")
    date_label.config(text=f"Čas je: {dt_object}")

    # 🔥 Vykreslení ISS na mapě
    draw_iss(latitude, longitude)


# =========================
# Vykreslení ISS
# =========================
def draw_iss(lat, lon):
    canvas.delete("iss")  # smaže starou tečku

    x, y = latlon_to_xy(lat, lon, map_width, map_height)

    canvas.create_oval(
        x-5, y-5, x+5, y+5,
        fill="red",
        outline="white",
        width=2,
        tags="iss"
    )


# =========================
# GUI
# =========================
window = Tk()
window.title("Location ISS")
window.resizable(False, False)

map_width = 1000
map_height = 500

canvas = Canvas(window, width=map_width, height=map_height)
canvas.pack()

# Nahraj mapu světa
world_map = PhotoImage(file="world_map.png")
canvas.create_image(0, 0, anchor="nw", image=world_map)

recount_button = Button(window, text="Současné souřadnice ISS", command=iss_coordinates)
recount_button.pack()

latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()

date_label = Label()
date_label.pack()

window.mainloop()
