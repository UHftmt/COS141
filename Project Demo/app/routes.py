from flask import Flask, render_template, request, redirect, url_for
from app.StudentManager import StudentManager


def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add_student():
        if request.method == 'POST':
            # Extract form data and add new student
            return redirect(url_for('display'))
        return render_template('add_student.html')

    @app.route('/search', methods=['GET', 'POST'])
    def search_student():
        # Handle search and display results
        return render_template('search_student.html')

    @app.route('/modify', methods=['GET', 'POST'])
    def modify_student():
        # Modify student information if found
        return render_template('modify_student.html')
    
    @app.route('/delete', methods=['GET', 'POST'])
    def delete_student():
        #
        if request.method == 'POST':
            submitted = request.form
            print(submitted)

    @app.route('/display')
    def display_students():
        # get student list from StudentManager attribute
        students = StudentManager().students
        # go to display_students.html with data => name = value
        return render_template('display_students.html', students=students)

