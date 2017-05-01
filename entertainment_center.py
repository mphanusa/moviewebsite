""" Create an array of favorite movies with posters and trailer links.
User can click on a poster to play its youtube trailer.

"""

import media
import fresh_tomatoes

# creating list of favorite movies with posters and trailer links.

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Story Line",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/"
                             "School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "Story Line",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/"
                          "RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Story Line",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/"
                                "Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "Story Line",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/"
                           "HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# create a movie list that will be displayed and played the trailers.

movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games]

# build a movie page, display, allow user to select and play the trailer.

fresh_tomatoes.open_movies_page(movies)
                        
                        
