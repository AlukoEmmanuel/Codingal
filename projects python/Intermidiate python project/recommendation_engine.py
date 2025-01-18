import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class RecommendationEngine:
    def __init__(self, movies_file, ratings_file):
        self.movies = pd.read_csv(movies_file)
        self.ratings = pd.read_csv(ratings_file)
        self.popular_movies = None
        self.cosine_sim = None
        self.prepare_content_based()
        self.prepare_popularity_based()

    def prepare_content_based(self):
        self.movies["combined_features"] = self.movies["genres"].fillna("") + " " + \
                                           self.movies["keywords"].fillna("") + " " + \
                                           self.movies["cast"].fillna("") + " " + \
                                           self.movies["director"].fillna("")
        cv = CountVectorizer(stop_words="english")
        feature_matrix = cv.fit_transform(self.movies["combined_features"])
        self.cosine_sim = cosine_similarity(feature_matrix)

    def prepare_popularity_based(self):
        movie_ratings = self.ratings.groupby("movieId").mean()["rating"]
        self.movies["average_rating"] = self.movies["movieId"].map(movie_ratings)
        self.popular_movies = self.movies.sort_values(by="average_rating", ascending=False)

    def recommend_content_based(self, title):
        if title not in self.movies["title"].values:
            return ["Movie not found."]
        movie_idx = self.movies[self.movies["title"] == title].index[0]
        similar_movies = list(enumerate(self.cosine_sim[movie_idx]))
        sorted_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:6]
        return [self.movies.iloc[i[0]].title for i in sorted_movies]

    def recommend_popular(self):
        return self.popular_movies.head(5)["title"].tolist()
2