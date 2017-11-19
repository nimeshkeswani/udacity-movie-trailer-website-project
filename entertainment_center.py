import media
from fresh_tomatoes import open_movies_page

# Initialize 6 favorite movies
prisoners = media.Movie("Prisoners",
                        "https://images-na.ssl-images-amazon.com/images/M/"
                        "MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@."
                        "_V1_UY1200_CR90,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=bpXfcTF6iVk")

warrior = media.Movie("Warrior",
                      "https://www.iceposter.com/thumbs/MOV_860d8393_b.jpg",
                      "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

transporter_3 = media.Movie("Transporter 3",
                            "https://upload.wikimedia.org/wikipedia/en/f/f1"
                            "/Transporter_3_poster.jpg",
                            "https://www.youtube.com/watch?v=Pbh3CDBNIQA")

fifty_first_dates = media.Movie("50 First Dates",
                                "https://static.rogerebert.com/uploads/movie"
                                "/movie_poster/50-first-dates-2004/large_ztMU"
                                "IJV2nDN0tJ24aW7pjMvTxVV.jpg",
                                "https://www.youtube.com/watch?v=ErjP5xMTc8I")

interstellar = media.Movie("Interstellar",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/In"
                           "terstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Incep"
                        "tion_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# Create a list of movies for the open_movies_page function to take as an input
movie_list = [prisoners, warrior, transporter_3, fifty_first_dates,
              interstellar, inception]

open_movies_page(movie_list)
