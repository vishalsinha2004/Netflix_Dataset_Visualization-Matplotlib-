#s-1 import the libraries
import pandas as pd
import matplotlib.pyplot as plt 

#laod the data
df = pd.read_csv('netflix_titles.csv')
#clean data
df = df.dropna(subset=['type','release_year', 'rating','country', 'duration'])

# Convert 'release_year' to integer
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Number of Movies VS Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.savefig('movies_vs_shows.png')
plt.show() 

# Pie chart for Content Ratings
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content Ratings')
plt.tight_layout()
plt.savefig('content_ratings_pie.png')
plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)

# Histogram of Movie Durations
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Durations')    
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_durations_histogram.png')
plt.show()

# Scatter plot for Release Year vs Number of Shows
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='red')
plt.title('Release Year vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout
plt.savefig('release_years_scatter.png')
plt.show()

# Top 10 Countries by Number of Shows
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_countries.png')
plt.show()


content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12, 5))

#first subplot:movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')   
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

#second subplot:TV shows
ax[0].plot(content_by_year.index, content_by_year['TV Show'], color='orange')   
ax[0].set_title('TV Shows Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

fig.suptitle('comparison of Movies and TV Shows Released Over Year')


plt.tight_layout()
plt.savefig('movies_vs_tvshows_comparison.png')
plt.show()