import uuid
import datetime

from app.main import db
from app.main.model.course import Course


def create_course(data):
    course = Course.query.filter_by(course_code=data['course_code']).first()
    if not course:
        new_course = Course(
            public_id=str(uuid.uuid4()),
            course_code = data['course_code'],
            course_title = data['course_title'],
            strict = data['strict'],
            faculty = data['faculty'],
            department = data['department']
        )
        save_changes(new_course)
        return new_course, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course already exists.',
        }
        return response_object, 409


def get_all_courses():
    courses = Course.query.all()
    if courses:
        return courses
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course does not exist.',
        }
        return response_object, 409


def get_course(public_id):
    course = Course.query.filter_by(public_id=public_id).first()
    if course:
        return course
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course does not exist.'
        }
        return response_object, 409


def update_course(public_id, data):
    course = Course.query.filter_by(public_id=public_id).first()
    if course:
        course.course_code = data['course_code']
        course.course_title = data['course_title']
        course.strict = data['strict']
        course.faculty = data['faculty']
        course.department = data['department']
        save_changes(course)
        return course, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course does not exist.',
        }
        return response_object, 409


def remove_course(public_id):
    course = Course.query.filter_by(public_id=public_id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
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

def get_course_attendances(public_id):
    course = Course.query.filter_by(public_id=public_id).first()
    attendances = course.attendance_sessions
    if course and attendances:
        return attendances
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course or Attendance does not exist.',
        }
        return response_object, 409


def generate_token(course):
    try:
        # generate the auth token
        auth_token = Course.encode_auth_token(course.course_code)
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

