from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

from config import db, bcrypt
# Models go here!


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    is_admin = db.Column(db.Boolean)

    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
    saved_items = db.relationship('Saved', back_populates='user', cascade='all, delete')
    post_comments = db.relationship('PostComment', back_populates='user', cascade='all, delete')

    serialize_rules = ( '-comments.user', '-post_comments.user')

    
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    @validates
    def validate_username(self, key, username):
        if not username:
            raise ('You must enter a username')
        return username

    def __repr__(self):
        return f'User {self.username}, ID {self.id}'
    

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    image_url = db.Column(db.String)
    date_added = db.Column(db.String)

    post_comments = db.relationship('PostComment', back_populates='post', cascade='all, delete')
    
    def __repr__(self):
        return f'<Post {self.id}>'
    
class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    venue = db.Column(db.String)
    location = db.Column(db.String)
    details = db.Column(db.String)
    image_url = db.Column(db.String)
    event_date = db.Column(db.String)
    event_link = db.Column(db.String)

    def __repr__(self):
        return f'<Event {self.id}>'
    

class Release(db.Model, SerializerMixin):
    __tablename__ = 'releases'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    artist = db.Column(db.String)
    description = db.Column(db.String)
    record_label = db.Column(db.String)
    date_released = db.Column(db.String)
    image = db.Column(db.String)

    tracks = db.relationship('Track', back_populates='release', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='release', cascade='all, delete')
    saved_items = db.relationship('Saved', back_populates='release', cascade='all, delete')

    serialize_rules = ('-tracks.release', '-comments.release', '-saved_items.release')
    
    def __repr__(self):
        return f'<Release {self.id}>'
    
class Track(db.Model, SerializerMixin):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    bpm = db.Column(db.Integer)
    audio = db.Column(db.String)
    artist_names = db.Column(db.String)

    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    release = db.relationship('Release', back_populates='tracks')

    serialize_rules = ('-release.tracks', '-release.saved_items')

    def __repr__(self):
        return f'<Track {self.id}>'
    
class Saved(db.Model, SerializerMixin):
    __tablename__ = 'saved_items'

    id = db.Column(db.Integer, primary_key=True)
    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    release = db.relationship('Release', back_populates='saved_items')
    user = db.relationship('User', back_populates='saved_items')

    serialize_rules = ('-user.saved_items', '-release.saved_items')
        # serialize_rules = ('-release.saved_items', '-user.saved_items')


    def __repr__(self):
        return f'<SavedItem {self.id}>'

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)    
    comment = db.Column(db.String)
    date_added = db.Column(db.String)

    release_id = db.Column(db.Integer, db.ForeignKey('releases.id'))
    release = db.relationship('Release', back_populates='comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='comments')

    serialize_rules = ('-release.comments', '-user.comments', '-release.saved_items', '-user.saved_items')

    def __repr__(self):
        return f'<Comment {self.id}>'
    

class PostComment(db.Model, SerializerMixin):
    __tablename__ = 'post_comments'

    id = db.Column(db.Integer, primary_key=True)    
    comment = db.Column(db.String)
    date_added = db.Column(db.String)

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post = db.relationship('Post', back_populates='post_comments')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='post_comments')

    serialize_rules = ('-post.post_comments', '-user.post_comments', '-user.comments', '-user.saved_items')

    def __repr__(self):
        return f'<Comment {self.id}>'