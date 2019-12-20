import uuid
import datetime

from app.main import db
from app.main.model.lecturer import Lecturer
from app.main.model.course import Course


def save_new_lecturer(data):
    lecturer = Lecturer.query.filter_by(email=data['email']).first()
    if not lecturer:
        new_lecturer = Lecturer(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_lecturer)
        return generate_token(new_lecturer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer already exists. Please Log in.',
        }
        return response_object, 409

def register_course(data):
    course = Course.query.filter_by(id=data['course_id']).first()
    lecturer = Lecturer.query.filter_by(id=data['lecturer_id']).first()
    if course and lecturer:
        course.lecturers.append(lecturer)
        save_changes(course)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course does not exist.',
        }
        return response_object, 409

def remove_course(data):
    course = Course.query.filter_by(id=data['course_id']).first()
    lecturer = Lecturer.query.filter_by(id=data['lecturer_id']).first()
    if course and lecturer:
        course.lecturers.remove(lecturer)
        save_changes(course)
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course does not exist.',
        }
        return response_object, 409

def get_all_lecturers():
    return Lecturer.query.all()


def get_a_lecturer(public_id):
    return Lecturer.query.filter_by(public_id=public_id).first()


def generate_token(lecturer):
    try:
        # generate the auth token
        auth_token = Lecturer.encode_auth_token(lecturer.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
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

