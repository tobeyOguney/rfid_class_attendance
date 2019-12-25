from flask_restplus import Namespace, fields




class StudentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        "student_id": fields.String(required=True, description="student's ID number"),
        "first_name": fields.String(required=True, description="student's first name"),
        "last_name": fields.String(required=True, description="student's last name"),
        "email_address": fields.String(required=True, description="student's email address"),
        "faculty": fields.String(required=True, description="student's faculty"),
        "department": fields.String(required=True, description="student's department"),
        "level": fields.String(required=True, description="student's level"),
        "password": fields.String(required=True, description="student's password")
    })
    student_update = api.model('student', {
        "first_name": fields.String(required=True, description="student's first name"),
        "last_name": fields.String(required=True, description="student's last name"),
        "email_address": fields.String(required=True, description="student's email address"),
        "faculty": fields.String(required=True, description="student's faculty"),
        "department": fields.String(required=True, description="student's department"),
        "level": fields.String(required=True, description="student's level")
    })
    student_id = api.model('student', {
        "student_id": fields.String(required=True, description="student's ID number")
    })


class LecturerDto:
    api = Namespace('lecturer', description='lecturer related operations')
    lecturer = api.model('lecturer', {
        "lecturer_id": fields.String(required=True, description="lecturer's ID number"),
        "first_name": fields.String(required=True, description="lecturer's first name"),
        "last_name": fields.String(required=True, description="lecturer's last name"),
        "email_address": fields.String(required=True, description="lecturer's email address"),
        "faculty": fields.String(required=True, description="lecturer's faculty"),
        "department": fields.String(required=True, description="lecturer's department"),
        "level": fields.String(required=True, description="lecturer's level"),
        "password": fields.String(required=True, description="lecturer's password"),
    })
    lecturer_update = api.model('lecturer', {
        "first_name": fields.String(required=True, description="lecturer's first name"),
        "last_name": fields.String(required=True, description="lecturer's last name"),
        "email_address": fields.String(required=True, description="lecturer's email address"),
        "faculty": fields.String(required=True, description="lecturer's faculty"),
        "department": fields.String(required=True, description="lecturer's department"),
        "level": fields.String(required=True, description="lecturer's level"),
    })


class CourseDto:
    api = Namespace('course', description='course related operations')
    course = api.model('course', {
        "faculty": fields.String(required=True, description="course's faculty"),
        "department": fields.String(required=True, description="course's department"),
        "course_code": fields.String(required=True, description="course's code"),
        "course_title": fields.String(required=True, description="course's title"),
        "strict": fields.String(required=True, description="course's exclusiveness")
    })


class AttendanceDto:
    api = Namespace('attendance', description='attendance related operations')
    attendance = api.model('attendance', {
        "session": fields.String(required=True, description="academic session"),
        "semester": fields.String(required=True, description="academic semester"),
        "course": fields.String(required=True, description="associated course")
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    student_auth = api.model('auth_details', {
        'email_address': fields.String(required=True, description='The student email address'),
        'password': fields.String(required=True, description='The student password '),
    })
    lecturer_auth = api.model('auth_details', {
        'email_address': fields.String(required=True, description='The lecturer email address'),
        'password': fields.String(required=True, description='The lecturer password '),
    })
