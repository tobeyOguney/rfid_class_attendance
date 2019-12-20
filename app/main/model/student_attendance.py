from .. import db

student_attendances = db.Table('student_attendances',
    db.Column('student_id', db.Integer, db.ForeignKey('student.public_id')),
    db.Column('attendance_id', db.Integer, db.ForeignKey('attendance.public_id'))
)