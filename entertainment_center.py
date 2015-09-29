# import fresh_tomatoes.py, use open_movies_page function & structure html page
import fresh_tomatoes
# import media so can create instances of Movie
import media

# toystory instance
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

mib = media.Movie(
    "Men In Black",
    "Agents trying to save the world",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/Men_in_Black.png",
    "https://www.youtube.com/watch?v=vsQ41frO-kI")


school_of_rock = media.Movie(
    "School of Rock",
    "Using rock music to learn",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie(
    "Ratatouilee",
    "A paris rat who becomes a chef",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=vsQ41frO-kI")

dumb_and_dumber = media.Movie(
    "Dumb and Dumber",
    "Two friends try to return a suitcase",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
    "https://www.youtube.com/watch?v=tNLb4t9xgNM")

gladiator = media.Movie(
    "Gladiator",
    "A general who became a slave who became a gladiator who defied an empire",
    "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
    "https://www.youtube.com/watch?v=ol67qo3WhJk")

# creating array of movies
movies = [toy_story, avatar, mib, school_of_rock, dumb_and_dumber, gladiator]

# calling open_movies_page from fresh_tomatoes.py with argument movies
# It takes array of values, this opens up html page and produces movies
fresh_tomatoes.open_movies_page(movies)
