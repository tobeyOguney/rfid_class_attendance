
from flask import request
from flask_restplus import Resource

from ..util.dto import CourseDto, AttendanceDto
from ..service.course_service import (create_course, get_course,
    update_course, remove_course, get_all_courses, get_course_attendances)
from ..service.lecturer_service import (get_lecturer_courses,
    update_lecturer_course, remove_lecturer_course)
from ..service.student_service import (get_student_courses,
    update_student_course, remove_student_course)
api = CourseDto.api
_course = CourseDto.course
_course_response = CourseDto.course_response
_course_id = CourseDto.course_id
_attendance_response = AttendanceDto.attendance_response
_registered = CourseDto.registered


@api.route('/')
class Course(Resource):
    @api.doc('get all courses')
    @api.marshal_list_with(_course_response)
    def get(self):
        """Returns all courses"""
        return get_all_courses()

    @api.expect(_course, validate=True)
    @api.response(201, 'Course successfully created.')
    @api.doc('create a new course')
    @api.marshal_with(_course_response)
    def post(self):
        """Creates a new Course """
        data = request.json
        return create_course(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Course identifier')
@api.response(404, 'Course not found.')
class CourseProfile(Resource):
    @api.doc('get a course\'s profile')
    @api.marshal_with(_course_response)
    def get(self, public_id):
        """get a course\'s profile given its identifier"""
        course = get_course(public_id)
        return course

    @api.doc('updates an existing course')
    @api.expect(_course, validate=True)
    @api.marshal_with(_course_response)
    def put(self, public_id):
        """Updates an existing Course """
        data = request.json
        return update_course(public_id, data=data)

    @api.doc('remove a course\'s profile')
    def delete(self, public_id):
        """removes a course's profile"""
        return remove_course(public_id)


@api.route('/student/<public_id>')
@api.param('public_id', 'The Student identifier')
@api.response(404, 'Student not found.')
class StudentCourse(Resource):
    @api.doc('get courses available to the student')
    @api.marshal_list_with(_course_response)
    @api.expect(_registered, validate=True)
    def post(self, public_id):
        """get courses available to the student"""
        data = request.json
        courses = get_student_courses(public_id, data['registered'])
        return courses

    @api.doc('add course to student')
    @api.expect(_course_id, validate=True)
    def put(self, public_id):
        """Add course to student """
        data = request.json
        return update_student_course(public_id=public_id, data=data)

    @api.doc('remove course from student')
    @api.expect(_course_id, validate=True)
    def delete(self, public_id):
        """removes course from student"""
        data = request.json
        return remove_student_course(public_id=public_id, data=data)

@api.route('/lecturer/<public_id>')
@api.param('public_id', 'The Lecturer identifier')
@api.response(404, 'Lecturer not found.')
class LecturerCourse(Resource):
    @api.doc('get courses available to the lecturer')
    @api.marshal_with(_course_response)
    @api.expect(_registered, validate=True)
    def post(self, public_id):
        """get courses available to the lecturer"""
        data = request.json
        courses = get_lecturer_courses(public_id, data['registered'])
        return courses

    @api.doc('add course to lecturer')
    @api.expect(_course_id, validate=True)
    def put(self, public_id):
        """Add course to lecturer """
        data = request.json
        return update_lecturer_course(public_id=public_id, data=data)

    @api.doc('remove course from lecturer')
    @api.expect(_course_id, validate=True)
    def delete(self, public_id):
        """removes course from lecturer"""
        data = request.json
        return remove_lecturer_course(public_id=public_id, data=data)


@api.route('/attendance/<public_id>')
@api.param('public_id', 'The Course identifier')
@api.response(404, 'Course not found.')
class CourseAttendance(Resource):
    @api.doc('get attendances available to the course')
    @api.marshal_with(_attendance_response)
    def get(self, public_id):
        """get attendances available to the course"""
        attendances = get_course_attendances(public_id)
        return attendances
