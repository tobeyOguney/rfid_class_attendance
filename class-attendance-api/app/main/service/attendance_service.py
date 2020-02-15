import uuid
import datetime
import time

from app.main import db
from app.main.model.attendance import Attendance
from app.main.model.lecturer import Lecturer
from app.main.model.student import Student
from app.main.model.course import Course


def create_attendance(data):
    lecturer = Lecturer.query.filter_by(lecturer_id=data["lecturer_id"]).first()
    course = Course.query.filter_by(course_code=data['course_code']).first()
    if lecturer and course:
        new_attendance = Attendance(
            public_id=str(uuid.uuid4()),
            session = data['session'],
            semester = data['semester'],
            open = True,
            created_on = datetime.datetime.utcnow(),
            hash_key = int(round(time.time() * 1000))
        )
        save_changes(new_attendance)
        lecturer.attendance_sessions.append(new_attendance)
        course.attendance_sessions.append(new_attendance)
        save_changes(lecturer)
        save_changes(course)
        return new_attendance, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer or Course does not exist.',
        }
        return response_object, 409


def get_attendance(public_id):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        return attendance, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance does not exist.'
        }
        return response_object, 409


def get_students(public_id):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        return attendance.students, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance does not exist.'
        }
        return response_object, 409


def update_attendance(public_id, data):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        attendance.session = data['session']
        attendance.semester = data['semester']
        save_changes(attendance)
        return attendance, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance does not exist.'
        }
        return response_object, 409

def close_attendance(public_id):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        attendance.open = False
        save_changes(attendance)
        response_object = {
            'status': 'success',
            'message': 'Successfully closed.'
        }
        return response_object, 201
    else:
        response_object = {
                'status': 'fail',
                'message': 'Attendance does not exist.',
        }
        return response_object, 409


def check_attendance(hash_key):
    attendance = Attendance.query.filter_by(hash_key=hash_key).first()
    if attendance and attendance.open:
        response_object = {
            'status': 'success',
            'message': 'Writable Attendance.'
        }
        return response_object, 201
    else:
        response_object = {
                'status': 'fail',
                'message': 'Attendance is closed or does not exist.',
        }
        return response_object, 409


def commit_attendance(hash_key, data):
    attendance = Attendance.query.filter_by(hash_key=hash_key).first()
    if attendance and attendance.open:
        student = Student.query.filter_by(student_id=data['student_id']).first()
        if student:
            attendance.students.append(student)
            save_changes(attendance)
            response_object = {
                'status': 'success',
                'message': 'Successfully commited.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Student does not exist.',
            }
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance is closed or does not exist.',
        }
        return response_object, 409


def remove_attendance(public_id):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        db.session.delete(attendance)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance does not exist.',
        }
        return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()

