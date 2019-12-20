from flask_restplus import Namespace, fields


class StudentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        'email': fields.String(required=True, description='student email address'),
        'username': fields.String(required=True, description='student username'),
        'password': fields.String(required=True, description='student password'),
    })


class LecturerDto:
    api = Namespace('lecturer', description='lecturer related operations')
    lecturer = api.model('lecturer', {
        'email': fields.String(required=True, description='lecturer email address'),
        'username': fields.String(required=True, description='lecturer username'),
        'password': fields.String(required=True, description='lecturer password'),
    })
    

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    student_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The student password '),
    })
    lecturer_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The lecturer password '),
    })
