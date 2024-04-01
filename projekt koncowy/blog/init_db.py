from datetime import datetime
from app import app, db, BlogPost

def initialize_database():
    print("Initializing database...")
    db.create_all()
    print("Database initialized.")

def add_initial_blog_post():
    print("Adding an initial blog post...")
    initial_post = BlogPost(
        title="Hello World!",
        content="This is the first post in our Flask blog.",
        date_posted=datetime.utcnow(),
        published=True
    )
    db.session.add(initial_post)
    db.session.commit()
    print(f"Added blog post: {initial_post.title}")

def main():
    with app.app_context():
        initialize_database()
        add_initial_blog_post()

if __name__ == "__main__":
    main()
