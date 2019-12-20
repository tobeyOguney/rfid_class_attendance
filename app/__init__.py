from flask_restplus import Api
from flask import Blueprint

from .main.controller.student_controller import api as student_ns
from .main.controller.lecturer_controller import api as lecturer_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='RFID Class Attendance System',
          version='1.0',
          description='a rest api for administration of class attendance issues'
          )

#api.add_namespace(user_ns, path='/user')
api.add_namespace(student_ns, path='/student')
api.add_namespace(lecturer_ns, path='/lecturer')
api.add_namespace(auth_ns)