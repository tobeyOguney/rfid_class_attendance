from flask import request
from flask_restplus import Resource

from app.main.util.decorator import student_admin_token_required
from ..util.dto import StudentDto
from ..service.student_service import (save_new_student, get_all_students, get_a_student,
    register_course, remove_course)
from ..service.course_service import get_a_course, get_all_courses, save_new_course

api = StudentDto.api
_student = StudentDto.student


@api.route('/')
class StudentList(Resource):
    @api.doc('list_of_registered_students')
    @student_admin_token_required
    @api.marshal_list_with(_student, envelope='data')
    def get(self):
        """List all registered students"""
        return get_all_students()

    @api.expect(_student, validate=True)
    @api.response(201, 'Student successfully created.')
    @api.doc('create a new student')
    def post(self):
        """Creates a new Student """
        data = request.json
        return save_new_student(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Student identifier')
@api.response(404, 'Student not found.')
class Student(Resource):
    @api.doc('get a student')
    @api.marshal_with(_student)
    def get(self, public_id):
        """get a student given its identifier"""
        student = get_a_student(public_id)
        if not student:
            api.abort(404)
        else:
            return student



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
class Student(Resource):
    @api.response(201, 'Course successfully registered.')
    @api.doc('register a course')
    def post(self):
        """Registers a Course """
        data = request.json
        return register_course(data=data)


@api.route('/course/remove')
@api.response(404, 'Course not found.')
class Student(Resource):
    @api.response(201, 'Course successfully removed.')
    @api.doc('remove a course')
    def post(self):
        """Removes a Course """
        data = request.json
        return remove_course(data=data)
