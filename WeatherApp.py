import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800

# def test_function(entry):
#     print("This is entry : ", entry)

# pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state},{country code}
# 3039c9411c179ef6c1e962304e7d9ff5

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        hum = weather['main']['humidity']
        press = weather['main']['pressure']
        lon = weather['coord']['lon']
        lat = weather['coord']['lat']

        final_str = 'City: %s \nCondition: %s \nTemperature : %s °C \nHumidity : %s \nPressure: %s \nLocation: %s,%s'  % (name,desc,temp,hum,press,lat,lon) 
    except:
        final_str = 'Problem Retrieving Data'
    return final_str

def get_weather(city):
    weather_key = '3039c9411c179ef6c1e962304e7d9ff5'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q' : city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = tk.Tk()
root.title("Weather Station")

#ukuran window
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background
background_image = ImageTk.PhotoImage(Image.open("/home/mkn/python/Weather/skyblue.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


#frame atas
frame = tk.Frame(root,bg='blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#masukan karakter
entry = tk.Entry(frame, font=('Likhan',20))
entry.place(relwidth=0.65, relheight=1)

#tombol
button = tk.Button(frame, text = "Get Weather", font=('Likhan',20),bg='#cccccc', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#frame bawah
lower_frame = tk.Frame(root, bg='blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

#label
label = tk.Label(lower_frame, font=('Likhan',25), bg='white', anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

#--------------------------------------------------------------------------
root.mainloop()