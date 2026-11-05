from math import ceil

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]



def average_rating(movies: list[dict]) -> float:

    """Возвращает среднюю оценку по каталогу, округлённую до 1 знака."""

    if not movies:
        raise ValueError("The list is empty")

    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)



def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple[int, int, int]:

    """Возвращает самый старый фильм в годах, самый новый и среднее, округленное до целого."""

    if not movies:
        raise ValueError("The list is empty")

    oldest = min(movies, key=lambda m: m["year"])
    newest = max(movies, key=lambda m: m["year"])

    oldest_age = current_year - oldest["year"]
    newest_age = current_year - newest["year"]

    total_age = sum(current_year - movie["year"] for movie in movies)
    average = ceil(total_age / len(movies))

    return (oldest_age, newest_age, average)



def duration_in_hours(minutes: int) -> str:

    """Переводит минуты в строку формата "2ч 35м"."""

    if not isinstance(minutes, int):
        raise TypeError("Minutes must be int")

    return f"{minutes//60}ч {minutes%60}м"



def rating_tier(rating: float) -> str:

    """Возвращает категорию оценки: шедевр / хорошо / средне / слабо."""

    if not isinstance(rating, (int, float)):
        raise TypeError("Rating must be int or float")

    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "слабо" if rating < 5 else "средне"



def decade_label(year: int) -> str:

    """Возвращает категорию: новые / недавние / старые."""

    if not isinstance(year, int):
        raise TypeError("Year must be int")

    match year:
        case _ if year > 2020:
            return "новый"
        case _ if 2015 <= year <= 2020:
            return "недавний"
        case _:
            return "старый"



def count_long_movies(movies: list[dict], threshold: int = 120) -> int:

    """Возвращает количество фильмов длиннее threshold."""

    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count



def normalize_title(title: str) -> str:

    """Приводит строку к формату Title Case."""

    if not isinstance(title, str):
        raise TypeError("Title must be str")

    words = title.split()

    res = []
    for word in words:
        res.append(word[0].upper() + word[1:].lower())
    return " ".join(res)



def make_slug(title: str) -> str:

    """Превращает нормализованное название в «слаг»."""

    if not isinstance(title, str):
        raise TypeError("Title must be str")

    return title.lower().replace(" ", "-")



def format_report_line(movie: dict) -> str:

    """Возвращает единую строку с описанием фильма."""

    if not isinstance(movie, dict):
        raise TypeError("Movie must be dict")

    title = movie["title"]
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'



def titles_sorted_by_rating(movies: list[dict]) -> list[str]:

    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""

    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)

    return [movie["title"] for movie in sorted_movies]



def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float]]:

    """Возвращает список из n кортежей (title, rating) - топ по рейтингу."""

    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)

    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]



def count_by_genre(movies: list[dict]) -> dict:

    """Возвращает словарь {жанр: количество фильмов}."""

    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts



def actor_filmography(movies: list[dict]) -> dict:

    """Возвращает словарь {актер: [список названий фильмов]}."""

    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if filmography.get(actor) is None:
                filmography[actor] = [movie["title"]]
            else:
                filmography[actor].append(movie["title"])

    return filmography







def main():
    #print(f"Средняя оценка по каталогу: {average_rating(movies)}")
    #print(f"Самый старый фильм в годах, самый новый и среднее: {catalog_age_stats(movies)}")
    #print(duration_in_hours(98))
    #print(rating_tier(4.9))
    #print(decade_label(2013))
    #print(count_long_movies(movies))

    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    i = 0
    while i < len(movies):
        movie = movies[i]
        if rating_tier(movie["rating"]) == "шедевр":
            print(f"\n{movie['title']} шедевр")
            break
        i += 1
    else:
        print("Шедевров не найдено")

    #print(normalize_title("wow os it"))
    #print(make_slug("Wow os Tt"))
    #print(format_report_line(movies[5]))
    #print(titles_sorted_by_rating(movies))
    #print(top_n_by_rating(movies))
    #print(count_by_genre(movies))
    #print(actor_filmography(movies))

    threshold = average_rating(movies)
    title_rating = {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > threshold}

    #print(title_rating)


if __name__ == "__main__":
    main()
