from .. import db

course_lecturers = db.Table('course_lecturers',
    db.Column('course_id', db.Integer, db.ForeignKey('course.public_id')),
    db.Column('lecturer_id', db.Integer, db.ForeignKey('lecturer.public_id'))
)