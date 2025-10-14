# main.py

from src.recommender import ContentBasedRecommender
from src.utils import display_recommendations

def main():
    """
    Main function to run the command-line movie recommender.
    """
    # Define the path to the dataset
    MOVIES_FILEPATH = r'C:\Users\91994\Documents\movie_recommender\movie_recommender\data\movies.csv'

    # --- 1. Initialize the Recommender ---
    # This will load the data and prepare the similarity model.
    # You will see the "Loading and preparing data..." message here.
    recommender = ContentBasedRecommender(movies_filepath=MOVIES_FILEPATH)

    # --- 2. Define the Movie to Get Recommendations For ---
    # You can change this to any movie title from the dataset.
    # Some examples: 'Toy Story (1995)', 'Heat (1995)', 'Jumanji (1995)'
    movie_to_recommend_for = 'GoldenEye (1995)'

    # --- 3. Get and Display Recommendations ---
    # Call the recommend method to get a DataFrame of similar movies
    recommendations = recommender.recommend(movie_to_recommend_for, n_recommendations=10)

    # Use our utility function to print the results in a clean format
    display_recommendations(recommendations, movie_to_recommend_for)


if __name__ == '__main__':
    # This ensures the main() function runs only when the script is executed directly
    main()