from app import db


# by convention, all foreign key Columns must end in '_id'
# this will ensure that the parser object in resource.py will work correctly

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    role = db.relationship('Role', backref=db.backref('users', lazy='select'))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False, unique=True)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(250))
    photo_url = db.Column(db.String(250))
    website_url = db.Column(db.String(250))
    year = db.Column(db.Integer)
    gge_reduced = db.Column(db.Float)
    ghg_reduced = db.Column(db.Float)

    project_type_id = db.Column(db.Integer, db.ForeignKey('project_types.id'))

    type = db.relationship('ProjectType',
                           backref=db.backref('projects', lazy='select'))


class ProjectType(db.Model):
    __tablename__ = 'project_types'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(30), nullable=False, unique=True)


class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    project = db.relationship('Project', backref='locations') #, lazy='dynamic')
