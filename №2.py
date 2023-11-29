import requests
from tkinter import *

def clicked():
    word_language = txt_language.get()
    word_country = txt_country.get()
    word_city = txt_city.get()
    class WeatherAPI:
        token = 'd5e2cd15f8c6dd4878df815046846e28'
        website_URL = 'http://api.openweathermap.org'
        coord_URL = '/geo/1.0/direct'
        weather_URL = '/data/2.5/weather'
    
        def __init__(self, city=word_city, country=word_country, lg=word_language):
            self.city = city
            self.country = country
            self.language = lg

        def requests_place(self):
            parameters = {'q': f'{self.city},{self.country}',
                          'limit': 1,'appid': self.token}
            URL = f'{self.website_URL}{self.coord_URL}'
            place = requests.get(URL, params=parameters)
            data = place.json()[0]
            self.coordinates(data)
    
        def coordinates(self, data):
            self.lat = data['lat']
            self.lon = data['lon']

        def requests_weather(self):
            parameters = {'lat': self.lat, 'lon': self.lon, 
                          'units': 'metric', 'appid': self.token, 'lang': self.language}
            URL = f'{self.website_URL}{self.weather_URL}'
            weather = requests.get(URL, params=parameters)
            self.weather = weather.json()
    
        def answer(self):
            city = self.weather['name']
            temp = self.weather['main']['temp']
            min_temp = self.weather['main']['temp_min']
            max_temp = self.weather['main']['temp_max']
            pressure = self.weather['main']['pressure']
            humidity = self.weather['main']['humidity']
            speed_wind = self.weather['wind']['speed']
            weather = self.weather['weather'][0]['description']
            return (f'{temp}°C {weather}\n'
                    f'максимальная температура сегодня: {max_temp}°C\n'
                    f'минимальная температура сегодня: {min_temp}°C\n'
                    f'давление - {pressure} мм.рт.ст.\n'
                    f'влажность - {humidity}%\n'
                    f'скорость ветра - {speed_wind} м/с')
    
        def show_answer(self):
            answer = Label(window, text = (f'Погода в городе {self.city}:\n' 
                                           f'{self.answer()}'), background="dodgerblue3", 
                                           foreground="white", font = ("Times New Roman", 20))
            answer.place(relx=0.55, rely=0.05)

    if __name__ == '__main__':
        weather = WeatherAPI()
        weather.requests_place()
        weather.requests_weather()
        weather.show_answer()

window = Tk()
window.title('Погода')
window.geometry('1920x720')
window.resizable (width=False, height=False)
image =  PhotoImage(file = 'image.png')
window_image = Label(window, image=image)
window_image.grid(row=0, column=0)
    
language = Label(window, 
                 text = (f'Введите язык, в котором хотите увидеть прогноз погоды, '
                         f'в формате "ru", "eg" и т.д.'), 
                 background="dodgerblue4", foreground="white", font = ("Times New Roman", 14))
language.place(relx=0.03, rely=0.03)
txt_language = Entry(window, width=20, font=("Times New Roman", 14))  
txt_language.place(relx=0.15, rely=0.07)
txt_language.focus()

country = Label(window, 
                text = (f'Введите название страны, в которой находится требуемый город:'), 
                background="dodgerblue4", foreground="white", font = ("Times New Roman", 14))
country.place(relx=0.06, rely=0.12)
txt_country = Entry(window, width=20, font=("Times New Roman", 14))  
txt_country.place(relx=0.15, rely=0.16)

city = Label(window, 
             text = (f'Введите название города, погоду которого хотите узнать:'), 
             background="dodgerblue4", foreground="white", font = ("Times New Roman", 14))
city.place(relx=0.073, rely=0.21)
txt_city = Entry(window, width=20, font=("Times New Roman", 14))  
txt_city.place(relx=0.15, rely=0.25)

button = Button(window, text="ГОТОВО", width=15, 
                font = ("Times New Roman", 25), 
                bg = "dodgerblue3", fg = "white", command=clicked)
button.place(relx = 0.12, rely = 0.35)
window.mainloop()