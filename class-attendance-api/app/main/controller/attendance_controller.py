
from flask import request
from flask_restplus import Resource

from ..util.dto import AttendanceDto, StudentDto
from ..service.attendance_service import (create_attendance, get_attendance,
    update_attendance, remove_attendance, commit_attendance)
api = AttendanceDto.api
_attendance = AttendanceDto.attendance
_student_id = StudentDto.student_id


@api.route('/')
class Attendance(Resource):
    @api.expect(_attendance, validate=True)
    @api.response(201, 'Attendance successfully created.')
    @api.doc('create a new attendance')
    def post(self):
        """Creates a new Attendance """
        data = request.json
        return create_attendance(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Attendance identifier')
@api.response(404, 'Attendance not found.')
class AttendanceProfile(Resource):
    @api.doc('get a attendance\'s profile')
    @api.marshal_with(_attendance)
    def get(self, public_id):
        """get a attendance\'s profile given its identifier"""
        attendance = get_attendance(public_id)
        if not attendance:
            api.abort(404)
        else:
            return attendance

    @api.doc('updates an existing attendance')
    @api.expect(_attendance, validate=True)
    def put(self, public_id):
        """Updates an existing Attendance """
        data = request.json
        return update_attendance(public_id=public_id, data=data)

    @api.doc('remove a attendance\'s profile')
    def delete(self, public_id):
        """removes a attendance's profile"""
        return remove_attendance(public_id)


@api.route('/commit/<hash_key>')
@api.param('hash_key', 'The Attendance hash key')
@api.response(404, 'Attendance not found.')
class AttendanceSession(Resource):
    @api.doc('commit to an attendance session')
    @api.expect(_student_id, validate=True)
    def put(self, hash_key):
        data = request.json
        return commit_attendance(hash_key=hash_key, data=data)
