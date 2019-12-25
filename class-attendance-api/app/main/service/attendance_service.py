import uuid
import datetime
import time

from app.main import db
from app.main.model.attendance import Attendance
from app.main.model.student import Student


def create_attendance(data):
    attendance = Attendance.query.filter_by(attendance_id=data['attendance_id']).first()
    if not attendance:
        new_attendance = Attendance(
            public_id=str(uuid.uuid4()),
            session = data['session'],
            semester = data['semester'],
            course = data['course'],
            created_on = datetime.datetime.utcnow(),
            hash_key = int(round(time.time() * 1000))
        )
        save_changes(new_attendance)
        return generate_token(new_attendance)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance already exists.',
        }
        return response_object, 409


def get_attendance(public_id):
    return Attendance.query.filter_by(public_id=public_id).first()


def update_attendance(public_id, data):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        new_attendance = Attendance(
            session = data['session'],
            semester = data['semester'],
            course = data['course']
        )
        save_changes(new_attendance)
        return generate_token(new_attendance)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance does not exist.'
        }
        return response_object, 409

def commit_attendance(hash_key, data):
    attendance = Attendance.query.filter_by(hash_key=hash_key).first()
    if attendance:
        student = Student.query.filter_by(student_id=data['student_id']).first()
        if student:
            attendance.students.append()
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
            'message': 'Attendance does not exist.',
        }
        return response_object, 409


def remove_attendance(public_id):
    attendance = Attendance.query.filter_by(public_id=public_id).first()
    if attendance:
        attendance.delete()
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


def generate_token():
    try:
        # generate the auth token
        auth_token = Attendance.encode_auth_token(attendance.attendance_code)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()

