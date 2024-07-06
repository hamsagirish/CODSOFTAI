Recommendation System

Overview:
Prepare Data: Create a user-item matrix with ratings.
Calculate Similarities: Compute similarities between users or items.
Generate Recommendations: Use similarities to recommend items.

Collaborative filtering method-This method recommends items by finding similar users and suggesting items they liked.

Install using pip install pandas numpy.
Create a sample dataset of user ratings for movies.
Compute the similarity between users using cosine similarity.
Recommend movies based on similar users' preferences.

Explanation:

Prepare Data:
DataFrame: We create a DataFrame with sample user ratings for movies.
User-Item Matrix: Pivot the DataFrame to create a user-item matrix where rows represent users and columns represent movies, with ratings as values.

Cosine Similarity: Compute the cosine similarity between users based on their ratings. This gives a similarity score between 0 and 1, indicating how similar two users are.

Generate Recommendations:
Similar Users: Find the top similar users to the target user.
Weighted Ratings: Compute the weighted average ratings for movies based on similar users' ratings.
Recommendations: Exclude movies the user has already rated and recommend the top-rated movies from the similar users' preferences.

Execution in terminal:
python recommendsystem.py
