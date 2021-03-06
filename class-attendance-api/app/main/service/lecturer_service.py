import uuid
import datetime
import flask_bcrypt
from sqlalchemy import or_, and_

from app.main import db
from app.main.model.lecturer import Lecturer
from app.main.model.course import Course


def create_lecturer(data):
    lecturer = Lecturer.query.filter(or_(Lecturer.email_address==data['email_address'], Lecturer.lecturer_id==data['lecturer_id'])).first()
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
    lecturers = Lecturer.query.all()
    if lecturers:
        return lecturers
    else:
        response_object = {
            'status': 'fail',
            'message': 'No Lecturer exists.',
        }
        return response_object, 409


def get_lecturer(public_id):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        return lecturer
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def update_lecturer(public_id, data):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        lecturer.first_name = data['first_name']
        lecturer.last_name = data['last_name']
        lecturer.email_address = data['email_address']
        lecturer.faculty = data['faculty']
        lecturer.department = data['department']
        lecturer.level = data['level']
        lecturer.password_hash = flask_bcrypt.generate_password_hash(data['password']).decode('utf-8')
        save_changes(lecturer)
        return lecturer, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def remove_lecturer(public_id):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        lecturer.courses.clear()
        lecturer.attendance_sessions.clear()
        db.session.add(lecturer)
        db.session.delete(lecturer)
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


def get_lecturer_courses(public_id, registered):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    if lecturer:
        reg_courses = lecturer.courses
        unreg_courses = Course.query.filter(
            and_(
                or_(Course.department==lecturer.department, Course.strict==False),
                ~Course.public_id.in_([course.public_id for course in lecturer.courses])
            )
        ).all()
        if registered:
            return reg_courses
        else:
            return unreg_courses
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer does not exist.',
        }
        return response_object, 409


def update_lecturer_course(public_id, data):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    course = Course.query.filter_by(public_id=data['public_id']).first()
    if lecturer and course:
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
            'message': 'Lecturer or Course does not exist.',
        }
        return response_object, 409


def remove_lecturer_course(public_id, data):
    lecturer = Lecturer.query.filter_by(public_id=public_id).first()
    course = Course.query.filter_by(public_id=data['public_id']).first()
    if lecturer and course:
        lecturer.courses.remove(course)
        save_changes(lecturer)
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lecturer or Course does not exist.',
        }
        return response_object, 409


def generate_token(lecturer):
    try:
        # generate the auth token
        auth_token = Lecturer.encode_auth_token(lecturer.lecturer_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.',
            'public_id': lecturer.public_id,
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

