from flask import *
import sqlite3

DATABASE = 'movies.db'

app = Flask(__name__)
app.config.from_object(__name__)

# footer = "© Working project by Daan 2016"

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
	g.db = connect_db()
	cur = g.db.execute("SELECT formatted_title, ratings FROM imdb_top_10000_cleaned")
	movies = [dict(title=row[0], rating=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html',movies=movies)

@app.route('/search')
def search():
	return render_template('search.html')

@app.route('/results')
def results():
	search = request.values.get('search_terms')
	heading = 'You searched for the movie titled ' + search

	return render_template('results.html', heading=heading)


app.run(debug=True)