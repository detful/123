from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMTA4MDFlMmM4YzJkYjU4YmNjM2Q4NzAzYjgxMTdkNSIsInN1YiI6IjY1ZjQwNDc3MjRmMmNlMDE4NTE3NDYyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rNvTbvcP3od5hq5RgG7HuWgnn0n9WYC3wmC8IReLJbM"  # Zastąp swoim tokenem

def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['results']

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()['cast'][:10]

@app.route('/')
def homepage():
    list_type = request.args.get('list_type', 'popular')
    available_lists = ['popular', 'now_playing', 'top_rated', 'upcoming']
    if list_type not in available_lists:
        list_type = 'popular'
    movies = get_movies_list(list_type)
    return render_template("homepage.html", movies=movies, current_list=list_type, available_lists=available_lists)

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    movie = get_single_movie(movie_id)
    cast = get_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, cast=cast)

if __name__ == '__main__':
    app.run(debug=True)
