
from .. import db
from .student_attendance import student_attendance


class Attendance(db.Model):
    """ Attendance Model for storing attendance related details """
    __tablename__ = "attendance"

    session = db.Column(db.String(255), nullable=False)
    semester = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    hash_key = db.Column(db.Integer)
    course = db.relationship('course', backref='attendance')
    lecturer = db.relationship('lecturer', backref='attendance')
    students = db.relationship("student", secondary=student_attendance, backref="attendance")
    public_id = db.Column(db.String(100), unique=True, primary_key=True)

    def __repr__(self):
        return "<Attendance '{}'>".format(self.public_id)
