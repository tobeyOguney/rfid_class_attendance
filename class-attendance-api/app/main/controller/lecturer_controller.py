
from flask import request
from flask_restplus import Resource

from ..util.dto import LecturerDto
from ..service.lecturer_service import (create_lecturer, get_lecturer,
    update_lecturer, remove_lecturer, get_all_lecturers)
api = LecturerDto.api
_lecturer = LecturerDto.lecturer
_lecturer_update = LecturerDto.lecturer_update


@api.route('/')
class Lecturer(Resource):
    @api.doc('List Of Registered Lecturers')
    @api.marshal_list_with(_lecturer)
    def get(self):
        """List all registered lecturers"""
        return get_all_lecturers()
    
    @api.expect(_lecturer, validate=True)
    @api.response(201, 'Lecturer successfully created.')
    @api.doc('create a new lecturer')
    def post(self):
        """Creates a new Lecturer """
        data = request.json
        return create_lecturer(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The Lecturer identifier')
@api.response(404, 'Lecturer not found.')
class LecturerProfile(Resource):
    @api.doc('get a lecturer\'s profile')
    @api.marshal_with(_lecturer)
    def get(self, public_id):
        """get a lecturer\'s profile given its identifier"""
        lecturer = get_lecturer(public_id)
        if not lecturer:
            api.abort(404)
        else:
            return lecturer

    @api.doc('updates an existing lecturer')
    @api.expect(_lecturer_update, validate=True)
    def put(self):
        """Updates an existing Lecturer """
        data = request.json
        return update_lecturer(data=data)

    @api.doc('remove a lecturer\'s profile')
    def delete(self, public_id):
        """removes a lecturer's profile"""
        return remove_lecturer(public_id)
    