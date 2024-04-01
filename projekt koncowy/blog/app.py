from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'root'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=True, nullable=False)

class User(UserMixin):
    id = 1

users = {'root': generate_password_hash('root')}

@login_manager.user_loader
def load_user(user_id):
    if int(user_id) == User.id:
        return User()
    return None

@app.route('/')
def index():
    posts = BlogPost.query.filter_by(published=True).order_by(BlogPost.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users.get(username), password):
            user = User()
            login_user(user)
            return redirect(url_for('index'))
        else:
            return '<p>Invalid username or password</p>'
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        published = 'publish' in request.form
        new_post = BlogPost(title=title, content=content, published=published)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    default_post = BlogPost(published=True)
    return render_template('create_post.html', post=default_post)


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.published = 'publish' in request.form
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/unpublished')
@login_required
def unpublished_posts():
    posts = BlogPost.query.filter_by(published=False).order_by(BlogPost.date_posted.desc()).all()
    return render_template('unpublished.html', posts=posts)

@app.route('/publish/<int:post_id>', methods=['POST'])
@login_required
def publish_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    post.published = True
    db.session.commit()
    return redirect(url_for('unpublished_posts'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
