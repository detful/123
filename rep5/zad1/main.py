from flask import Flask, render_template

app = Flask(__name__)

# apikey = "e10801e2c8c2db58bcc3d8703b8117d5"
# apireadaccesstoken = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMTA4MDFlMmM4YzJkYjU4YmNjM2Q4NzAzYjgxMTdkNSIsInN1YiI6IjY1ZjQwNDc3MjRmMmNlMDE4NTE3NDYyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.rNvTbvcP3od5hq5RgG7HuWgnn0n9WYC3wmC8IReLJbM"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/homepage')
def homepage():
    movies = [
        {"title": 'Przykładowy film 1', "img_url": "http://placehold.it/300x500", "more_info_url": "#"},
        {"title": "Przykładowy film 2", "img_url": "http://placehold.it/300x500", "more_info_url": "#"},
        # Można dodać więcej filmów tutaj
    ]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)

