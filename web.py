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
# Get a full list of movies and the scores
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
# Get the results from the search
	search = request.values.get('search_terms') 
	if search == "" or search.isspace():
		heading = "No keywords entered" 
	else:		
		heading = 'You searched for the movie titled ' + search

# Search in the database. Make this a separate function if needed 	g.db = connect_db()
	cur = g.db.execute("SELECT formatted_title, ratings FROM imdb_top_10000_cleaned WHERE formatted_title LIKE ?", ('{}%'.format(search),))
	movies = [dict(title=row[0], rating=row[1]) for row in cur.fetchall()]
	g.db.close()

	return render_template('results.html', heading=heading, movies=movies)

app.run(debug=True)