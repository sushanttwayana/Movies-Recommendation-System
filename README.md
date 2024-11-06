🎬 Movie Recommendation System

A content-based movie recommendation system that uses Natural Language Processing (NLP) to suggest movies based on similarity in themes, genres, and keywords. This project preprocesses movie metadata, converts text data to a structured format, and calculates similarity scores to deliver accurate recommendations.

💡 Project Overview

This project uses several NLP and machine learning techniques to recommend movies:

Bag of Words (BoW): Extracts features by tokenizing movie descriptions, cast, genres, and keywords into a vectorized format.
Similarity-based Search: Uses cosine similarity on BoW vectors to compute the closeness between movies, generating personalized recommendations.
Stemming & Stop Words Removal: Refines feature extraction by reducing words to their root forms and removing common stop words to improve relevance.

📁 Key Features

Data Preprocessing: Parses and cleans movie data, including genres, keywords, cast, and crew information.
Text Vectorization: Transforms text data into vectors using the BoW model for similarity calculations.
Recommendation Engine: Returns a ranked list of similar movies based on cosine similarity, providing top movie recommendations.


# Output
![image](https://github.com/user-attachments/assets/2124bdac-e72f-456f-a9f2-46cfca92b9f6)

!
📄 Project Demo
Check out the demo on Streamlit to see the Movie Recommendation System in action!

