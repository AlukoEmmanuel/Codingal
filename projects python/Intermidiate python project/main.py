from flask import Flask, render_template, request, jsonify
from recommendation_engine import RecommendationEngine
import requests

app = Flask(__name__)

# Initialize the recommendation engine
engine = RecommendationEngine(movies_file="movies.csv", ratings_file="ratings.csv")

# Replace with your actual TMDB API key
TMDB_API_KEY = "your_tmdb_api_key"
TMDB_BASE_URL = "https://api.themoviedb.org/3"

# Helper function to fetch movie details from TMDB API
def fetch_movie_details(movie_title):
    try:
        search_url = f"{TMDB_BASE_URL}/search/movie"
        params = {"api_key": TMDB_API_KEY, "query": movie_title}
        response = requests.get(search_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data["results"][0] if data["results"] else None
    except requests.RequestException as e:
        print(f"Error fetching movie details: {e}")
        return {"error": "Unable to fetch movie details"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        movie_title = request.form.get("movie_title")
        if not movie_title:
            return jsonify({"error": "Movie title is required"}), 400
        
        recommendations = engine.recommend_content_based(movie_title)
        return jsonify(recommendations)
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return jsonify({"error": "An error occurred while processing your request"}), 500

@app.route("/popular")
def popular():
    try:
        recommendations = engine.recommend_popular()
        return jsonify(recommendations)
    except Exception as e:
        print(f"Error fetching popular recommendations: {e}")
        return jsonify({"error": "An error occurred while fetching popular movies"}), 500

@app.route("/movie-details", methods=["POST"])
def movie_details():
    try:
        movie_title = request.form.get("movie_title")
        if not movie_title:
            return jsonify({"error": "Movie title is required"}), 400
        
        details = fetch_movie_details(movie_title)
        if "error" in details:
            return jsonify(details), 500
        
        return jsonify(details)
    except Exception as e:
        print(f"Error fetching movie details: {e}")
        return jsonify({"error": "An error occurred while fetching movie details"}), 500

if __name__ == "__main__":
    app.run(debug=True)
