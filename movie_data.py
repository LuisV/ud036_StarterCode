import media
import fresh_tomatoes

# Guardians of the Galaxy is arguably the best movie series.
guardians = media.Movie(
    "Guardians of the Galaxy",
    "A group of intergalactic criminals are forced to work together "
    "to stop a fanatical warrior from taking control of the universe.",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA"
)

rogue = media.Movie(
    "Rogue One",
    "The daughter of an Imperial scientist joins the Rebel Alliance "
    "in a risky move to steal the Death Star plans.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=frdj1zb9sMY"
)

guardians2 = media.Movie(
    "Guardians of the Galaxy Vol2",
    "The Guardians must fight to keep their newfound family together "
    "as they unravel the mystery of Peter Quill's true parentage.",
    "https://upload.wikimedia.org/wikipedia/en/9/95/GotG_Vol2_poster.jpg",
    "https://www.youtube.com/watch?v=dW1BIid8Osg"
)

lion = media.Movie(
    "The Lion King",
    "Lion cub and future king Simba searches for his identity. "
    "His eagerness to please others and penchant for testing "
    "his boundaries sometimes gets him into trouble.",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=4sj1MT05lAA"
)

fast_furious = media.Movie(
    "Fast and Furious",
    "Los Angeles police officer Brian O'Connor must decide "
    "where his loyalty really lies when he becomes enamored "
    "with the street racing world he has been sent undercover to destroy. ",
    "http://www.filmofilia.com/wp-content/uploads/2009/02/fastandthefurious4_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ZsJz2TJAPjw"
)

coco = media.Movie(
    "Coco",
    "Aspiring musician Miguel, confronted with his family's "
    "ancestral ban on music, enters the Land of the Dead "
    "to find his great-great-grandfather, a legendary singer.",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?time_continue=3&v=Ga6RYejo6Hk"
)
movies = [guardians, rogue, lion, fast_furious, guardians2, coco]
fresh_tomatoes.open_movies_page(movies)
