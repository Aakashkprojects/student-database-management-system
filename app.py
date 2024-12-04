from flask import Flask, render_template, request, jsonify, redirect, url_for
from database import Database
from sample_data import insert_sample_data

app = Flask(__name__)
db = Database()

# Insert sample data if database is empty
if not db.get_all_students():
    insert_sample_data(db)

@app.route('/')
def index():
    students = db.get_all_students()
    return render_template('index.html', students=students)

@app.route('/search')
def search():
    query = request.args.get('query', '')
    students = db.search_students(query)
    return render_template('index.html', students=students, search_query=query)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_data = {
            'student_id': request.form['student_id'],
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'mobile': request.form['mobile'],
            'address': request.form['address'],
            'major': request.form['major'],
            'course': request.form['course'],
            'branch': request.form['branch'],
            'gpa': float(request.form['gpa']),
            'attendance': float(request.form['attendance'])
        }
        if db.add_student(student_data):
            return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if request.method == 'POST':
        student_data = {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'mobile': request.form['mobile'],
            'address': request.form['address'],
            'major': request.form['major'],
            'course': request.form['course'],
            'branch': request.form['branch'],
            'gpa': float(request.form['gpa']),
            'attendance': float(request.form['attendance'])
        }
        if db.update_student(student_id, student_data):
            return redirect(url_for('index'))
    student = db.get_student(student_id)
    return render_template('edit.html', student=student)

@app.route('/delete/<student_id>')
def delete_student(student_id):
    db.delete_student(student_id)
    return redirect(url_for('index'))

@app.route('/view/<student_id>')
def view_student(student_id):
    student = db.get_student(student_id)
    return render_template('view.html', student=student)

if __name__ == '__main__':
    app.run(debug=True, port=3000)