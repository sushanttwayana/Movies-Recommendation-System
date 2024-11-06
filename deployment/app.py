import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
    
    
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        
        movie_id = movies.iloc[i[0]].movie_id
        
        # fetch poster from the API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movies_poster
    
st.title("Movie Recommendor System")
selected_movie_list = st.selectbox(
    "Type the movie name or select from the dropdown",
    movies['title'].values
)

similarity = pickle.load(open('similarity.pkl','rb'))

# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie_list)
#     columns = st.columns(5)  # Create 5 columns

#     # Loop through each recommendation and display it in a column
#     for i in range(5):
#         with columns[i]:
#             st.text(recommended_movie_names[i])
#             st.image(recommended_movie_posters[i])


# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie_list)

#     # Display two rows with two movie recommendations per row
#     for row in range(0, 5, 2):
#         cols = st.columns([1, 0.5, 1])  # Add padding between columns

#         # Display the first movie in the row
#         with cols[0]:
#             st.text(recommended_movie_names[row])
#             st.image(recommended_movie_posters[row])

#         # Check if there’s a second movie in the row
#         if row + 1 < len(recommended_movie_names):
#             with cols[2]:
#                 st.text(recommended_movie_names[row + 1])
#                 st.image(recommended_movie_posters[row + 1])


if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_list)

    # Define custom CSS for styling text
    st.markdown(
        """
        <style>
        .movie-title {
            font-size: 20px;  /* Adjust font size as needed */
            font-family: Arial, sans-serif;  /* Change to preferred font */
            color: #333333;  /* Adjust color if needed */
            text-align: center;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display two rows with two movie recommendations per row
    for row in range(0, 5, 2):
        cols = st.columns([1, 0.5, 1])  # Add padding between columns

        # Display the first movie in the row
        with cols[0]:
            st.markdown(f"<p class='movie-title'>{recommended_movie_names[row]}</p>", unsafe_allow_html=True)
            st.image(recommended_movie_posters[row])

        # Check if there’s a second movie in the row
        if row + 1 < len(recommended_movie_names):
            with cols[2]:
                st.markdown(f"<p class='movie-title'>{recommended_movie_names[row + 1]}</p>", unsafe_allow_html=True)
                st.image(recommended_movie_posters[row + 1])
