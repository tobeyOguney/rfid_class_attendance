from flask import request
from flask_restplus import Resource

from app.main.util.decorator import lecturer_admin_token_required
from ..util.dto import LecturerDto
from ..service.lecturer_service import (save_new_lecturer, get_all_lecturers, get_a_lecturer,
    register_course, remove_course)
from ..service.course_service import get_a_course, get_all_courses, save_new_course
from ..service.attendance_service import get_an_attendance, get_all_attendances, save_new_attendance, update_attendance

api = LecturerDto.api
_lecturer = LecturerDto.lecturer


@api.route('/')
class LecturerList(Resource):
    @api.doc('list_of_registered_lecturers')
    @lecturer_admin_token_required
    @api.marshal_list_with(_lecturer, envelope='data')
    def get(self):
        """List all registered lecturers"""
        return get_all_lecturers()

    @api.expect(_lecturer, validate=True)
    @api.response(201, 'Lecturer successfully created.')
    @api.doc('create a new lecturer')
    def post(self):
        """Creates a new Lecturer """
        data = request.json
        return save_new_lecturer(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Lecturer identifier')
@api.response(404, 'Lecturer not found.')
class Lecturer(Resource):
    @api.doc('get a lecturer')
    @api.marshal_with(_lecturer)
    def get(self, public_id):
        """get a lecturer given its identifier"""
        lecturer = get_a_lecturer(public_id)
        if not lecturer:
            api.abort(404)
        else:
            return lecturer


@api.route('/course')
class CourseList(Resource):
    @api.doc('list_of_registered_courses')
    def get(self):
        """List all registered courses"""
        return get_all_courses()

    @api.response(201, 'Course successfully created.')
    @api.doc('create a new course')
    def post(self):
        """Creates a new Course """
        data = request.json
        return save_new_course(data=data)


@api.route('/course/<public_id>')
@api.param('public_id', 'The Course identifier')
@api.response(404, 'Course not found.')
class Course(Resource):
    @api.doc('get a course')
    def get(self, public_id):
        """get a course given its identifier"""
        course = get_a_course(public_id)
        if not course:
            api.abort(404)
        else:
            return course


@api.route('/course/register')
@api.response(404, 'Course not found.')
class Lecturer(Resource):
    @api.response(201, 'Course successfully registered.')
    @api.doc('register a course')
    def post(self):
        """Registers a Course """
        data = request.json
        return register_course(data=data)


@api.route('/course/remove')
@api.response(404, 'Course not found.')
class Lecturer(Resource):
    @api.response(201, 'Course successfully removed.')
    @api.doc('remove a course')
    def post(self):
        """Removes a Course """
        data = request.json
        return remove_course(data=data)

@api.route('/attendance')
class CourseList(Resource):
    @api.doc('list_of_attendance_taken')
    def get(self):
        """List all taken attendance"""
        return get_all_attendances()

    @api.response(201, 'Attendance successfully created.')
    @api.doc('create a new attendance')
    def post(self):
        """Creates a new Attendance """
        data = request.json
        return save_new_attendance(data=data)


@api.route('/attendance/<public_id>')
@api.param('public_id', 'The Attendance identifier')
@api.response(404, 'Attendance not found.')
class Course(Resource):
    @api.doc('get an attendance')
    def get(self, public_id):
        """get an attendance given its identifier"""
        attendance = get_an_attendance(public_id)
        if not attendance:
            api.abort(404)
        else:
            return attendance

    @api.doc('update an attendance')
    def put(self, public_id):
        """updates an attendance given its identifier"""
        data = request.json
        return update_attendance(data=data)
