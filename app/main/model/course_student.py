from .. import db

course_students = db.Table('course_students',
    db.Column('course_id', db.Integer, db.ForeignKey('course.public_id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.public_id'))
)