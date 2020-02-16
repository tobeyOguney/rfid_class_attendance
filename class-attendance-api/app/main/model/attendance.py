
from .. import db
from .student_attendance import StudentAttendance


class Attendance(db.Model):
    """ Attendance Model for storing attendance related details """
    __tablename__ = "attendance"

    session = db.Column(db.String(255), nullable=False)
    semester = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    hash_key = db.Column(db.String, nullable=False)
    open = db.Column(db.Boolean, nullable=False)
    _course = db.Column(db.String, db.ForeignKey('course.public_id'))
    _lecturer = db.Column(db.String, db.ForeignKey('lecturer.public_id'))
    students = db.relationship("Student", secondary='student_attendance', backref="attendance")
    public_id = db.Column(db.String(100), unique=True, primary_key=True)

    def __repr__(self):
        return "<Attendance '{}'>".format(self.public_id)
