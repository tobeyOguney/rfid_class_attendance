
from flask import request
from flask_restplus import Resource

from ..util.dto import StudentDto
from ..service.student_service import (create_student, get_student,
    update_student, remove_student, get_all_students)
api = StudentDto.api
_student = StudentDto.student
_student_update = StudentDto.student_update


@api.route('/')
class Student(Resource):
    @api.doc('List Of Registered Students')
    @api.marshal_list_with(_student)
    def get(self):
        """List all registered students"""
        return get_all_students()
    
    @api.expect(_student, validate=True)
    @api.response(201, 'Student successfully created.')
    @api.doc('create a new student')
    def post(self):
        """Creates a new Student """
        data = request.json
        return create_student(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Student identifier')
@api.response(404, 'Student not found.')
class StudentProfile(Resource):
    @api.doc('get a student\'s profile')
    @api.marshal_with(_student)
    def get(self, public_id):
        """get a student\'s profile given its identifier"""
        student = get_student(public_id)
        if not student:
            api.abort(404)
        else:
            return student

    @api.doc('updates an existing student')
    @api.expect(_student_update, validate=True)
    def put(self):
        """Updates an existing Student """
        data = request.json
        return update_student(data=data)

    @api.doc('remove a student\'s profile')
    def delete(self, public_id):
        """removes a student's profile"""
        return remove_student(public_id)
    