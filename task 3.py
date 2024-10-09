TASK 3:

# Sample data
users = {
    1: {'The Matrix': 5, 'Toy Story': 3, 'The Godfather': 4},
    2: {'The Matrix': 4, 'Avatar': 5},
    3: {'Toy Story': 5, 'Avatar': 4, 'Shrek': 2},
    4: {'The Matrix': 3, 'The Godfather': 5, 'Shrek': 4},
    5: {'Toy Story': 4, 'Avatar': 4, 'The Godfather': 5}
}

movies = {
    'The Matrix': ['Action', 'Sci-Fi'],
    'Toy Story': ['Animation', 'Children'],
    'Avatar': ['Action', 'Sci-Fi'],
    'The Godfather': ['Crime', 'Drama'],
    'Shrek': ['Animation', 'Comedy']
}

# Helper function to calculate similarity between users based on ratings
def calculate_similarity(user1_ratings, user2_ratings):
    common_movies = set(user1_ratings.keys()).intersection(set(user2_ratings.keys()))
    if not common_movies:
        return 0  # No similarity if no common movies
    
    similarity = 0
    for movie in common_movies:
        similarity += user1_ratings[movie] * user2_ratings[movie]  # dot product
    return similarity

# Collaborative Filtering: Recommend movies based on similar users
def collaborative_filtering(user_id):
    target_user_ratings = users[user_id]
    similarities = {}
    
    # Calculate similarity with other users
    for other_user_id, other_user_ratings in users.items():
        if other_user_id != user_id:
            sim = calculate_similarity(target_user_ratings, other_user_ratings)
            similarities[other_user_id] = sim
    
    # Sort users by similarity score
    similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    
    # Recommend movies that the similar users liked but the target user hasn't rated
    recommendations = []
    for similar_user_id, sim_score in similar_users:
        if sim_score > 0:  # Only consider users with positive similarity
            for movie, rating in users[similar_user_id].items():
                if movie not in target_user_ratings and rating >= 4:  # High rating by the similar user
                    recommendations.append(movie)
    
    # Remove duplicates and return recommendations
    return list(set(recommendations))

# Helper function to calculate similarity between movies based on genres
def calculate_genre_similarity(movie1_genres, movie2_genres):
    common_genres = set(movie1_genres).intersection(set(movie2_genres))
    return len(common_genres) / max(len(movie1_genres), len(movie2_genres))

# Content-Based Filtering: Recommend movies based on genres
def content_based_filtering(user_id):
    target_user_ratings = users[user_id]
    
    # Find movies that the user liked (rating 4 or higher)
    liked_movies = [movie for movie, rating in target_user_ratings.items() if rating >= 4]
    
    # Calculate similarity between liked movies and all other movies
    movie_scores = {}
    for liked_movie in liked_movies:
        for movie, genres in movies.items():
            if movie != liked_movie and movie not in target_user_ratings:
                similarity = calculate_genre_similarity(movies[liked_movie], genres)
                if movie not in movie_scores:
                    movie_scores[movie] = similarity
                else:
                    movie_scores[movie] += similarity
    
    # Sort movies by similarity score and recommend
    recommendations = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in recommendations]

# Test the recommendation system
user_id = 1
print("Collaborative Filtering Recommendations for User", user_id)
print(collaborative_filtering(user_id))

print("\nContent-Based Filtering Recommendations for User", user_id)
print(content_based_filtering(user_id))

OUTPUT :

Collaborative Filtering Recommendations for User 1
['Shrek', 'Avatar']

Content-Based Filtering Recommendations for User 1
['Avatar', 'Shrek']

=== Code Execution Successful ===
