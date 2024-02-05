# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:45:06 2024

@author: MManitshana
"""

import pandas as pd
import matplotlib.pyplot as plt 
from collections import Counter

# Load the dataset/data frame
file_path = "movie_dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows to show the data
print(df.head())

# Check for missing values and handle them
print(df.isnull().sum())

# For numerical columns, fill missing values with mean
df['Runtime (Minutes)'] = df['Runtime (Minutes)'].fillna(df['Runtime (Minutes)'].mean())
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].mean())

# For categorical columns, fill missing values with the most common value
df['Genre'] = df['Genre'].fillna(df['Genre'].mode()[0])

# Drop rows with missing values in specific columns
df = df.dropna(subset=['Director'])

# Rename columns to remove spaces
df.columns = df.columns.str.replace(' ', '_')

# Perform EDA
print(df.describe())

# Plot histograms for numerical columns
df[['Runtime_(Minutes)', 'Rating', 'Revenue_(Millions)', 'Metascore']].hist(figsize=(12, 8))

plt.show()

#Highest rated movie
highest_rated_movie = df.loc[df['Rating'].idxmax()]
print("Highest Rated Movie:")
print(highest_rated_movie[['Title', 'Rating']])

#Average Revenue
average_revenue = df['Revenue_(Millions)'].mean()
print("Average Revenue of All Movies: $", round(average_revenue, 2))

# Specify the year range
start_year = 2015
end_year = 2017

# Filter movies for the given year range
filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]

# Exclude rows with missing values in 'Revenue (Millions)'
filtered_df = filtered_df.dropna(subset=['Revenue_(Millions)'])

# Check if there are movies for the given year range
if not filtered_df.empty:
    # Calculate the average revenue
    average_revenue_range = filtered_df['Revenue_(Millions)'].mean()
    print(f"Average Revenue of Movies from {start_year} to {end_year}: ${round(average_revenue_range, 2)}")
else:
    print(f"No movies found for the year range {start_year} to {end_year}.")

# Specify the target year
target_year = 2016

# Filter movies for the given year
movies_2016 = df[df['Year'] == target_year]

# Count the number of movies released in 2016
num_movies_2016 = len(movies_2016)

print(f"Number of movies released in {target_year}: {num_movies_2016}")   

# Specify the director's name
director_name = 'Christopher Nolan'

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == director_name]

# Count the number of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

print(f"Number of movies directed by {director_name}: {num_nolan_movies}")
print(f"Median rating of movies directed by {director_name}: {median_rating_nolan_movies}")

# Specify the minimum rating
min_rating = 8.0

# Filter movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= min_rating]

# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

print(f"Number of movies with a rating of at least {min_rating}: {num_high_rated_movies}")

# Group by 'Year' and calculate the average rating for each year
average_rating_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

print(f"Year with the highest average rating: {year_highest_average_rating}, Average Rating: {highest_average_rating}")

# Specify the years
old_year = 2006
new_year = 2016

# Filter movies for the old year
old_year_movies = df[df['Year'] == old_year]

# Filter movies for the new year
new_year_movies = df[df['Year'] == new_year]

# Count the number of movies for each year
num_movies_old_year = len(old_year_movies)
num_movies_new_year = len(new_year_movies)

# Calculate the percentage increase
percentage_increase = ((num_movies_new_year - num_movies_old_year) / num_movies_old_year) * 100

print(f"Percentage increase in number of movies between {old_year} and {new_year}: {percentage_increase:.2f}%")

# Combine all actor names from the 'Actors' column
all_actors = ', '.join(df['Actors'])

# Split the combined string into a list of actor names
all_actor_list = [actor.strip() for actor in all_actors.split(',')]

# Count the occurrences of each actor
actor_counts = Counter(all_actor_list)

# Find the most common actor
most_common_actor, count_most_common_actor = actor_counts.most_common(1)[0]

print(f"The most common actor in all movies is: {most_common_actor}, with {count_most_common_actor} occurrences.")

# Combine all genre names from the 'Genre' column
all_genres = ', '.join(df['Genre'])

# Split the combined string into a list of genre names
all_genre_list = [genre.strip() for genre in all_genres.split(',')]

# Get the unique genres
unique_genres = set(all_genre_list)

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print(f"There are {num_unique_genres} unique genres in the dataset.")

# Selecting numerical columns for correlation analysis
numerical_columns = ['Runtime_(Minutes)', 'Rating', 'Votes', 'Revenue_(Millions)', 'Metascore']

# Calculate the correlation matrix
correlation_matrix = df[numerical_columns].corr()

print("Correlation Matrix:")
print(correlation_matrix)