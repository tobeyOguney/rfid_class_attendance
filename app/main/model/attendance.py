
from datetime import datetime
from .. import db
from .student_attendance import student_attendances


class Attendance(db.Model):
    """ Attendance Model for storing attendance related details """
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_id = db.Column(db.String(255), db.ForeignKey('course.public_id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    students = db.relationship('Student', secondary=student_attendances, backref='attendance')
    public_id = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<Attendance '{}'>".format(self.code)
