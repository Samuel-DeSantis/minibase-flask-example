import minibase
import flask
from flask import jsonify, render_template, request, redirect

db = minibase.Database()
app = flask.Flask(__name__)

# ===== Create a table =====
db.table('users').create(
	columns=[
		['name', 'text'],
		['age', 'integer'],
	]
)

# View JSON data for all users
@app.route('/api/users')
def users():
	data = db.table('users').read()
	return jsonify(data)

# View JSON data for one users
@app.route('/api/users/<id>')
def user(id):
	data = db.table('users').record.read(id)
	return jsonify(data)

# Index page w/ Create a user form
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		db.table('users').record.create([
			request.form['name'], 
			request.form['age']
		])

	data = db.table('users').read()
	return render_template('index.html', data=data)

# Delete a user
@app.route('/users/<id>', methods=['POST'])
def delete(id):
	db.table('users').record.delete(id=id)
	return redirect('/')

if __name__ == '__main__':
  app.run()

# ===== Seed Data =====
# db.table('users').record.create(['John', 30])
# db.table('users').record.create(['John', 31])
# db.table('users').record.create(['Jane', 25])
# db.table('users').record.create(['Bill', 40])