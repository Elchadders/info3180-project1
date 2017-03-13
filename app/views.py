"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""



import time
from models import Person, PersonGroup
from flask_appbuilder.views import ModelView, BaseView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.widgets import ListThumbnail

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import UserForm
from models import User
# import sqlite3

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            firstname = user_form.firstname.data # You could also have used request.form['name']
            lastname = user_form.lastname.data
            age = user_form.age.data
            gender = user_form.gender.data
            biography = user_form.biography.data
            image = filename(user_form.image.file.filename)
            

            # save user to database
            user = User(firstname, lastname, age, gender, biography,image)
            db.session.add(user)
            db.session.commit()

            flash('User successfully added')
            return redirect(url_for('profiles'))

    flash_errors(user_form)
    return render_template('profile.html', form=user_form)



@app.route('/profiles')
def show_users():
    users = db.session.query(User).all()
    
    
@app.route('/profile/<userid>', methods= ['GET','POST'])
def personalprofileform ():
    form = PersonalProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return render_template('personalprofile.html', form=form)
        else:
            flash('Please complete all the fields required.')
            return render_template('personalprofile.html', form=form)
    elif request.method == 'GET':
        """Render website's profile page."""
        return render_template('personalprofile.html', form=form)
    
def dateinfo():
	result = time.strftime("%a, %d %b %Y")

	return result

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/uploads/<path:path>')
def send_uploads(path):
return send_from_directory(app.config['UPLOAD_FOLDER'], path)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
