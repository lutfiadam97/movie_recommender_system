import streamlit as st
import pickle
import pandas as pd
import requests

# # recommendation system program

# def fetch_poster(movie_id):
#     api_key = "d0e15344d04efaed8617008869f8e984"
#     base_url = "https://api.themoviedb.org/3"

#     # movie_id = movie_id
#     image_url = f"{base_url}/movie/{movie_id}/popular?api_key={api_key}"
#     response = requests.get(image_url.format(movie_id))
#     image_data = response.json()
#     backdrops = image_data.get("backdrops", [])
#     posters = image_data.get("posters", [])

#     for backdrop in backdrops:
#         print("Backdrop URL:", backdrop["backdrop_path"])
#     for poster in posters:
#         print("Poster URL:", poster["poster_path"])

# def recommendation(movie):
#     movie_index = movies[movies['title']==movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]

#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         # fetch poster from API
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.title('Movie Recommender System')

# selected_movie_name = st.selectbox('Search the movie', movies['title'].values)

# if st.button('Recommendation'):
#     # recommendations = recommendation(selected_movie_name)
#     # for i in recommendations:
#     #     st.write(i)
#     recommended_movies, recommended_movies_posters = recommendation(selected_movie_name)

#     col1, col2, col3, col4, col5= st.columns(5)
#     with col1:
#         st.text(recommended_movies[0])
#         st.image(recommended_movies_posters[0])
#     with col2:
#         st.text(recommended_movies[1])
#         st.image(recommended_movies_posters[1])
#     with col3:
#         st.text(recommended_movies[2])
#         st.image(recommended_movies_posters[2])
#     with col4:
#         st.text(recommended_movies[3])
#         st.image(recommended_movies_posters[3])
#     with col5:
#         st.text(recommended_movies[4])
#         st.image(recommended_movies_posters[4])

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d0e15344d04efaed8617008869f8e984&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




