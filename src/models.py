from app import db

class User(db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    role = db.Relationship('Role', backref=db.backref('users', lazy='select'))

class Role(db.Model):
    __table__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False, unique=True)

class Project(db.Model):
    __table__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(250))
    photo_url = db.Column(db.String(250))
    website_url = db.Column(db.String(250))
    year = db.Column(db.Integer)
    gge_reduced = db.Column(db.Float)
    ghg_reduced = db.Column(db.Float)

    project_type_id = db.Column(db.Integer, db.ForeignKey('project_types.id'))

    type = db.Relationship('ProjectType',
                           backref=db.backref('projects', lazy='select'))

class Location(db.Model):
    __table__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    project_id = db.Column(db.Integer, db.ForeignKey('projects'))

    project = db.Relationship('Project', backref='locations', lazy='dynamic')

class ProjectType(db.Model):
    __table__ = 'project_types'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(30), nullable=False, unique=True)