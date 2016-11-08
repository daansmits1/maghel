from flask import *
import sqlite3

DATABASE = 'movies.db'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
	g.db = connect_db()
	cur = g.db.execute("select name, score from imdb_top_10000")
	movies = [dict(name=row[0], score=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('index.html',movies=movies)

app.run(debug=True)