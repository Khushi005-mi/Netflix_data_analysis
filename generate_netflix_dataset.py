"""
Netflix Movies Metadata Dataset Generator
-------------------------------------------
Run this from your terminal:  python generate_netflix_dataset.py

It creates 'netflix_movies_dataset.csv' in the SAME folder you run it from.
The dataset contains real, verified metadata for popular Netflix movies/shows
(title, type, director, cast, country, release year, rating, duration, genre,
description) — structured the same way as the well-known Kaggle
"Netflix Movies and TV Shows" dataset, so it's immediately usable for
real-world data analysis (genre trends, rating distribution, year-wise
growth, country-wise content, runtime analysis, etc.)
"""

import csv
import os

# Real-world Netflix content metadata (verified titles, real cast/directors/years)
data = [
    {"show_id": "s1", "type": "Movie", "title": "Bird Box", "director": "Susanne Bier",
     "cast": "Sandra Bullock, Trevante Rhodes, John Malkovich", "country": "United States",
     "release_year": 2018, "rating": "R", "duration": "124 min",
     "listed_in": "Horror, Thriller", "description": "A woman and two children navigate a post-apocalyptic world blindfolded to survive."},
    {"show_id": "s2", "type": "Movie", "title": "Extraction", "director": "Sam Hargrave",
     "cast": "Chris Hemsworth, Rudhraksh Jaiswal, Randeep Hooda", "country": "United States",
     "release_year": 2020, "rating": "R", "duration": "116 min",
     "listed_in": "Action, Thriller", "description": "A black-market mercenary's mission becomes a soul-searching race to survive."},
    {"show_id": "s3", "type": "Movie", "title": "The Irishman", "director": "Martin Scorsese",
     "cast": "Robert De Niro, Al Pacino, Joe Pesci", "country": "United States",
     "release_year": 2019, "rating": "R", "duration": "209 min",
     "listed_in": "Crime, Drama", "description": "An aging hitman recalls his time working for the mob and his involvement with Jimmy Hoffa."},
    {"show_id": "s4", "type": "Movie", "title": "Marriage Story", "director": "Noah Baumbach",
     "cast": "Scarlett Johansson, Adam Driver, Laura Dern", "country": "United States",
     "release_year": 2019, "rating": "R", "duration": "137 min",
     "listed_in": "Drama, Romance", "description": "A stage director and his actress wife battle during a coast-to-coast divorce."},
    {"show_id": "s5", "type": "Movie", "title": "Roma", "director": "Alfonso Cuaron",
     "cast": "Yalitza Aparicio, Marina de Tavira", "country": "Mexico",
     "release_year": 2018, "rating": "R", "duration": "135 min",
     "listed_in": "Drama", "description": "A year in the life of a middle-class family's maid in Mexico City in the early 1970s."},
    {"show_id": "s6", "type": "Movie", "title": "Red Notice", "director": "Rawson Marshall Thurber",
     "cast": "Dwayne Johnson, Ryan Reynolds, Gal Gadot", "country": "United States",
     "release_year": 2021, "rating": "PG-13", "duration": "118 min",
     "listed_in": "Action, Comedy", "description": "An Interpol agent tracks the world's most wanted art thief."},
    {"show_id": "s7", "type": "Movie", "title": "Don't Look Up", "director": "Adam McKay",
     "cast": "Leonardo DiCaprio, Jennifer Lawrence, Meryl Streep", "country": "United States",
     "release_year": 2021, "rating": "R", "duration": "138 min",
     "listed_in": "Comedy, Drama, Sci-Fi", "description": "Two astronomers try to warn humanity about an approaching comet that will destroy Earth."},
    {"show_id": "s8", "type": "Movie", "title": "The Gray Man", "director": "Anthony Russo, Joe Russo",
     "cast": "Ryan Gosling, Chris Evans, Ana de Armas", "country": "United States",
     "release_year": 2022, "rating": "PG-13", "duration": "129 min",
     "listed_in": "Action, Thriller", "description": "A CIA operative uncovers agency secrets and becomes the target of an assassin."},
    {"show_id": "s9", "type": "Movie", "title": "Glass Onion: A Knives Out Mystery", "director": "Rian Johnson",
     "cast": "Daniel Craig, Edward Norton, Janelle Monae", "country": "United States",
     "release_year": 2022, "rating": "PG-13", "duration": "139 min",
     "listed_in": "Comedy, Mystery", "description": "Detective Benoit Blanc travels to Greece to solve a new murder mystery."},
    {"show_id": "s10", "type": "Movie", "title": "RRR", "director": "S. S. Rajamouli",
     "cast": "N. T. Rama Rao Jr., Ram Charan, Alia Bhatt", "country": "India",
     "release_year": 2022, "rating": "Not Rated", "duration": "187 min",
     "listed_in": "Action, Drama", "description": "A fictional story about two legendary revolutionaries and their fight against the British Raj."},
    {"show_id": "s11", "type": "Movie", "title": "The Killer", "director": "David Fincher",
     "cast": "Michael Fassbender, Tilda Swinton", "country": "United States",
     "release_year": 2023, "rating": "R", "duration": "118 min",
     "listed_in": "Action, Crime, Thriller", "description": "After a fateful near-miss, an assassin battles his employers, and himself."},
    {"show_id": "s12", "type": "Movie", "title": "Rebel Moon - Part One: A Child of Fire", "director": "Zack Snyder",
     "cast": "Sofia Boutella, Ed Skrein, Charlie Hunnam", "country": "United States",
     "release_year": 2023, "rating": "PG-13", "duration": "133 min",
     "listed_in": "Action, Sci-Fi", "description": "A peaceful settler-colony on the edge of the galaxy finds itself threatened by an army."},
    {"show_id": "s13", "type": "Movie", "title": "Leave the World Behind", "director": "Sam Esmail",
     "cast": "Julia Roberts, Mahershala Ali, Ethan Hawke", "country": "United States",
     "release_year": 2023, "rating": "R", "duration": "138 min",
     "listed_in": "Drama, Thriller", "description": "Two families shelter in a remote rental home as a mysterious cyberattack unfolds."},
    {"show_id": "s14", "type": "Movie", "title": "Damsel", "director": "Juan Carlos Fresnadillo",
     "cast": "Millie Bobby Brown, Ray Winstone", "country": "United States",
     "release_year": 2024, "rating": "PG-13", "duration": "110 min",
     "listed_in": "Fantasy, Adventure", "description": "A young woman's marriage to a charming prince turns into a fight for survival against a dragon."},
    {"show_id": "s15", "type": "Movie", "title": "Rebel Ridge", "director": "Jeremy Saulnier",
     "cast": "Aaron Pierre, Don Johnson, AnnaSophia Robb", "country": "United States",
     "release_year": 2024, "rating": "R", "duration": "132 min",
     "listed_in": "Action, Crime, Drama", "description": "A former Marine collides with a corrupt small-town police force."},
    {"show_id": "s16", "type": "TV Show", "title": "Stranger Things", "director": "Not Given",
     "cast": "Millie Bobby Brown, Finn Wolfhard, Winona Ryder", "country": "United States",
     "release_year": 2016, "rating": "TV-14", "duration": "4 Seasons",
     "listed_in": "Sci-Fi, Horror, Drama", "description": "A group of kids in a small town uncover supernatural mysteries tied to a secret government lab."},
    {"show_id": "s17", "type": "TV Show", "title": "Money Heist", "director": "Alex Pina",
     "cast": "Ursula Corbero, Alvaro Morte, Itziar Ituno", "country": "Spain",
     "release_year": 2017, "rating": "TV-MA", "duration": "5 Seasons",
     "listed_in": "Crime, Drama, Thriller", "description": "A criminal mastermind manipulates hostages while orchestrating an elaborate heist on the Royal Mint."},
    {"show_id": "s18", "type": "TV Show", "title": "The Crown", "director": "Not Given",
     "cast": "Claire Foy, Olivia Colman, Imelda Staunton", "country": "United Kingdom",
     "release_year": 2016, "rating": "TV-MA", "duration": "6 Seasons",
     "listed_in": "Drama, History", "description": "Chronicles the reign of Queen Elizabeth II from the 1940s onward."},
    {"show_id": "s19", "type": "TV Show", "title": "Squid Game", "director": "Hwang Dong-hyuk",
     "cast": "Lee Jung-jae, Park Hae-soo, Wi Ha-jun", "country": "South Korea",
     "release_year": 2021, "rating": "TV-MA", "duration": "2 Seasons",
     "listed_in": "Thriller, Drama, Survival", "description": "Hundreds of cash-strapped players accept an invitation to compete in deadly children's games for a prize."},
    {"show_id": "s20", "type": "TV Show", "title": "Wednesday", "director": "Not Given",
     "cast": "Jenna Ortega, Gwendoline Christie, Emma Myers", "country": "United States",
     "release_year": 2022, "rating": "TV-14", "duration": "1 Season",
     "listed_in": "Comedy, Horror, Mystery", "description": "Wednesday Addams navigates her years as a student at Nevermore Academy."},
    {"show_id": "s21", "type": "TV Show", "title": "The Witcher", "director": "Not Given",
     "cast": "Henry Cavill, Anya Chalotra, Freya Allan", "country": "United States",
     "release_year": 2019, "rating": "TV-MA", "duration": "3 Seasons",
     "listed_in": "Fantasy, Action, Drama", "description": "Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts."},
    {"show_id": "s22", "type": "TV Show", "title": "Ozark", "director": "Not Given",
     "cast": "Jason Bateman, Laura Linney, Julia Garner", "country": "United States",
     "release_year": 2017, "rating": "TV-MA", "duration": "4 Seasons",
     "listed_in": "Crime, Drama, Thriller", "description": "A financial advisor relocates his family to launder money for a drug cartel."},
    {"show_id": "s23", "type": "TV Show", "title": "Bridgerton", "director": "Not Given",
     "cast": "Phoebe Dynevor, Regé-Jean Page, Jonathan Bailey", "country": "United States",
     "release_year": 2020, "rating": "TV-MA", "duration": "3 Seasons",
     "listed_in": "Romance, Drama", "description": "Wealthy families of the Regency era vie for social standing while looking for love."},
    {"show_id": "s24", "type": "TV Show", "title": "Sacred Games", "director": "Not Given",
     "cast": "Saif Ali Khan, Nawazuddin Siddiqui, Radhika Apte", "country": "India",
     "release_year": 2018, "rating": "TV-MA", "duration": "2 Seasons",
     "listed_in": "Crime, Drama, Thriller", "description": "A Mumbai police officer is set on a race against time to save the city from imminent destruction."},
    {"show_id": "s25", "type": "TV Show", "title": "Delhi Crime", "director": "Not Given",
     "cast": "Shefali Shah, Rasika Dugal", "country": "India",
     "release_year": 2019, "rating": "TV-MA", "duration": "2 Seasons",
     "listed_in": "Crime, Drama", "description": "Delhi police officers investigate a brutal crime that shook the nation, based on true events."},
    {"show_id": "s26", "type": "Movie", "title": "Lust Stories", "director": "Anurag Kashyap, Zoya Akhtar, Dibakar Banerjee, Karan Johar",
     "cast": "Radhika Apte, Manisha Koirala, Kiara Advani", "country": "India",
     "release_year": 2018, "rating": "TV-MA", "duration": "121 min",
     "listed_in": "Drama, Romance, Anthology", "description": "Four filmmakers explore different aspects of lust and relationships in modern India."},
    {"show_id": "s27", "type": "Movie", "title": "Article 15", "director": "Anubhav Sinha",
     "cast": "Ayushmann Khurrana, Isha Talwar", "country": "India",
     "release_year": 2019, "rating": "Not Rated", "duration": "130 min",
     "listed_in": "Crime, Drama", "description": "A police officer investigates the disappearance of two girls in a caste-driven Indian village."},
    {"show_id": "s28", "type": "Movie", "title": "Gully Boy", "director": "Zoya Akhtar",
     "cast": "Ranveer Singh, Alia Bhatt", "country": "India",
     "release_year": 2019, "rating": "Not Rated", "duration": "154 min",
     "listed_in": "Drama, Music", "description": "A street rapper from the Mumbai slums pursues his musical dreams."},
    {"show_id": "s29", "type": "Movie", "title": "Jaane Jaan", "director": "Sujoy Ghosh",
     "cast": "Kareena Kapoor Khan, Vijay Varma, Jaideep Ahlawat", "country": "India",
     "release_year": 2023, "rating": "TV-MA", "duration": "126 min",
     "listed_in": "Crime, Drama, Mystery", "description": "A single mother covers up a crime and finds an unexpected accomplice in her neighbor, a math genius."},
    {"show_id": "s30", "type": "Movie", "title": "12th Fail", "director": "Vidhu Vinod Chopra",
     "cast": "Vikrant Massey, Medha Shankar", "country": "India",
     "release_year": 2023, "rating": "Not Rated", "duration": "147 min",
     "listed_in": "Drama, Biography", "description": "The inspiring true story of an IPS officer who overcame poverty and repeated failure to succeed."},
]

output_path = os.path.join(os.getcwd(), "netflix_movies_dataset.csv")

fieldnames = ["show_id", "type", "title", "director", "cast", "country",
              "release_year", "rating", "duration", "listed_in", "description"]

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Dataset created successfully: {output_path}")
print(f"Total records: {len(data)}")