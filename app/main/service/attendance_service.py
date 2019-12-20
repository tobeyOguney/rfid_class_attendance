import uuid

from app.main import db
from app.main.model.attendance import Attendance


def save_new_attendance(data):
    new_attendance = Attendance(
        public_id=str(uuid.uuid4()),
        course_code=data['course_code'],
    )
    save_changes(new_attendance)
    return generate_token(new_attendance)


def update_attendance(data):
    attendance = Attendance.query.filter_by(public_id=data['attendance_id']).first()
    course = Course.query.filter_by(public_id=data['course_id']).first()
    if attendance and course:
        course.attendances.append(attendance)
        save_changes(course)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Attendance session does not exist.',
        }
        return response_object, 409


def get_all_attendances():
    return Attendance.query.all()


def get_an_attendance(public_id):
    return Attendance.query.filter_by(public_id=public_id).first()


def generate_token(attendance):
    try:
        # generate the auth token
        auth_token = Attendance.encode_auth_token(attendance.id)
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

