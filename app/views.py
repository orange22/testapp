__author__ = 'orange'
from app import app
from app.models import *
from app.forms import *
from sqlalchemy import desc
from database import db_session
from flask import render_template, session, request, redirect, url_for


@app.route("/")
def index():
    books=Book.query.order_by(desc('id')).limit(5).all()
    authors=Author.query.order_by(desc('id')).limit(5).all()
    return render_template('index.html',books=books,authors=authors)

@app.route("/authors")
def authors():
    authors=Author.query.order_by(desc('id')).all()
    return render_template('authors.html',authors=authors)

@app.route("/books")
def books():
    books=Book.query.order_by(desc('id')).all()
    return render_template('books.html',books=books)


@app.route('/author/<int:author_id>')
def show_author(author_id):
    author=Author.query.filter_by(id=author_id).first()
    return render_template('author.html',author=author)

@app.route('/<instance>/delete/<int:obj_id>')
def delete(instance=None,obj_id=None):
    if session['username']:
        if instance == 'author':
            obj = Author.query.filter_by(id=obj_id).first()
        if instance == 'book':
            obj = Book.query.filter_by(id=obj_id).first()
        db_session.delete(obj)
        db_session.commit()
        return redirect('/'+instance+'s')
    else:
        return redirect('/')


@app.route('/author/create')
@app.route('/author/edit', methods=['GET', 'POST'])
@app.route('/author/edit/<int:author_id>')
def edit_author(author_id=None):
    model=Author.query.filter_by(id=author_id).first()
    form = AuthorForm(request.form, model)
    #pprint (vars(form))

    if request.method == 'POST' and form.validate():
        author = Author(form.name.data)
        if form.id.data:
            db_session.query(Author).filter_by(id=form.id.data).update({"name": form.name.data})
        else:
            db_session.add(author)
        db_session.commit()
        return redirect('/')


    return render_template('authoredit.html',author=model,form=form)

@app.route('/book/<int:book_id>')
def show_book(book_id):
    book=Book.query.filter_by(id=book_id).first()
    return render_template('book.html',book=book)

@app.route('/book/create')
@app.route('/book/edit', methods=['GET', 'POST'])
@app.route('/book/edit/<int:book_id>')
def edit_book(book_id=None):
    model=Book.query.filter_by(id=book_id).first()
    form = BookForm(request.form, model)
    #pprint (vars(form))

    if request.method == 'POST' and form.validate():

        book = Book(form.name.data)
        if form.id.data:
            db_session.query(Book).filter_by(id=form.id.data).update({"name": form.name.data})
        else:
            db_session.add(book)
        db_session.commit()
        return redirect('/')


    return render_template('bookedit.html',book=model,form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username']=='admin' and request.form['password']=='admin':
        session['username'] = request.form['username']
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/test')
def test():
    # remove the username from the session if it's there
    #books=Book.query.order_by(desc('id')).limit(5).all()
    books = Book.query.whoosh_search('%book%')
    return render_template('search.html',books=books)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
