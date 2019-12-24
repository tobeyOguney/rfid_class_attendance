
from .. import db
from .student_course import student_course
from .lecturer_course import lecturer_course


class Course(db.Model):
    """ Course Model for storing course related details """
    __tablename__ = "course"

    faculty = db.Column(db.String(255), nullable=False)
    department = db.Column(db.String(255), nullable=False)
    course_code = db.Column(db.String(255), nullable=False)
    course_title = db.Column(db.String(255), nullable=False)
    strict = db.Column(db.Boolean, nullable=False)
    students = db.relationship("student", secondary=student_course, backref="course")
    lecturers = db.relationship("lecturer", secondary=lecturer_course, backref="course")
    attendance_sessions = db.Column('attendance_id', db.Integer, db.ForeignKey('attendance.public_id'))
    public_id = db.Column(db.String(100), unique=True, primary_key=True)

    def __repr__(self):
        return "<Course '{}'>".format(self.course_code)
