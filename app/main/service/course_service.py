import uuid

from app.main import db
from app.main.model.course import Course


def save_new_course(data):
    course = Course.query.filter_by(code=data['code']).first()
    if not course:
        new_course = Course(
            public_id=str(uuid.uuid4()),
            code=data['code'],
            title=data['title']
        )
        save_changes(new_course)
        return generate_token(new_course)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Course already exists.',
        }
        return response_object, 409


def get_all_courses():
    return Course.query.all()


def get_a_course(public_id):
    return Course.query.filter_by(public_id=public_id).first()


def generate_token(course):
    try:
        # generate the auth token
        auth_token = Course.encode_auth_token(course.id)
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

