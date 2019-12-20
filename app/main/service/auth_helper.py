# from app.main.model.user import User
from app.main.model.student import Student
from app.main.model.lecturer import Lecturer
from ..service.blacklist_service import save_token


class Auth:


    @staticmethod
    def login_student(data):
        try:
            # fetch the student data
            student = Student.query.filter_by(email=data.get('email')).first()
            if student and student.check_password(data.get('password')):
                auth_token = Student.encode_auth_token(student.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def login_lecturer(data):
        try:
            # fetch the lecturer data
            lecturer = Lecturer.query.filter_by(email=data.get('email')).first()
            if lecturer and lecturer.check_password(data.get('password')):
                auth_token = Lecturer.encode_auth_token(lecturer.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500


    @staticmethod
    def logout_student(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Student.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def logout_lecturer(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Lecturer.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403


    @staticmethod
    def get_logged_in_student(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Student.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                student = Student.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'student_id': student.id,
                        'email': student.email,
                        'admin': student.admin,
                        'registered_on': str(student.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401


    @staticmethod
    def get_logged_in_lecturer(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Lecturer.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                lecturer = Lecturer.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'lecturer_id': lecturer.id,
                        'email': lecturer.email,
                        'admin': lecturer.admin,
                        'registered_on': str(lecturer.registered_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
