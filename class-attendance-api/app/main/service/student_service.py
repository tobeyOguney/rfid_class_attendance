import uuid
import datetime

from app.main import db
from app.main.model.student import Student


def create_student(data):
    student = Student.query.filter_by(student_id=data['student_id']).first()
    if not student:
        new_student = Student(
            public_id=str(uuid.uuid4()),
            student_id = data['student_id'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email_address = data['email_address'],
            faculty = data['faculty'],
            department = data['department'],
            level = data['level'],
            password = data['password']
        )
        save_changes(new_student)
        return generate_token(new_student)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student already exists. Please Log in.',
        }
        return response_object, 409


def get_all_students():
    return Student.query.all()


def get_student(public_id):
    return Student.query.filter_by(public_id=public_id).first()


def update_student(data):
    student = Student.query.filter_by(student_id=data['student_id']).first()
    if student:
        new_student = Student(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email_address = data['email_address'],
            faculty = data['faculty'],
            department = data['department'],
            level = data['level'],
            password = data['password']
        )
        save_changes(new_student)
        return generate_token(new_student)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def remove_student(public_id):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        student.delete()
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def get_student_courses(public_id):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        courses = Course.query.filter_by(department=student.department)
        return courses
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def update_student_course(public_id, data):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        course = Course.query.filter_by(public_id=data['public_id'])
        student.courses.append(course)
        save_changes(student)
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


def remove_student_course():
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        course = Course.query.filter_by(public_id=data['public_id'])
        student.courses.remove(course)
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


def generate_token(student):
    try:
        # generate the auth token
        auth_token = Student.encode_auth_token(student.student_id)
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

