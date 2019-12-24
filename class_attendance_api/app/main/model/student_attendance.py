from .. import db

student_attendance = db.Table('student_attendance',
    db.Column('student_id', db.Integer, db.ForeignKey('student.public_id')),
    db.Column('attendance_id', db.Integer, db.ForeignKey('attendance.public_id'))
)