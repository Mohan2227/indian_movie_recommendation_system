from flask import Flask, render_template, request
from recommender import recommend

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    movie = request.form['movie']
    results = recommend(movie)
    return render_template('index.html', movies=results, user_input=movie)

if __name__ == "__main__":
    app.run(debug=True)