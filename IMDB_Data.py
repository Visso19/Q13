# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:26:23 2024

@author: ObakachiV
"""

"""
import pandas as pd

df = pd.read_csv("movie_dataset.csv")

x = df["Revenue (Millions)"].mean()
y = df["Metascore"].mean()


df["Revenue (Millions)"].fillna(x, inplace = True) 


df["Metascore"].fillna(y, inplace = True) 
"""

"""

df = df.to_csv('cleaned_data.csv', index=False)

"""


import pandas as pd

df = pd.read_csv("C:/Users/obakachiv/CSS Project - IMDB Data/cleaned_dataset.csv")

highest_rated_movie = df.loc[df['Rating'].idxmax()]

print(highest_rated_movie)

average_revenue = df['Revenue (Millions)'].mean()

print("Average Revenue (Millions) of All Movies:", average_revenue)


filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

average_revenue_2015_to_2017 = filtered_df['Revenue (Millions)'].mean()

print("Average Revenue (Millions) of Movies from 2015 to 2017:", average_revenue_2015_to_2017)

movies_2016 = df[df['Year'] == 2016]

number_of_movies_2016 = len(movies_2016)

print("Number of Movies Released in 2016:", number_of_movies_2016)

nolan_movies = df[df['Director'] == 'Christopher Nolan']

number_of_nolan_movies = len(nolan_movies)

print("Number of Movies Directed by Christopher Nolan:", number_of_nolan_movies)

high_rated_movies = df[df['Rating'] >= 8.0]

number_of_high_rated_movies = len(high_rated_movies)

print("Number of Movies with a Rating of at Least 8.0:", number_of_high_rated_movies)

nolan_movies = df[df['Director'] == 'Christopher Nolan']

median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)


average_ratings_by_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_ratings_by_year.idxmax()
highest_average_rating = average_ratings_by_year.max()

print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}")


movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

number_of_movies_2006 = len(movies_2006)
number_of_movies_2016 = len(movies_2016)

percentage_increase = ((number_of_movies_2016 - number_of_movies_2006) / number_of_movies_2006) * 100

print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")


from collections import Counter

# Assuming df is your DataFrame with an 'Actors' column
# Replace 'Actors' with the actual column name in your dataset
actors_series = df['Actors'].str.split(',').explode()

# Count the occurrences of each actor
actors_count = Counter(actors_series)

# Find the most common actor
most_common_actor, count_most_common_actor = actors_count.most_common(1)[0]

print(f"The most common actor in all movies is {most_common_actor} with {count_most_common_actor} appearances.")

genres_series = df['Genre'].str.split(',').explode()
number_of_unique_genres = genres_series.nunique()

print(f"There are {number_of_unique_genres} unique genres in the dataset.")

# Assuming df is your DataFrame with numerical features
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Deduce insights
insight_1 = "There is a strong positive correlation between feature A and feature B."
insight_2 = "Feature C has a negative correlation with Feature D."
insight_3 = "No significant correlation is observed between Feature E and other features."
insight_4 = "Feature F and Feature G have a moderate positive correlation."
insight_5 = "Feature H has a strong negative correlation with Feature I."

print("\nInsights:")
print(insight_1)
print(insight_2)
print(insight_3)
print(insight_4)
print(insight_5)




















