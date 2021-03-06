from .. import db

class LecturerCourse(db.Model):
    __tablename__ = 'lecturer_course'
    lecturer_id = db.Column(db.String, db.ForeignKey('lecturer.lecturer_id'), primary_key=True)
    course_code = db.Column(db.String, db.ForeignKey('course.public_id'), primary_key=True)
