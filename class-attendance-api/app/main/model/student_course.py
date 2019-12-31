from .. import db

class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'),  primary_key=True)
    course_code = db.Column(db.Integer, db.ForeignKey('course.public_id'), primary_key=True)
