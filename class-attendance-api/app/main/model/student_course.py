from .. import db

student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('student.public_id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.public_id'))
)