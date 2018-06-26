import fresh_tomatoes
import media

logan = media.Movie("Logan",
                    "A story about Wolverine",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODQwNTg4OV5BMl5BanBnXkFtZTgwMTk4MTAzMjI@._V1_.jpg",
                    "https://youtu.be/Div0iP65aZo")
inglorious_basterds = media.Movie("Inglourious Basterds",
                     "A story about killing Nazis.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SY1000_SX675_AL_.jpg",
                     "https://youtu.be/KnrRy6kSFF0")
spirited_away = media.Movie("Spirited Away",
                            "A wondrous world",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BOGJjNzZmMmUtMjljNC00ZjU5LWJiODQtZmEzZTU0MjBlNzgxL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://youtu.be/ByXuk9QqQkk")
rush = media.Movie("Rush",
                   "Legendary rivalry between James Hunt and Niki Lauda",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BOWEwODJmZDItYTNmZC00OGM4LThlNDktOTQzZjIzMGQxODA4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg",
                   "https://youtu.be/lzNbGH1oZJc")
ponyo = media.Movie("Ponyo",
                    "Goldish princess falls in love",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NzkxNTg2MF5BMl5BanBnXkFtZTcwMTA3MjU1Mg@@._V1_.jpg",
                    "https://youtu.be/CsR3KVgBzSM")
the_dark_knight = media.Movie("The Dark Knight",
                              "Batman battles the Joker",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                              "https://youtu.be/EXeTwQWrcwY")
inception = media.Movie("Inception",
                        "A dream within a dream within a dream",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://youtu.be/YoHD9XEInc0")
city_of_god = media.Movie("City of god",
                          "Life of streets in Rio",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_.jpg",
                          "https://youtu.be/dcUOO4Itgmw")
la_vita_e_bella = media.Movie("La Vita e Bella",
                              "Italian family during WW2",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BYmJmM2Q4NmMtYThmNC00ZjRlLWEyZmItZTIwOTBlZDQ3NTQ1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX670_AL_.jpg",
                              "https://youtu.be/pAYEQP8gx3w")
leon_the_professional = media.Movie("Leon The Professional",
                                    "Leon and Matilda form an unusual relationship",
                                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjdjMGU3MGYtN2Y5ZC00MTE4LWE4YWQtMTBhMjc3MTk0ZDUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX664_AL_.jpg",
                                    "https://youtu.be/aNQqoExfQsg")
#friday = media.Movie("Friday", "", "", "")
#gladiator = media.Movie("Gladiator", "", "", "")
#full_metal_jacket = media.Movie("Full Metal Jacket", "", "", "")
#pans_labryinth = media.Movie("Panys Labyrinth", "", "", "")
#my_neighbor_totoro = media.Movie("My Neighbor Totoro", "", "", "")
#the_wolf_of_wall_street = media.Movie("The Wolf of Wall Street", "", "", "")
#grandmas_boy = media.Movie("Grandmas Boy", "", "", "")
movies = [logan, inglorious_basterds, spirited_away, rush, ponyo, the_dark_knight,
          inception, city_of_god, la_vita_e_bella, leon_the_professional]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)


                     
