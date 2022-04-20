import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poter(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def reconmend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    reconmended_movies = []
    reconmended_movies_poster= []
    for i in movies_list[1:15]:
        movie_id = movies.iloc[i[0]].movie_id

        reconmended_movies.append(movies.iloc[i[0]].title)
        # Lấy poster từ API
        reconmended_movies_poster.append(fetch_poter(movie_id))
    return  reconmended_movies,reconmended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(layout="wide")
#st.image('logo.png')

video_file = open('intro1.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.title('Hệ thống gợi ý Phim')
st.write(movies['title'])
option_movie_name = st.selectbox(
    'NHẬP TÊN PHIM BẠN MUỐN XEM ',
    movies['title'].values)

#if st.button('Tìm kiếm'):
#     name,poster = reconmend(option_movie_name)
#     for i in reconmendations:
#        st.write(i)

if st.button('Tìm kiếm'):
    recommended_movie_names,recommended_movie_posters = reconmend(option_movie_name)
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])

        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])

        st.text(recommended_movie_names[10])
        st.image(recommended_movie_posters[10])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

        st.text(recommended_movie_names[11])
        st.image(recommended_movie_posters[11])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

        st.text(recommended_movie_names[12])
        st.image(recommended_movie_posters[12])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

        st.text(recommended_movie_names[13])
        st.image(recommended_movie_posters[13])