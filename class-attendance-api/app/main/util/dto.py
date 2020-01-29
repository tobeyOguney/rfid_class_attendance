from flask_restplus import Namespace, fields




class StudentDto:
    api = Namespace('student', description='student related operations')
    student = api.model('student', {
        "student_id": fields.String(required=True, description="student's ID number"),
        "rf_id": fields.String(required=True, description="student's RFID number"),
        "first_name": fields.String(required=True, description="student's first name"),
        "last_name": fields.String(required=True, description="student's last name"),
        "email_address": fields.String(required=True, description="student's email address"),
        "faculty": fields.String(required=True, description="student's faculty"),
        "department": fields.String(required=True, description="student's department"),
        "level": fields.String(required=True, description="student's level"),
        "password": fields.String(required=True, description="student's password")
    })
    student_update = api.model('student_update', {
        "rf_id": fields.String(required=True, description="student's RFID number"),
        "first_name": fields.String(required=True, description="student's first name"),
        "last_name": fields.String(required=True, description="student's last name"),
        "email_address": fields.String(required=True, description="student's email address"),
        "faculty": fields.String(required=True, description="student's faculty"),
        "department": fields.String(required=True, description="student's department"),
        "level": fields.String(required=True, description="student's level"),
        "password": fields.String(required=True, description="student's password") 
    })
    student_response = api.model('student_response', {
        "student_id": fields.String(required=True, description="student's ID number"),
        "rf_id": fields.String(required=True, description="student's RFID number"),
        "first_name": fields.String(required=True, description="student's first name"),
        "last_name": fields.String(required=True, description="student's last name"),
        "email_address": fields.String(required=True, description="student's email address"),
        "faculty": fields.String(required=True, description="student's faculty"),
        "department": fields.String(required=True, description="student's department"),
        "level": fields.String(required=True, description="student's level"),
        "public_id": fields.String(required=True, description="student's public identifier")
    })
    student_id = api.model('student_id', {
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
    lecturer_update = api.model('lecturer_update', {
        "first_name": fields.String(required=True, description="lecturer's first name"),
        "last_name": fields.String(required=True, description="lecturer's last name"),
        "email_address": fields.String(required=True, description="lecturer's email address"),
        "faculty": fields.String(required=True, description="lecturer's faculty"),
        "department": fields.String(required=True, description="lecturer's department"),
        "level": fields.String(required=True, description="lecturer's level"),
        "password": fields.String(required=True, description="lecturer's password"),
    })
    lecturer_response = api.model('lecturer_response', {
        "lecturer_id": fields.String(required=True, description="lecturer's ID number"),
        "first_name": fields.String(required=True, description="lecturer's first name"),
        "last_name": fields.String(required=True, description="lecturer's last name"),
        "email_address": fields.String(required=True, description="lecturer's email address"),
        "faculty": fields.String(required=True, description="lecturer's faculty"),
        "department": fields.String(required=True, description="lecturer's department"),
        "level": fields.String(required=True, description="lecturer's level"),
        "public_id": fields.String(required=True, description="lecturer's public identifier"),
    })


class CourseDto:
    api = Namespace('course', description='course related operations')
    course = api.model('course', {
        "faculty": fields.String(required=True, description="course's faculty"),
        "department": fields.String(required=True, description="course's department"),
        "course_code": fields.String(required=True, description="course's code"),
        "course_title": fields.String(required=True, description="course's title"),
        "strict": fields.Boolean(required=True, description="course's exclusiveness"),
    })
    course_id = api.model('course_id', {
        "public_id": fields.String(required=True, description="course's public identifier")
    })
    registered = api.model('registered', {
        "registered": fields.Boolean(required=True, description="indicates if course is registered or not")
    })
    course_response = api.model('course_response', {
        "faculty": fields.String(required=True, description="course's faculty"),
        "department": fields.String(required=True, description="course's department"),
        "course_code": fields.String(required=True, description="course's code"),
        "course_title": fields.String(required=True, description="course's title"),
        "strict": fields.Boolean(required=True, description="course's exclusiveness"),
        "public_id": fields.String(required=True, description="course's public identifier")
    })


class AttendanceDto:
    api = Namespace('attendance', description='attendance related operations')
    attendance = api.model('attendance', {
        "session": fields.String(required=True, description="academic session"),
        "semester": fields.String(required=True, description="academic semester"),
        "course_code": fields.String(required=True, description="associated course"),
        "lecturer_id": fields.String(required=True, description="creating lecturer")
    })
    attendance_response = api.model('attendance_response', {
        "session": fields.String(required=True, description="academic session"),
        "semester": fields.String(required=True, description="academic semester"),
        "hash_key": fields.Integer(required=True, description="Hash Key"),
        "open": fields.Boolean(required=True, description="Ongoing Session"),
        "public_id": fields.String(required=True, description="Public Identifier")
    })
    attendance_update = api.model('attendance_update', {
        "session": fields.String(required=True, description="academic session"),
        "semester": fields.String(required=True, description="academic semester")
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    student_auth = api.model('student_auth', {
        'email_address': fields.String(required=True, description='The student email address'),
        'password': fields.String(required=True, description='The student password '),
    })
    lecturer_auth = api.model('lecturer_auth', {
        'email_address': fields.String(required=True, description='The lecturer email address'),
        'password': fields.String(required=True, description='The lecturer password '),
    })
