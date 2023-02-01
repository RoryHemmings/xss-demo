from flask import render_template, request, redirect, url_for, flash

from app import app, db
from .models import Message, WebPage
from .utils import filter_message


@app.route('/')
def home():
    new_page = WebPage()
    db.session.add(new_page)
    db.session.commit()

    return redirect(url_for('index', page_id=new_page.id))


@app.route('/<page_id>/')
def index(page_id):
    page = db.session.query(WebPage).get(page_id)
    if page == None: 
        return page_not_found(404)

    return render_template('home.html', messages=page.messages[::-1], page_id=page_id)


@app.route('/upload-message/<page_id>/', methods=['POST'])
def upload_message(page_id):
    page = db.session.query(WebPage).get(page_id)
    if (page == None):
        return page_not_found(404)

    content = request.form.get('message')
    author = request.form.get('author')

    if not content or not author:
        return redirect(url_for('index', page_id=page_id))

    # message = Message(filter_message(content), author)
    message = Message(content, author)
    page.messages.append(message)
    print(content, author, page.messages)

    db.session.add(message)
    db.session.commit()

    flash('Message successfully uploaded')
    return redirect(url_for('index', page_id=page_id))


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """

    # disable caching
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
