from app.main.model.student import Student
from app.main.model.lecturer import Lecturer
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_student(data):
        try:
            # fetch the student data
            student = Student.query.filter_by(email_address=data.get('email_address')).first()
            if student and student.check_password(data.get('password')):
                auth_token = Student.encode_auth_token(student.student_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'public_id': student.public_id,
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
    def get_logged_in_student(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Student.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                student = Student.query.filter_by(student_id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'student_id': student.student_id,
                        'public_id': student.public_id,
                        'email_address': student.email_address,
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
    def login_lecturer(data):
        try:
            # fetch the lecturer data
            lecturer = Lecturer.query.filter_by(email_address=data.get('email_address')).first()
            if lecturer and lecturer.check_password(data.get('password')):
                auth_token = Lecturer.encode_auth_token(lecturer.lecturer_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'public_id': lecturer.public_id,
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
    def get_logged_in_lecturer(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = Lecturer.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                lecturer = Lecturer.query.filter_by(lecturer_id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'lecturer_id': lecturer.lecturer_id,
                        'public_id': lecturer.public_id,
                        'email_address': lecturer.email_address
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
