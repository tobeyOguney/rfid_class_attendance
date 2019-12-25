import uuid
import datetime

from app.main import db
from app.main.model.lecturer import Lecturer
from app.main.model.course import Course


def create_lecturer(data):
    lecturer = Lecturer.query.filter_by(lecturer_id=data['lecturer_id']).first()
    if not lecturer:
        new_lecturer = Lecturer(
            public_id=str(uuid.uuid4()),
            lecturer_id = data['lecturer_id'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email_address = data['email_address'],
            faculty = data['faculty'],
            department = data['department'],
            level = data['level'],
            password = data['password']
        )
        save_changes(new_lecturer)
        return generate_token(new_lecturer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer already exists. Please Log in.',
        }
        return response_object, 409


def get_all_lecturers():
    return Lecturer.query.all()


def get_lecturer(public_id):
    return Lecturer.query.filter_by(public_id=public_id).first()


def update_lecturer(data):
    lecturer = Lecturer.query.filter_by(lecturer_id=data['lecturer_id']).first()
    if lecturer:
        new_lecturer = Lecturer(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email_address = data['email_address'],
            faculty = data['faculty'],
            department = data['department'],
            level = data['level'],
            password = data['password']
        )
        save_changes(new_lecturer)
        return generate_token(new_lecturer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def remove_lecturer(public_id):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        lecturer.delete()
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def get_lecturer_courses(public_id):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        courses = Course.query.filter_by(department=lecturer.department)
        return courses
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def update_lecturer_course(public_id, data):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        course = Course.query.filter_by(public_id=data['public_id'])
        lecturer.courses.append(course)
        save_changes(lecturer)
        response_object = {
            'status': 'success',
            'message': 'Successfully added.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def remove_lecturer_course():
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        course = Course.query.filter_by(public_id=data['public_id'])
        lecturer.courses.remove(course)
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def generate_token(lecturer):
    try:
        # generate the auth token
        auth_token = Lecturer.encode_auth_token(lecturer.lecturer_id)
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

