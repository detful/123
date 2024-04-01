from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domowabiblioteka.db'
app.config['SECRET_KEY'] = 'bardzosekretnyklucz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year_of_publication = db.Column(db.Integer, nullable=True)
    is_borrowed = db.Column(db.Boolean, default=False)

class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    year_of_publication = IntegerField('Rok wydania', validators=[DataRequired()])
    is_borrowed = BooleanField('Czy wypożyczona')  # Dodane pole is_borrowed
    submit = SubmitField('Dodaj')

if __name__ == '__main__':
    db.create_all()
