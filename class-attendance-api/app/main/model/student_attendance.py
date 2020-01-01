from .. import db

class StudentAttendance(db.Model):
    __tablename__ = 'student_attendance'
    student_id = db.Column(db.String, db.ForeignKey('student.student_id'),  primary_key=True)
    attendance_id = db.Column(db.String, db.ForeignKey('attendance.public_id'), primary_key=True)
