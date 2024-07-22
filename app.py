from fastapi import FastAPI, HTTPException
import pickle
import pandas as pd
import requests
import gdown
import os

app = FastAPI()

# Function to download the file from Google Drive
def download_file_from_google_drive(url, output):
    gdown.download(url, output, quiet=False)

# Define file paths
similarity_file_url = 'https://drive.google.com/uc?id=1ojbk7Oic_vmyyGZ5KfXnmog4upExOOQ4'
similarity_file_path = 'similarity.pkl'
movies_file_path = 'movies.pkl'

# Download similarity.pkl file only if it does not exist
if not os.path.exists(similarity_file_path):
    download_file_from_google_drive(similarity_file_url, similarity_file_path)

# Load movies and similarity data from pickled files
with open(movies_file_path, 'rb') as file:
    movies = pickle.load(file)

with open(similarity_file_path, 'rb') as file:
    similarity = pickle.load(file)

@app.get('/')
def read_root():
    return {'message': 'Welcome to the Movie Recommender API'}

@app.get('/recommend/{movie_title}')
def recommend_movies(movie_title: str):
    try:
        names, posters = recommended_movies(movie_title)
        recommendations = [{"name": name, "poster": poster} for name, poster in zip(names, posters)]
        return {"recommendations": recommendations}
    except IndexError:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    
@app.get('/movies')
def get_all_movies():
    return {"movies":movies['title'].tolist()}

def recommended_movies(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        raise HTTPException(status_code=404, detail="Movie not found in my database")

    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_list = []
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_list.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))

    return recommended_movie_list, recommend_movies_poster

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
