import uuid
import datetime

from app.main import db
from app.main.model.student import Student


def save_new_student(data):
    student = Student.query.filter_by(email=data['email']).first()
    if not student:
        new_student = Student(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_student)
        return generate_token(new_student)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student already exists. Please Log in.',
        }
        return response_object, 409


def register_course(data):
    course = Course.query.filter_by(id=data['course_id']).first()
    student = Student.query.filter_by(id=data['student_id']).first()
    if course and student:
        course.students.append(student)
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
    student = Student.query.filter_by(id=data['student_id']).first()
    if course and student:
        course.students.remove(student)
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


def get_all_students():
    return Student.query.all()


def get_a_student(public_id):
    return Student.query.filter_by(public_id=public_id).first()


def generate_token(student):
    try:
        # generate the auth token
        auth_token = Student.encode_auth_token(student.id)
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

