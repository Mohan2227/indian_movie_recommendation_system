import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:/Users/mayur/Desktop/movie-recommendation/IMDB-Movie-Data.csv")

df = df[['Title', 'Genre', 'Description']].dropna()
df['combined'] = df['Genre'] + " " + df['Description']

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend(movie_name):
    movie_name = movie_name.strip()

    if movie_name not in df['Title'].values:
        return ["Movie not found"]

    index = df[df['Title'] == movie_name].index[0]
    distances = list(enumerate(similarity[index]))
    movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    return [df.iloc[i[0]].Title for i in movies]