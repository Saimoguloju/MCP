from mcp.server.fastmcp import FastMCP

mcp = FastMCP("IMDB Top 100 Movie Recommendation Server")

MOVIES = [
    {"rank": 1,   "title": "The Shawshank Redemption", "year": 1994, "rating": 9.3, "genre": ["Drama"],                          "director": "Frank Darabont"},
    {"rank": 2,   "title": "The Godfather",             "year": 1972, "rating": 9.2, "genre": ["Crime", "Drama"],                 "director": "Francis Ford Coppola"},
    {"rank": 3,   "title": "The Dark Knight",           "year": 2008, "rating": 9.0, "genre": ["Action", "Crime", "Drama"],       "director": "Christopher Nolan"},
    {"rank": 4,   "title": "The Godfather Part II",     "year": 1974, "rating": 9.0, "genre": ["Crime", "Drama"],                 "director": "Francis Ford Coppola"},
    {"rank": 5,   "title": "12 Angry Men",              "year": 1957, "rating": 9.0, "genre": ["Crime", "Drama"],                 "director": "Sidney Lumet"},
    {"rank": 6,   "title": "Schindler's List",          "year": 1993, "rating": 9.0, "genre": ["Biography", "Drama", "History"],  "director": "Steven Spielberg"},
    {"rank": 7,   "title": "The Lord of the Rings: The Return of the King", "year": 2003, "rating": 9.0, "genre": ["Action", "Adventure", "Drama"], "director": "Peter Jackson"},
    {"rank": 8,   "title": "Pulp Fiction",              "year": 1994, "rating": 8.9, "genre": ["Crime", "Drama"],                 "director": "Quentin Tarantino"},
    {"rank": 9,   "title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "rating": 8.8, "genre": ["Action", "Adventure", "Drama"], "director": "Peter Jackson"},
    {"rank": 10,  "title": "The Good, the Bad and the Ugly", "year": 1966, "rating": 8.8, "genre": ["Western"],                  "director": "Sergio Leone"},
    {"rank": 11,  "title": "Forrest Gump",              "year": 1994, "rating": 8.8, "genre": ["Drama", "Romance"],              "director": "Robert Zemeckis"},
    {"rank": 12,  "title": "Fight Club",                "year": 1999, "rating": 8.8, "genre": ["Drama"],                         "director": "David Fincher"},
    {"rank": 13,  "title": "Inception",                 "year": 2010, "rating": 8.8, "genre": ["Action", "Adventure", "Sci-Fi"], "director": "Christopher Nolan"},
    {"rank": 14,  "title": "The Lord of the Rings: The Two Towers", "year": 2002, "rating": 8.8, "genre": ["Action", "Adventure", "Drama"], "director": "Peter Jackson"},
    {"rank": 15,  "title": "The Matrix",                "year": 1999, "rating": 8.7, "genre": ["Action", "Sci-Fi"],              "director": "Lana Wachowski"},
    {"rank": 16,  "title": "Goodfellas",                "year": 1990, "rating": 8.7, "genre": ["Biography", "Crime", "Drama"],   "director": "Martin Scorsese"},
    {"rank": 17,  "title": "One Flew Over the Cuckoo's Nest", "year": 1975, "rating": 8.7, "genre": ["Drama"],                   "director": "Milos Forman"},
    {"rank": 18,  "title": "Seven Samurai",             "year": 1954, "rating": 8.6, "genre": ["Action", "Adventure", "Drama"],  "director": "Akira Kurosawa"},
    {"rank": 19,  "title": "Se7en",                     "year": 1995, "rating": 8.6, "genre": ["Crime", "Drama", "Mystery"],     "director": "David Fincher"},
    {"rank": 20,  "title": "City of God",               "year": 2002, "rating": 8.6, "genre": ["Crime", "Drama"],                "director": "Fernando Meirelles"},
    {"rank": 21,  "title": "The Silence of the Lambs",  "year": 1991, "rating": 8.6, "genre": ["Crime", "Drama", "Thriller"],    "director": "Jonathan Demme"},
    {"rank": 22,  "title": "It's a Wonderful Life",     "year": 1946, "rating": 8.6, "genre": ["Drama", "Fantasy", "Romance"],   "director": "Frank Capra"},
    {"rank": 23,  "title": "Life is Beautiful",         "year": 1997, "rating": 8.6, "genre": ["Comedy", "Drama", "Romance"],    "director": "Roberto Benigni"},
    {"rank": 24,  "title": "Star Wars: Episode IV",     "year": 1977, "rating": 8.6, "genre": ["Action", "Adventure", "Fantasy"],"director": "George Lucas"},
    {"rank": 25,  "title": "Interstellar",              "year": 2014, "rating": 8.6, "genre": ["Adventure", "Drama", "Sci-Fi"],  "director": "Christopher Nolan"},
    {"rank": 26,  "title": "Saving Private Ryan",       "year": 1998, "rating": 8.6, "genre": ["Drama", "War"],                  "director": "Steven Spielberg"},
    {"rank": 27,  "title": "Spirited Away",             "year": 2001, "rating": 8.6, "genre": ["Animation", "Adventure", "Family"], "director": "Hayao Miyazaki"},
    {"rank": 28,  "title": "The Green Mile",            "year": 1999, "rating": 8.6, "genre": ["Crime", "Drama", "Fantasy"],     "director": "Frank Darabont"},
    {"rank": 29,  "title": "Parasite",                  "year": 2019, "rating": 8.5, "genre": ["Comedy", "Drama", "Thriller"],   "director": "Bong Joon-ho"},
    {"rank": 30,  "title": "Leon: The Professional",   "year": 1994, "rating": 8.5, "genre": ["Action", "Crime", "Drama"],       "director": "Luc Besson"},
    {"rank": 31,  "title": "The Usual Suspects",        "year": 1995, "rating": 8.5, "genre": ["Crime", "Mystery", "Thriller"],  "director": "Bryan Singer"},
    {"rank": 32,  "title": "The Pianist",               "year": 2002, "rating": 8.5, "genre": ["Biography", "Drama", "Music"],   "director": "Roman Polanski"},
    {"rank": 33,  "title": "Psycho",                    "year": 1960, "rating": 8.5, "genre": ["Horror", "Mystery", "Thriller"], "director": "Alfred Hitchcock"},
    {"rank": 34,  "title": "Gladiator",                 "year": 2000, "rating": 8.5, "genre": ["Action", "Adventure", "Drama"],  "director": "Ridley Scott"},
    {"rank": 35,  "title": "American History X",        "year": 1998, "rating": 8.5, "genre": ["Drama"],                         "director": "Tony Kaye"},
    {"rank": 36,  "title": "The Lion King",             "year": 1994, "rating": 8.5, "genre": ["Animation", "Adventure", "Drama"], "director": "Roger Allers"},
    {"rank": 37,  "title": "Grave of the Fireflies",    "year": 1988, "rating": 8.5, "genre": ["Animation", "Drama", "War"],     "director": "Isao Takahata"},
    {"rank": 38,  "title": "The Departed",              "year": 2006, "rating": 8.5, "genre": ["Crime", "Drama", "Thriller"],    "director": "Martin Scorsese"},
    {"rank": 39,  "title": "Whiplash",                  "year": 2014, "rating": 8.5, "genre": ["Drama", "Music"],                "director": "Damien Chazelle"},
    {"rank": 40,  "title": "The Prestige",              "year": 2006, "rating": 8.5, "genre": ["Drama", "Mystery", "Sci-Fi"],    "director": "Christopher Nolan"},
    {"rank": 41,  "title": "Casablanca",                "year": 1942, "rating": 8.5, "genre": ["Drama", "Romance", "War"],       "director": "Michael Curtiz"},
    {"rank": 42,  "title": "Once Upon a Time in the West", "year": 1968, "rating": 8.5, "genre": ["Western"],                   "director": "Sergio Leone"},
    {"rank": 43,  "title": "Memento",                   "year": 2000, "rating": 8.5, "genre": ["Mystery", "Thriller"],           "director": "Christopher Nolan"},
    {"rank": 44,  "title": "Back to the Future",        "year": 1985, "rating": 8.5, "genre": ["Adventure", "Comedy", "Sci-Fi"], "director": "Robert Zemeckis"},
    {"rank": 45,  "title": "Alien",                     "year": 1979, "rating": 8.5, "genre": ["Horror", "Sci-Fi"],              "director": "Ridley Scott"},
    {"rank": 46,  "title": "Apocalypse Now",            "year": 1979, "rating": 8.4, "genre": ["Drama", "Mystery", "War"],       "director": "Francis Ford Coppola"},
    {"rank": 47,  "title": "Joker",                     "year": 2019, "rating": 8.4, "genre": ["Crime", "Drama", "Thriller"],    "director": "Todd Phillips"},
    {"rank": 48,  "title": "Django Unchained",          "year": 2012, "rating": 8.4, "genre": ["Drama", "Western"],              "director": "Quentin Tarantino"},
    {"rank": 49,  "title": "WALL-E",                    "year": 2008, "rating": 8.4, "genre": ["Animation", "Adventure", "Family"], "director": "Andrew Stanton"},
    {"rank": 50,  "title": "Paths of Glory",            "year": 1957, "rating": 8.4, "genre": ["Drama", "War"],                  "director": "Stanley Kubrick"},
    {"rank": 51,  "title": "The Shining",               "year": 1980, "rating": 8.4, "genre": ["Drama", "Horror"],               "director": "Stanley Kubrick"},
    {"rank": 52,  "title": "Sunset Blvd.",              "year": 1950, "rating": 8.4, "genre": ["Drama", "Film-Noir"],            "director": "Billy Wilder"},
    {"rank": 53,  "title": "Oldboy",                    "year": 2003, "rating": 8.4, "genre": ["Action", "Drama", "Mystery"],    "director": "Park Chan-wook"},
    {"rank": 54,  "title": "Dr. Strangelove",           "year": 1964, "rating": 8.4, "genre": ["Comedy", "War"],                 "director": "Stanley Kubrick"},
    {"rank": 55,  "title": "Princess Mononoke",         "year": 1997, "rating": 8.4, "genre": ["Animation", "Action", "Adventure"], "director": "Hayao Miyazaki"},
    {"rank": 56,  "title": "Coco",                      "year": 2017, "rating": 8.4, "genre": ["Animation", "Adventure", "Comedy"], "director": "Lee Unkrich"},
    {"rank": 57,  "title": "Raiders of the Lost Ark",   "year": 1981, "rating": 8.4, "genre": ["Action", "Adventure"],           "director": "Steven Spielberg"},
    {"rank": 58,  "title": "Come and See",              "year": 1985, "rating": 8.4, "genre": ["Drama", "War"],                  "director": "Elem Klimov"},
    {"rank": 59,  "title": "Witness for the Prosecution", "year": 1957, "rating": 8.4, "genre": ["Crime", "Drama", "Mystery"],  "director": "Billy Wilder"},
    {"rank": 60,  "title": "Like Stars on Earth",       "year": 2007, "rating": 8.4, "genre": ["Drama", "Family"],               "director": "Aamir Khan"},
    {"rank": 61,  "title": "2001: A Space Odyssey",     "year": 1968, "rating": 8.3, "genre": ["Adventure", "Sci-Fi"],           "director": "Stanley Kubrick"},
    {"rank": 62,  "title": "No Country for Old Men",    "year": 2007, "rating": 8.2, "genre": ["Crime", "Drama", "Thriller"],    "director": "Joel Coen"},
    {"rank": 63,  "title": "Reservoir Dogs",            "year": 1992, "rating": 8.3, "genre": ["Crime", "Drama", "Thriller"],    "director": "Quentin Tarantino"},
    {"rank": 64,  "title": "Toy Story",                 "year": 1995, "rating": 8.3, "genre": ["Animation", "Adventure", "Comedy"], "director": "John Lasseter"},
    {"rank": 65,  "title": "Das Boot",                  "year": 1981, "rating": 8.3, "genre": ["Drama", "War"],                  "director": "Wolfgang Petersen"},
    {"rank": 66,  "title": "Bicycle Thieves",           "year": 1948, "rating": 8.3, "genre": ["Drama"],                         "director": "Vittorio De Sica"},
    {"rank": 67,  "title": "Up",                        "year": 2009, "rating": 8.3, "genre": ["Animation", "Adventure", "Comedy"], "director": "Pete Docter"},
    {"rank": 68,  "title": "Good Will Hunting",         "year": 1997, "rating": 8.3, "genre": ["Drama", "Romance"],              "director": "Gus Van Sant"},
    {"rank": 69,  "title": "Toy Story 3",               "year": 2010, "rating": 8.3, "genre": ["Animation", "Adventure", "Comedy"], "director": "Lee Unkrich"},
    {"rank": 70,  "title": "Full Metal Jacket",         "year": 1987, "rating": 8.3, "genre": ["Drama", "War"],                  "director": "Stanley Kubrick"},
    {"rank": 71,  "title": "Lawrence of Arabia",        "year": 1962, "rating": 8.3, "genre": ["Adventure", "Biography", "Drama"], "director": "David Lean"},
    {"rank": 72,  "title": "The Apartment",             "year": 1960, "rating": 8.3, "genre": ["Comedy", "Drama", "Romance"],    "director": "Billy Wilder"},
    {"rank": 73,  "title": "Heat",                      "year": 1995, "rating": 8.3, "genre": ["Action", "Crime", "Drama"],      "director": "Michael Mann"},
    {"rank": 74,  "title": "Eternal Sunshine of the Spotless Mind", "year": 2004, "rating": 8.3, "genre": ["Drama", "Romance", "Sci-Fi"], "director": "Michel Gondry"},
    {"rank": 75,  "title": "Avengers: Infinity War",    "year": 2018, "rating": 8.4, "genre": ["Action", "Adventure", "Sci-Fi"], "director": "Anthony Russo"},
    {"rank": 76,  "title": "The Dark Knight Rises",     "year": 2012, "rating": 8.4, "genre": ["Action", "Drama"],               "director": "Christopher Nolan"},
    {"rank": 77,  "title": "Requiem for a Dream",       "year": 2000, "rating": 8.3, "genre": ["Drama"],                         "director": "Darren Aronofsky"},
    {"rank": 78,  "title": "Braveheart",                "year": 1995, "rating": 8.3, "genre": ["Biography", "Drama", "History"], "director": "Mel Gibson"},
    {"rank": 79,  "title": "Inglourious Basterds",      "year": 2009, "rating": 8.3, "genre": ["Adventure", "Drama", "War"],     "director": "Quentin Tarantino"},
    {"rank": 80,  "title": "Monty Python and the Holy Grail", "year": 1975, "rating": 8.2, "genre": ["Adventure", "Comedy", "Fantasy"], "director": "Terry Gilliam"},
    {"rank": 81,  "title": "A Beautiful Mind",          "year": 2001, "rating": 8.2, "genre": ["Biography", "Drama"],            "director": "Ron Howard"},
    {"rank": 82,  "title": "The Wolf of Wall Street",   "year": 2013, "rating": 8.2, "genre": ["Biography", "Comedy", "Crime"],  "director": "Martin Scorsese"},
    {"rank": 83,  "title": "Indiana Jones and the Last Crusade", "year": 1989, "rating": 8.2, "genre": ["Action", "Adventure"],  "director": "Steven Spielberg"},
    {"rank": 84,  "title": "Cinema Paradiso",           "year": 1988, "rating": 8.5, "genre": ["Drama", "Romance"],              "director": "Giuseppe Tornatore"},
    {"rank": 85,  "title": "Catch Me If You Can",       "year": 2002, "rating": 8.1, "genre": ["Biography", "Crime", "Drama"],   "director": "Steven Spielberg"},
    {"rank": 86,  "title": "The Truman Show",           "year": 1998, "rating": 8.2, "genre": ["Comedy", "Drama"],               "director": "Peter Weir"},
    {"rank": 87,  "title": "Vertigo",                   "year": 1958, "rating": 8.3, "genre": ["Mystery", "Romance", "Thriller"], "director": "Alfred Hitchcock"},
    {"rank": 88,  "title": "Rear Window",               "year": 1954, "rating": 8.5, "genre": ["Mystery", "Thriller"],           "director": "Alfred Hitchcock"},
    {"rank": 89,  "title": "Spotlight",                 "year": 2015, "rating": 8.1, "genre": ["Biography", "Crime", "Drama"],   "director": "Tom McCarthy"},
    {"rank": 90,  "title": "Gran Torino",               "year": 2008, "rating": 8.1, "genre": ["Drama"],                         "director": "Clint Eastwood"},
    {"rank": 91,  "title": "The Intouchables",          "year": 2011, "rating": 8.5, "genre": ["Biography", "Comedy", "Drama"],  "director": "Olivier Nakache"},
    {"rank": 92,  "title": "3 Idiots",                  "year": 2009, "rating": 8.4, "genre": ["Comedy", "Drama"],               "director": "Rajkumar Hirani"},
    {"rank": 93,  "title": "Amélie",                    "year": 2001, "rating": 8.3, "genre": ["Comedy", "Romance"],             "director": "Jean-Pierre Jeunet"},
    {"rank": 94,  "title": "The Great Escape",          "year": 1963, "rating": 8.2, "genre": ["Adventure", "Drama", "War"],     "director": "John Sturges"},
    {"rank": 95,  "title": "Hachi: A Dog's Tale",       "year": 2009, "rating": 8.1, "genre": ["Drama", "Family"],               "director": "Lasse Hallstrom"},
    {"rank": 96,  "title": "The Secret in Their Eyes",  "year": 2009, "rating": 8.2, "genre": ["Crime", "Drama", "Mystery"],     "director": "Juan José Campanella"},
    {"rank": 97,  "title": "Avengers: Endgame",         "year": 2019, "rating": 8.4, "genre": ["Action", "Adventure", "Drama"],  "director": "Anthony Russo"},
    {"rank": 98,  "title": "The Hunt",                  "year": 2012, "rating": 8.3, "genre": ["Drama"],                         "director": "Thomas Vinterberg"},
    {"rank": 99,  "title": "Blade Runner 2049",         "year": 2017, "rating": 8.0, "genre": ["Action", "Drama", "Mystery"],    "director": "Denis Villeneuve"},
    {"rank": 100, "title": "Gone with the Wind",        "year": 1939, "rating": 8.2, "genre": ["Drama", "History", "Romance"],   "director": "Victor Fleming"},
]


@mcp.tool()
def get_top_movies(limit: int = 10) -> str:
    """Return the top N movies from the IMDB Top 100 list."""
    limit = max(1, min(limit, 100))
    lines = [f"Top {limit} IMDB Movies\n{'='*40}"]
    for m in MOVIES[:limit]:
        genres = ", ".join(m["genre"])
        lines.append(f"#{m['rank']:>3}  {m['title']} ({m['year']})  ⭐{m['rating']}  [{genres}]  — {m['director']}")
    return "\n".join(lines)


@mcp.tool()
def search_by_genre(genre: str) -> str:
    """Find movies that belong to a specific genre (e.g. Drama, Action, Sci-Fi, Horror)."""
    genre_lower = genre.lower()
    matches = [m for m in MOVIES if any(g.lower() == genre_lower for g in m["genre"])]
    if not matches:
        return f"No movies found for genre '{genre}'."
    lines = [f"Movies in genre: {genre.title()}\n{'='*40}"]
    for m in matches:
        lines.append(f"#{m['rank']:>3}  {m['title']} ({m['year']})  ⭐{m['rating']}  — {m['director']}")
    return "\n".join(lines)


@mcp.tool()
def search_by_director(director: str) -> str:
    """Find all movies by a specific director."""
    director_lower = director.lower()
    matches = [m for m in MOVIES if director_lower in m["director"].lower()]
    if not matches:
        return f"No movies found for director '{director}'."
    lines = [f"Movies by {director.title()}\n{'='*40}"]
    for m in matches:
        genres = ", ".join(m["genre"])
        lines.append(f"#{m['rank']:>3}  {m['title']} ({m['year']})  ⭐{m['rating']}  [{genres}]")
    return "\n".join(lines)


@mcp.tool()
def get_movie_details(title: str) -> str:
    """Get full details of a movie by its title (partial match supported)."""
    title_lower = title.lower()
    matches = [m for m in MOVIES if title_lower in m["title"].lower()]
    if not matches:
        return f"No movie found matching '{title}'."
    lines = []
    for m in matches:
        genres = ", ".join(m["genre"])
        lines.append(
            f"Title    : {m['title']}\n"
            f"Year     : {m['year']}\n"
            f"Rating   : ⭐ {m['rating']} / 10\n"
            f"Genre    : {genres}\n"
            f"Director : {m['director']}\n"
            f"IMDB Rank: #{m['rank']}\n"
            f"{'-'*40}"
        )
    return "\n".join(lines)


@mcp.tool()
def recommend_movies(genre: str = "", min_rating: float = 8.0, limit: int = 5) -> str:
    """
    Recommend movies filtered by genre and minimum rating.
    Leave genre empty to recommend across all genres.
    """
    results = MOVIES
    if genre:
        genre_lower = genre.lower()
        results = [m for m in results if any(g.lower() == genre_lower for g in m["genre"])]
    results = [m for m in results if m["rating"] >= min_rating]
    results = results[:limit]
    if not results:
        return f"No recommendations found for genre='{genre}' with rating >= {min_rating}."
    tag = f" in {genre.title()}" if genre else ""
    lines = [f"Top {len(results)} Recommendations{tag} (min rating {min_rating})\n{'='*40}"]
    for m in results:
        genres = ", ".join(m["genre"])
        lines.append(f"#{m['rank']:>3}  {m['title']} ({m['year']})  ⭐{m['rating']}  [{genres}]  — {m['director']}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
