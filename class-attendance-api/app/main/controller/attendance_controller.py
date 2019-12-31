
from flask import request
from flask_restplus import Resource

from ..util.dto import AttendanceDto, StudentDto
from ..service.attendance_service import (create_attendance, get_attendance, get_students,
    update_attendance, remove_attendance, commit_attendance, close_attendance, check_attendance)
api = AttendanceDto.api
_attendance = AttendanceDto.attendance
_attendance_update = AttendanceDto.attendance_update
_attendance_response = AttendanceDto.attendance_response
_student_id = StudentDto.student_id
_student_response = StudentDto.student_response


@api.route('/')
class Attendance(Resource):
    @api.expect(_attendance, validate=True)
    @api.response(201, 'Attendance successfully created.')
    @api.doc('create a new attendance')
    @api.marshal_with(_attendance_response)
    def post(self):
        """Creates a new Attendance """
        data = request.json
        return create_attendance(data=data)


@api.route('/student/<public_id>')
@api.param('public_id', 'The Attendance identifier')
class StudentAttendance(Resource):
    @api.doc('List Of Commited Students')
    @api.marshal_list_with(_student_response)
    def get(self, public_id):
        """List all commited students"""
        return get_students(public_id)


@api.route('/profile/<public_id>')
@api.param('public_id', 'The Attendance identifier')
@api.response(404, 'Attendance not found.')
class AttendanceProfile(Resource):
    @api.doc('get a attendance\'s profile')
    @api.marshal_with(_attendance_response)
    def get(self, public_id):
        """get a attendance\'s profile given its identifier"""
        attendance = get_attendance(public_id)
        return attendance

    @api.doc('updates an existing attendance')
    @api.expect(_attendance_update, validate=True)
    @api.marshal_with(_attendance_response)
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
class CommitAttendanceSession(Resource):
    @api.doc('commit to an attendance session')
    @api.expect(_student_id, validate=True)
    def put(self, hash_key):
        """commits to an attendance session"""
        data = request.json
        return commit_attendance(hash_key=hash_key, data=data)


@api.route('/check/<hash_key>')
@api.param('hash_key', 'The Attendance hash key')
@api.response(404, 'Attendance not found.')
class CheckAttendanceSession(Resource):
    @api.doc('check an attendance session')
    def get(self, hash_key):
        """checks an attendance session"""
        return check_attendance(hash_key)


@api.route('/close/<public_id>')
@api.param('public_id', 'The Attendance public identifier')
@api.response(404, 'Attendance not found.')
class CloseAttendanceSession(Resource):
    @api.doc('close an attendance session')
    def put(self, public_id):
        """closes an attendance session"""
        return close_attendance(public_id)

