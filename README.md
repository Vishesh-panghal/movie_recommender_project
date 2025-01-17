
# Movie Recommender System

This project involves building a complete movie recommender system, which includes machine learning, API creation and deployment, and a Flutter app for visualization.



# Table of Contents

- Overview
- Machine Learning Model
- API development
- Flutter app
- Installation
- Contributing

# Overview

The Movie Recommender System project is divided into three main parts:

1. **Machine Learning Model**- Develop a machine learning model to recommend movies.
2. **API Development**- Create and host an API using FastAPI to serve the recommendations.
3. **Flutter App**- Build a Flutter app to visualize movie names and posters, and provide recommendations.


# Machine Learning Model

The machine learning component involves creating a model that can recommend movies based on user input. The model is trained on a dataset containing movie ratings and metadata.

### Steps

1. **Data Collection**-Gather a dataset containing movie ratings and metadata.[tmdb-5000 dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2. **Data Preprocessing**- Clean and preprocess the data for model training.
3. **Model Training**-Train a recommendation model using Stemming, Vectroization & cosine_similarity.
4. **Model Evaluation**-Evaluate the model's performance using metrics:- precision = correct_recommendations / total_recommendations.
5. **Export Model**- Export model using pickel.

### Tools and Libraries

- Python
- Pandas
- Numpy
- NLTK
- Sklearn


###
###
# API Development

Create a FastAPI application to serve the movie recommendations generated by the machine learning model.

### Steps

1. **FastAPI Setup**- Initialize a FastAPI project.
2. **Endpoints**- Create endpoints to handle requests for movie recommendations.
3. **Model Integration**-Integrate the trained machine learning model with the API using pkl files.
4. **Deployment**- Deploy the FastAPI application on Render.

### Tools and Libraries

- FastAPI
- Uvicorn
- Render

## Deployment

The API is hosted on Render and can be accessed at:
[link](https://movie-recommender-api-r7ig.onrender.com/docs)


## API Reference

#### Get all movies

```http
  GET /movies
```

#### Get recommendations

```http
  GET /recommended/${movie_title}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `movie_title`      | `string` | **Required** movie_title|



###
###

## Flutter App

Build a Flutter application to interact with the FastAPI and visualize the movie recommendations.

### Features

- Search for movies
- Display movie posters and names
- Get recommendations based on selected movies.
- ios/android

### Tools and Libraries

- Flutter
- Dart
- Cubit for state management
- Google fonts


###
###

## Installation

### Machine Learning Model

1. Clone the repository:
```bash
  git clone https://github.com/Vishesh-panghal/movie_recommender_project.git
```
2. Navigate to the Model directory:
```bash
  cd ml_model
```
3. Run the model training script:
```bash
  python Movie Recommender System.ipynb
```

### API Development

1. Navigate to the API directory:
```bash
  cd api
```
2. Install the necessary dependencies:
```bash
  pip install -r requirements.txt
```
3. Run the FastAPI application:
```bash
  uvicorn app:app --reload
```

### Flutter App

1. Navigate to the Flutter app directory:
```bash
  cd movie_recommender_App
```
2. Install the necessary dependencies:
```bash
  flutter pub get
```
3. Run the Flutter application:
```bash
  flutter run
```


### Usage
1. Start the FastAPI server.
2. Open the Flutter app and search for movies.
3. Select a movie to get recommendations and visualize the results.
## Contributing
Contributions are welcome! 
##


## Authors

- [@vishesh](https://panghal.tech)⏎


## Support

For support, email pvt.panghal@gmail.com.

