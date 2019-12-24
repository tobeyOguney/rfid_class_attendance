from .. import db

lecturer_course = db.Table('lecturer_course',
    db.Column('lecturer_id', db.Integer, db.ForeignKey('lecturer.public_id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.public_id'))
)