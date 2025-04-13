from flask import Flask, render_template, request, session, flash, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# --- Setup ---
app = Flask(__name__)
app.secret_key = 'super-secret-key' # Need to change this later

@app.context_processor
def inject_unread_notifications():
    if 'username' in session:
        user = db.query(User).filter_by(username=session['username']).first()
        unread = db.query(Notification).filter_by(user_id=user.id, is_read=0).count()
        return dict(unread_notifications=unread)
    return dict(unread_notifications=0)


Base = declarative_base()

def book_is_checked_out(book_id):
    return db.query(Checkout).filter_by(book_id=book_id).first() is not None

app.jinja_env.globals.update(book_is_checked_out=book_is_checked_out)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_key = Column(String)
    isbn = Column(String)
    publish_date = Column(String)
    subject = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    author_key = Column(String, unique=True)
    name = Column(String)

class Checkout(Base):
    __tablename__ = 'checkouts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    checkout_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="checkouts")
    book = relationship("Book")

class Wishlist(Base):
    __tablename__ = 'wishlist'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))

    user = relationship("User", backref="wishlist_items")
    book = relationship("Book")

class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String)
    is_read = Column(Integer, default=0)  # 0 = unread, 1 = read

    user = relationship("User", backref="notifications")


# --- Database connection ---
engine = create_engine('sqlite:///books.db')
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

Base.metadata.create_all(engine)

# --- Search Route ---
@app.route('/search')
def search_books():
    query = request.args.get('q', '')
    results = []
    author_map = {}
    if query:
        results = db.query(Book).filter(Book.title.ilike(f"%{query}%")).limit(50).all()
        keys = list(set(book.author_key for book in results if book.author_key))
        authors = db.query(Author).filter(Author.author_key.in_(keys)).all()
        author_map = {author.author_key: author.name for author in authors}

    return render_template('search.html', books=results, authors=author_map, query=query)

# --- Login Route ---
@app.route('/index', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.query(User).filter_by(username=username).first()

        if user and user.password == password:
            session['username'] = username
            return redirect(url_for('landing'))

        flash("Invalid username or password.")
        return render_template('index.html')

    return render_template('index.html')

# --- Register Route ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = db.query(User).filter_by(username=username).first()
        if existing_user:
            flash("Username already taken. Please choose another.")
            return render_template('register.html')

        new_user = User(username=username, password=password)
        db.add(new_user)
        db.commit()

        flash("Registration successful! You can now log in.")
        return redirect(url_for('login'))

    return render_template('register.html')

# --- Landing Route ---
@app.route('/landing')
def landing():
    if 'username' not in session:
        flash("You must be logged in to view your landing page.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()

    checkouts = (
        db.query(Checkout)
        .filter_by(user_id=user.id)
        .order_by(Checkout.checkout_date.desc())
        .all()
    )
    wishlist = (
        db.query(Wishlist)
        .filter_by(user_id=user.id)
        .all()
    )

    return render_template('landing.html', checkouts=checkouts, wishlist=wishlist)


# --- Checkout Route ---
@app.route('/checkout', methods=['POST'])
def checkout():
    if 'username' not in session:
        flash("You must be logged in to check out books.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()
    book_id = request.form.get('book_id')

    existing_checkout = db.query(Checkout).filter_by(book_id=book_id).first()
    if existing_checkout:
        flash("This book is already checked out.")
        return redirect(url_for('search_books'))

    user_checkouts = db.query(Checkout).filter_by(user_id=user.id).count()
    if user_checkouts >= 3:
        flash("You can only check out 3 books at a time.")
        return redirect(url_for('search_books'))

    new_checkout = Checkout(user_id=user.id, book_id=book_id, checkout_date=datetime.utcnow())
    db.add(new_checkout)
    db.commit()

    flash("Book checked out successfully!")
    return redirect(url_for('landing'))


# --- Checkout from Wishlist Route ---
@app.route('/checkout_from_wishlist', methods=['POST'])
def checkout_from_wishlist():
    if 'username' not in session:
        flash("You must be logged in to check out books.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()
    book_id = request.form.get('book_id')

    if book_is_checked_out(book_id):
        flash("That book is already checked out.")
        return redirect(url_for('landing'))

    user_checkouts = db.query(Checkout).filter_by(user_id=user.id).count()
    if user_checkouts >= 3:
        flash("You can only check out 3 books at a time.")
        return redirect(url_for('landing'))

    new_checkout = Checkout(user_id=user.id, book_id=book_id, checkout_date=datetime.utcnow())
    db.add(new_checkout)

    wish = db.query(Wishlist).filter_by(user_id=user.id, book_id=book_id).first()
    if wish:
        db.delete(wish)

    db.commit()
    flash("Book checked out successfully from your wishlist!")
    return redirect(url_for('landing'))



# --- Logout Route ---
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))


# --- Return Route ---
@app.route('/return', methods=['GET', 'POST'])
def return_books():
    if 'username' not in session:
        flash("Please log in to return books.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()
    returned = False

    if request.method == 'POST':
        return_ids = request.form.getlist('return_ids')
        for checkout_id in return_ids:
            checkout = db.query(Checkout).filter_by(id=checkout_id, user_id=user.id).first()
            if checkout:

                wishers = db.query(Wishlist).filter_by(book_id=checkout.book_id).all()
                for wisher in wishers:
                    if wisher.user_id != user.id:
                        note = Notification(
                            user_id=wisher.user_id,
                            message=f"'{checkout.book.title}' is now available!",
                            is_read=0
                        )
                        db.add(note)


                db.delete(checkout)

        db.commit()
        returned = True


    checkouts = db.query(Checkout).filter_by(user_id=user.id).all()
    return render_template('return.html', checkouts=checkouts, returned=returned)


# --- Wishlist Route ---
@app.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    if 'username' not in session:
        flash("You must be logged in.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()
    book_id = request.form.get('book_id')

    exists = db.query(Wishlist).filter_by(user_id=user.id, book_id=book_id).first()
    if exists:
        flash("Book is already in your wishlist.")
        return redirect(url_for('search_books'))

    wish = Wishlist(user_id=user.id, book_id=book_id)
    db.add(wish)
    db.commit()
    flash("Book added to wishlist!")
    return redirect(url_for('search_books'))

# --- Notifications Route ---
@app.route('/notifications')
def view_notifications():
    if 'username' not in session:
        flash("Please log in to view notifications.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()

    for note in user.notifications:
        note.is_read = 1
    db.commit()

    return render_template('notifications.html', notifications=user.notifications)


# --- Clear Notifications Route ---
@app.route('/clear_notifications', methods=['POST'])
def clear_notifications():
    if 'username' not in session:
        flash("Please log in to clear notifications.")
        return redirect(url_for('login'))

    user = db.query(User).filter_by(username=session['username']).first()
    db.query(Notification).filter_by(user_id=user.id).delete()
    db.commit()

    flash("All notifications cleared.")
    return redirect(url_for('view_notifications'))



if __name__ == '__main__':
    app.run(debug=True)