
from flask import request
from flask_restplus import Resource

from ..util.dto import CourseDto
from ..service.course_service import (create_course, get_course,
    update_course, remove_course, get_all_courses, get_course_attendances)
from ..service.lecturer_service import (get_lecturer_courses,
    update_lecturer_course, remove_lecturer_course)
from ..service.student_service import (get_student_courses,
    update_student_course, remove_student_course)
api = CourseDto.api
_course = CourseDto.course


@api.route('/')
class Course(Resource):
    @api.expect(_course, validate=True)
    @api.response(201, 'Course successfully created.')
    @api.doc('create a new course')
    def post(self):
        """Creates a new Course """
        data = request.json
        return create_course(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Course identifier')
@api.response(404, 'Course not found.')
class CourseProfile(Resource):
    @api.doc('get a course\'s profile')
    @api.marshal_with(_course)
    def get(self, public_id):
        """get a course\'s profile given its identifier"""
        course = get_course(public_id)
        if not course:
            api.abort(404)
        else:
            return course

    @api.doc('updates an existing course')
    @api.expect(_course, validate=True)
    def put(self):
        """Updates an existing Course """
        data = request.json
        return update_course(data=data)

    @api.doc('remove a course\'s profile')
    def delete(self, public_id):
        """removes a course's profile"""
        return remove_course(public_id)


@api.route('/student/<public_id>')
@api.param('public_id', 'The Student identifier')
@api.response(404, 'Student not found.')
class StudentCourse(Resource):
    @api.doc('get courses available to the student')
    @api.marshal_list_with(_course)
    def get(self, public_id):
        """get courses available to the student"""
        courses = get_student_courses(public_id)
        if not course:
            api.abort(404)
        else:
            return courses

    @api.doc('add course to student')
    @api.expect(_course, validate=True)
    def put(self, public_id):
        """Add course to student """
        data = request.json
        return update_student_course(public_id=public_id, data=data)

    @api.doc('remove course from student')
    @api.expect(_course, validate=True)
    def delete(self, public_id):
        """removes course from student"""
        data = request.json
        return remove_student_course(public_id=public_id, data=data)

@api.route('/lecturer/<public_id>')
@api.param('public_id', 'The Lecturer identifier')
@api.response(404, 'Lecturer not found.')
class LecturerCourse(Resource):
    @api.doc('get courses available to the lecturer')
    @api.marshal_with(_course)
    def get(self, public_id):
        """get courses available to the lecturer"""
        courses = get_lecturer_courses(public_id)
        if not course:
            api.abort(404)
        else:
            return courses

    @api.doc('add course to lecturer')
    def put(self, public_id):
        """Add course to lecturer """
        data = request.json
        return update_lecturer_course(public_id=public_id, data=data)

    @api.doc('remove course from lecturer')
    @api.marshal_with(_course)
    def delete(self, public_id):
        """removes course from lecturer"""
        data = request.json
        return remove_lecturer_course(public_id=public_id, data=data)


@api.route('/attendance/<public_id>')
@api.param('public_id', 'The Course identifier')
@api.response(404, 'Course not found.')
class CourseAttendance(Resource):
    @api.doc('get attendances available to the course')
    def get(self, public_id):
        """get attendances available to the course"""
        attendances = get_course_attendances(public_id)
        if not course:
            api.abort(404)
        else:
            return attendances
