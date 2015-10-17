__author__ = 'skylar1992'

import Movie_Website
import fresh_tomatoes

# First Movie "Pokemon Go!"
# Title Story Poster Trailer
Pokemon_Go = Movie_Website.Movie("Pokemon Go",
                                 "Turn the real world into Pokemon World with your mobile devices!",
                                 "http://cdn1.pcadvisor.co.uk/cmsdata/features/3625388/pokemon_go_800_thumb800.png",
                                 "https://www.youtube.com/watch?v=2sj2iQyBTQs"

                                )

#2nd Movie

Avatar = Movie_Website.Movie("Avatar",
                             "AVATAR takes us to a spectacular world beyond imagination, where a reluctant hero embarks on an epic adventure, ultimately fighting to save the alien world he has learned to call home.",
                             "http://resizing.flixster.com/W1BtrV4MS0HZwzJQSBe4mBQfwQs=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
                             "https://www.youtube.com/watch?v=5PSNL1qE6VY"
)

#3rd Movie

The_Matrix = Movie_Website.Movie("The Matrix",
                                 "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                                 "https://fangirlknitsscarf.files.wordpress.com/2013/09/the-matrix-1999-wallpaper.jpg",
                                 "https://www.youtube.com/watch?v=vKQi3bBA1y8"
)

#4th Movie

Inception = Movie_Website.Movie("Tnception",
                                 "A skilled extractor is offered a chance to regain his old life as payment for a task considered to be impossible.",
                                 "http://resizing.flixster.com/l5I-Yk--UFS2Nrq_GJmKcWzRZ7M=/800x1200/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166725_ori.jpg",
                                 "https://www.youtube.com/watch?v=YoHD9XEInc0"
)

#5th Movie

The_Waterboy = Movie_Website.Movie("The Waterboy",
                                 "The Waterboy is a 1998 American sports film directed by Frank Coraci, and starring Adam Sandler, Kathy Bates, Fairuza Balk, Henry Winkler, Jerry Reed, Larry Gilliard, Jr., Blake Clark, Peter Dante and Jonathan Loughran.",
                                 "http://ecx.images-amazon.com/images/I/81BeAomXzOL._SL1500_.jpg",
                                 "https://www.youtube.com/watch?v=z8yv9eq5s14"
)

#6th Movie

The_Other_Woman = Movie_Website.Movie("The Other Woman",
                                 "After discovering her boyfriend is married, a woman (Cameron Diaz) tries to get her ruined life back on track. But when she accidentally meets the wife he's been cheating on (Leslie Mann), she realizes they have much in common, and her sworn enemy becomes her greatest friend. When yet another affair is discovered (Kate Upton), all three women team up to plot mutual revenge on their cheating, lying, three-timing SOB.",
                                 "http://static1.squarespace.com/static/53a5dbcee4b0c840895f2bfe/53a61021e4b0cd7da76c1c84/53a6104de4b0b0e684bcc68b/1403392078465/the-other-woman-og.png",
                                 "https://www.youtube.com/watch?v=7mYaPq7ZL2Q"
)

# Create the movie list array
movies = [Pokemon_Go,Avatar,The_Matrix,Inception,The_Waterboy,The_Other_Woman]

#Use fresh_tomatoes.py to create the page
fresh_tomatoes.open_movies_page(movies)