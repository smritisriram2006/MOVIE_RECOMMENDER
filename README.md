Content-Based Movie Recommender System
This project is a simple yet effective content-based movie recommendation system. It suggests movies to a user based on the genres of a movie they already like. The project includes both an interactive web application built with Streamlit and a command-line script.

Features
Content-Based Filtering: Recommends movies using genre similarity.

TF-IDF Vectorization: Converts movie genres into a numerical format for comparison.

Cosine Similarity: Calculates the similarity score between movies.

Interactive Web UI: A user-friendly interface built with Streamlit to easily get recommendations.

Command-Line Interface: A simple script to run the recommender directly from the terminal.

Project Structure
movie_recommender/
│
├── data/
│   └── movies.csv          # MovieLens dataset
│
├── src/
│   ├── recommender.py      # Core recommendation logic class
│   └── utils.py            # Helper functions for CLI display
│
├── venv/                   # Python virtual environment
│
├── app.py                  # Streamlit web application entry point
├── main.py                 # Command-line interface entry point
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
Setup and Installation
Follow these steps to set up the project on your local machine.

Prerequisites
Python 3.8 or higher

pip and venv (usually included with Python)

1. Clone the Repository
First, get the code on your local machine. If you have Git, you can clone it:

Bash

git clone <your-repository-url>
cd movie_recommender
If not, simply navigate into your project directory:

PowerShell

cd path\to\your\movie_recommender
2. Create and Activate a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated.

On Windows (PowerShell):

PowerShell

# Create the virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1
On macOS/Linux:

Bash

# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
You will know the environment is active when you see (venv) at the beginning of your terminal prompt.

3. Install Dependencies
Install all the required Python packages using the requirements.txt file.

Bash

pip install -r requirements.txt
Usage
You can run the recommender in two ways:

1. Running the Streamlit Web Application
This is the recommended way to interact with the system. From the project's root directory, run:

Bash

streamlit run app.py
This will start a local web server and open the application in your default web browser. From there, you can select a movie from the dropdown menu and click "Recommend" to see the results.

2. Running the Command-Line Script
To run the recommender from your terminal, execute the main.py script. This is useful for quick tests.

Bash

python main.py
This will output the recommendations for the movie hardcoded in the script (by default, 'GoldenEye (1995)'). You can edit main.py to change the input movie.

Example Output:

============================================================
Since you liked 'GoldenEye (1995)', you might also like:
============================================================

                             title                       genres
          Die Hard: With a Vengeance (1995)         Action, Crime, Thriller
                Clear and Present Danger (1994)    Action, Crime, Drama, Thriller
                         True Lies (1994)     Action, Adventure, Comedy, Romance, Thriller
                         ...
How It Works
Data Loading: The movies.csv dataset is loaded into a pandas DataFrame.

Feature Extraction: The genres for each movie (e.g., "Action|Adventure|Thriller") are treated as a document. A TfidfVectorizer from scikit-learn is used to convert this text data into a numerical matrix, where each movie is represented by a vector.

Similarity Calculation: The Cosine Similarity is calculated between all movie vectors. This results in a matrix where each cell (i, j) contains a score representing how similar movie i is to movie j.

Recommendation: When a user selects a movie, the system looks up its pre-calculated similarity scores with all other movies and returns the ones with the highest scores.