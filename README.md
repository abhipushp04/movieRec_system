# Movie Recommendation System

A Python-based movie recommendation system that suggests movies based on user ratings and preferences.

## Features

- View top 10 rated movies
- Find movies by starting letter
- Get personalized random movie recommendations
- Based on a dataset of 100,000+ ratings across 9,000+ movies by 600+ users

## How It Works

The recommendation system uses statistical filtering to provide suggestions:

### Popularity-Based Filtering
```python
quality_score = average_rating * (num_ratings / MIN_RATING_THRESHOLD)
```
- Movies must have >50 ratings to be considered
- Combines average rating with popularity
- Ensures recommendations are both highly rated and widely reviewed

## Dataset Requirements

The system expects two CSV files:
- `movies.csv`: movieId, title, genres
- `ratings.csv`: userId, movieId, rating, timestamp

## Sample outputs
![image](https://github.com/user-attachments/assets/cd3f8efe-f61b-427d-8955-9256f717f53c)

![image](https://github.com/user-attachments/assets/ddaf9710-de12-453d-88c0-2ecdb3a87a08)


