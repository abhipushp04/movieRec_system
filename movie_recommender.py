import pandas as pd
import numpy as np
import random

class MovieRecommender:
    def __init__(self):
        # Load and prepare the data
        self.movies_df = pd.read_csv("movies.csv")
        self.ratings_df = pd.read_csv("ratings.csv")
        self.prepare_data()

    def prepare_data(self):
        # Merge movies and ratings dataframes
        self.merged_df = pd.merge(self.ratings_df, self.movies_df, on='movieId')
        
        # Create ratings mean count dataframe
        self.movie_ratings = pd.DataFrame(self.merged_df.groupby('title')['rating'].mean())
        self.movie_ratings['rating_count'] = self.merged_df.groupby('title')['rating'].count()
        
        # Sort by rating count to get popular movies
        self.popular_movies = self.movie_ratings[self.movie_ratings['rating_count'] > 50].sort_values('rating', ascending=False)

    def get_top_10_movies(self):
        """Returns top 10 movies based on ratings and popularity"""
        top_10 = self.popular_movies.head(10)
        return [(title, round(row['rating'], 2), int(row['rating_count'])) 
                for title, row in top_10.iterrows()]

    def get_movies_by_letter(self, letter):
        """Returns top 10 movies starting with the given letter"""
        letter_movies = self.popular_movies[self.popular_movies.index.str.startswith(letter.upper()) | 
                                          self.popular_movies.index.str.startswith(letter.lower())]
        top_10_letter = letter_movies.head(10)
        
        if len(top_10_letter) == 0:
            return []
        
        return [(title, round(row['rating'], 2), int(row['rating_count'])) 
                for title, row in top_10_letter.iterrows()]

    def get_random_movie(self):
        """Returns a random movie from the popular movies"""
        random_movie = self.popular_movies.sample(n=1)
        title = random_movie.index[0]
        rating = round(random_movie['rating'].iloc[0], 2)
        count = int(random_movie['rating_count'].iloc[0])
        return (title, rating, count)