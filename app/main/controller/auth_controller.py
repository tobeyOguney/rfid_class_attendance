from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
student_auth = AuthDto.student_auth
lecturer_auth = AuthDto.lecturer_auth


@api.route('/login')
class StudentLogin(Resource):
    """
        Student Login Resource
    """
    @api.doc('student login')
    @api.expect(student_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_student(data=post_data)


@api.route('/login')
class LecturerLogin(Resource):
    """
        Lecturer Login Resource
    """
    @api.doc('lecturer login')
    @api.expect(lecturer_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_lecturer(data=post_data)


@api.route('/logout')
class StudentLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a student')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_student(data=auth_header)


@api.route('/logout')
class LecturerLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a lecturer')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_lecturer(data=auth_header)
