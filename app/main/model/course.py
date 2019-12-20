
from .. import db
from .course_student import course_students
from .course_lecturer import course_lecturers


class Course(db.Model):
    """ Course Model for storing course related details """
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(255), unique=True, nullable=False)
    title = db.Column(db.String(255), unique=True, nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    attendances = db.relationship('Attendance', backref='course')
    students = db.relationship('Student', secondary=course_students, lazy='subquery',
        backref=db.backref('course', lazy=True))
    lecturers = db.relationship('Lecturer', secondary=course_lecturers, lazy='subquery',
        backref=db.backref('course', lazy=True))

    def __repr__(self):
        return "<Course '{}'>".format(self.code)
