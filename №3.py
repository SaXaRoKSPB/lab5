#Программа будет использована для нахождения любого фильма или сериала соглсано предпочтениям
#У данного API большое кол-во различных функций, которые можно использовать, но считаю, что данная программа будет саммой полезной (ну как минимум мне)



import requests, random
from tkinter import *

def clicked():
    word_year = txt_year.get()
    word_rating = txt_rating.get()
    word_genre = txt_genre.get()

    class KinopoiskAPI:
        token = '6P8SZYF-YTP4ZRY-J516QWY-04MR59B'
        website_URL = 'https://api.kinopoisk.dev'
        film_URL = '/v1.4/movie'

        def __init__(self):
            self.year = word_year
            self.rating = word_rating
            self.genre = word_genre

        def requests_film(self):
            headers = {"X-API-KEY": self.token}
            parameters = {'page': 1,'limit': 1,'year': self.year, 
                          'rating.kp': self.rating, 'genres.name': self.genre}
            URL = f'{self.website_URL}{self.film_URL}'
            request_movie = requests.get(URL, headers=headers, params=parameters)
            selected_film = request_movie.json()
            self.film = selected_film['docs'][0]

        def answer(self):
            film_name = self.film['name']
            film_rating = self.film['rating']['kp']
            film_year = self.film['year']
            #film_description = self.film['description']
            return(f'Вам подобран фильм:\n'
                   f'{film_name} {film_year} год\n'
                   f'Рейтинг на кинопоиске: {film_rating}')
                   #f'Краткое описание: {film_description}')

        def show_answer(self):
            film_information = Label(window, text=self.answer(), background="black", foreground="white", font = ("Times New Roman", 20))
            film_information.place(relx=0.38, rely=0.67)

    if __name__ == '__main__':
        movie = KinopoiskAPI()
        movie.requests_film()
        movie.show_answer()

window = Tk()
window.title('Фильмы')
window.geometry('1536x864')
window.resizable (width=False, height=False)
image =  PhotoImage(file = 'image_kinopoisk.png')
window_image = Label(window, image=image)
window_image.grid(row=0, column=0)
    
year = Label(window, 
                 text = (f'Введите промежуток лет, в пределах которого необходимо найти фильм'), 
                 background="black", foreground="white", font = ("Times New Roman", 14))
year.place(relx=0.3, rely=0.03)
txt_year = Entry(window, width=20, font=("Times New Roman", 14))  
txt_year.place(relx=0.43, rely=0.07)
txt_year.focus()

rating = Label(window, 
                text = (f'Введите промежуток рейтинга, '
                        f'в пределах которого необходимо найти фильм'), 
                background="black", foreground="white", font = ("Times New Roman", 14))
rating.place(relx=0.29, rely=0.12)
txt_rating = Entry(window, width=20, font=("Times New Roman", 14))  
txt_rating.place(relx=0.43, rely=0.16)

genre = Label(window, 
             text = (f'Введите жанр фильма, который хотели бы посмотреть'), 
             background="black", foreground="white", font = ("Times New Roman", 14))
genre.place(relx=0.35, rely=0.21)
txt_genre = Entry(window, width=20, font=("Times New Roman", 14))  
txt_genre.place(relx=0.43, rely=0.25)

button = Button(window, text="ГОТОВО", width=15, 
                font = ("Times New Roman", 25), 
                bg = "orangered2", fg = "black", command=clicked)
button.place(relx = 0.4, rely = 0.3)
window.mainloop()