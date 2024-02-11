import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):

    # fetching the movies with specific IDs
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=783bd025afbc6a39efa3b96fab96995d&language=en-US'.format(movie_id)) 
    data = response.json()     # converting into json
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']    ## this will return the poster 
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]  
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    # append the top 5 movies 
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id      # this will fetch the id of the movies from the dataset
        # fetching poster from api
        recommended_movies.append(movies.iloc[i[0]].title)  # this will return the name of the top 5 movies
        recommended_movies_posters.append(fetch_poster(movie_id)) # this will return the posters
       
      
    return recommended_movies,recommended_movies_posters
        
        

movies_dict1=pickle.load(open('movie_dict1.pkl','rb'))
movies=pd.DataFrame(movies_dict1)

similarity=pickle.load(open('similarity.pkl','rb'))
# Show the title
st.title('Movie Recommendation System')
#show the drop dwn list of movies
selected_movie_name =st.selectbox(
    'How would you like to be contacted ',
    movies['title'].values)

if st.button('Recommend'):   # create a button named recommendation 
    names,posters=recommend(selected_movie_name)    # fetch the selected movies names 
    # for i in recommendations:
    #     st.write(i)# print all 5 movies
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
