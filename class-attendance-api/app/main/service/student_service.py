import uuid
import datetime
import flask_bcrypt

from app.main import db
from app.main.model.student import Student
from app.main.model.course import Course


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
    students = Student.query.all()
    if students:
        return students
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def get_student(public_id):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        return student
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def update_student(public_id, data):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        student.first_name = data['first_name']
        student.last_name = data['last_name']
        student.email_address = data['email_address']
        student.faculty = data['faculty']
        student.department = data['department']
        student.level = data['level']
        student.password_hash = flask_bcrypt.generate_password_hash(data['password']).decode('utf-8')
        save_changes(student)
        return student, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def remove_student(public_id):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        Student.query.filter_by(public_id=public_id).delete()
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


def get_student_courses(public_id, registered):
    student = Student.query.filter_by(public_id=public_id).first()
    if student:
        dept_courses = Course.query.filter(Course.department==student.department or Course.strict==False).all()
        reg_courses = student.courses
        if registered:
            return reg_courses
        else:
            reg_course_ids = [str(course.public_id) for course in reg_courses]
            dept_course_ids = [str(course.public_id) for course in dept_courses]
            all_course_ids = reg_course_ids.extend(dept_course_ids)
            unreg_course_ids = list()
            for course_id in all_course_ids:
                if all_course_ids.count(course_id) == 1:
                    unreg_course_ids.append(course_id)
            unreg_courses = Course.query.filter(Course.public_id in unreg_course_ids).all()
            return unreg_courses
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student does not exist.',
        }
        return response_object, 409


def update_student_course(public_id, data):
    student = Student.query.filter_by(public_id=public_id).first()
    course = Course.query.filter_by(public_id=data['public_id']).first()
    if student and course:
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
            'message': 'Student or Course does not exist.',
        }
        return response_object, 409


def remove_student_course(public_id, data):
    student = Student.query.filter_by(public_id=public_id).first()
    course = Course.query.filter_by(public_id=data['public_id']).first()
    if student and course:
        student.courses.remove(course)
        response_object = {
            'status': 'success',
            'message': 'Successfully removed.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Student or Course does not exist.',
        }
        return response_object, 409


def generate_token(student):
    try:
        # generate the auth token
        auth_token = Student.encode_auth_token(student.student_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully created.',
            'public_id': student.public_id,
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

