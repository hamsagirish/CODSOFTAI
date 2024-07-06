import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: user ratings for movies
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5],
    'movie_id': [1, 2, 3, 1, 2, 4, 2, 3, 1, 3, 2, 4],
    'rating': [5, 4, 3, 4, 5, 4, 3, 5, 2, 4, 5, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create user-item matrix
user_movie_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def get_recommendations(user_id, user_movie_matrix, user_similarity_df, k=5):
    # Get the user's ratings
    user_ratings = user_movie_matrix.loc[user_id]
    
    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:k+1]
    
    # Get the movies rated by similar users
    similar_users_ratings = user_movie_matrix.loc[similar_users]
    
    # Calculate the weighted average of the ratings
    weighted_ratings = similar_users_ratings.apply(lambda row: np.dot(row, user_similarity_df.loc[user_id, similar_users]) / user_similarity_df.loc[user_id, similar_users].sum(), axis=0)
    
    # Exclude movies already rated by the user
    recommendations = weighted_ratings[user_ratings == 0].sort_values(ascending=False).head(k)
    
    return recommendations.index.tolist()

# Recommend movies for a user
user_id = 4
recommended_movies = get_recommendations(user_id, user_movie_matrix, user_similarity_df, k=3)

print(f"Recommended movies for user {user_id}: {recommended_movies}")
