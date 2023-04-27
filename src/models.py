from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(120),unique=False, nullable=False)
    lastname = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    favourites = db.relationship("Favourites", back_populates="user", lazy=True)
    posts = db.relationship("Post", back_populates="owner", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "favourites": [favorite.__repr__() for favorite in self.favourites] 
        }

class Favourites(db.Model):
    __tablename__ = 'favourite'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False) 

    user = db.relationship('User', back_populates='favourites', lazy=True)
    post = db.relationship('Post', back_populates='favourited', lazy=True)

    def __repr__(self):
        return '<FavPost %r>' % self.post_id   

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    owner_id = db.Column(db.Integer(), db.ForeignKey("user.id"), nullable=False)
    planet_media_id = db.Column(db.Integer(), db.ForeignKey("planet.id"))
    character_media_id = db.Column(db.Integer(), db.ForeignKey("character.id"))
    vehicule_media_id = db.Column(db.Integer(), db.ForeignKey("vehicule.id"))

    # Relaciones Many-to-One con las clases 'Planet', 'Character' y 'Vehicule'
    planet = db.relationship('Planet', back_populates='post', lazy=True) #
    character = db.relationship('Character', back_populates='post', lazy=True)
    vehicule = db.relationship('Vehicule', back_populates='post', lazy=True)
    owner = db.relationship('User', back_populates='posts', lazy=True)
    favourited = db.relationship('Favourites', back_populates='post', lazy=True)

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    terrain = db.Column(db.String(250), nullable=True)
    gravity = db.Column(db.String(250), nullable=True)
    radius = db.Column(db.String(250), nullable=True)
    #
    post = db.relationship("Post", back_populates="planet", lazy=True)
    #
    born_here = db.relationship("Character", back_populates="planet", lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "gravity": self.gravity,
            "radius": self.radius,
            
            #"born_here" : [favorite.__repr__() for favorite in self.favourites],
            #"post" : [favorite.__repr__() for favorite in self.favourites] 
        } 

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    lastname = db.Column(db.String(250), nullable=True)
    birthdate = db.Column(db.String(250), nullable=True)
    gender = db.Column(db.String(250), nullable=True)
    eye_color = db.Column(db.String(250), nullable=True)
    #
    post = db.relationship("Post", back_populates="character")
    #
    origin_planet = db.Column(db.Integer(), db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="born_here", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "eye_color": self.eye_color,

            #"planet" : [favorite.__repr__() for favorite in self.favourites],
            #"post" : [favorite.__repr__() for favorite in self.favourites] 
        } 


class Vehicule(db.Model):
    __tablename__ = 'vehicule'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    capacity = db.Column(db.String(250), nullable=True)
    speed = db.Column(db.String(250), nullable=True)
    #
    post = db.relationship("Post", back_populates="vehicule", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            "speed": self.speed,

            #"planet" : [favorite.__repr__() for favorite in self.favourites],
            #"post" : [favorite.__repr__() for favorite in self.favourites] 
        }