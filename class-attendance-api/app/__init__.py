from flask_restplus import Api
from flask import Blueprint

from .main.controller.attendance_controller import api as attendance_ns
from .main.controller.student_controller import api as student_ns
from .main.controller.lecturer_controller import api as lecturer_ns
from .main.controller.course_controller import api as course_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='CLASS ATTENDANCE SYSTEM API',
          version='1.0',
          description='a web service for class attendance'
          )

api.add_namespace(attendance_ns, path='/attendance')
api.add_namespace(student_ns, path='/student')
api.add_namespace(lecturer_ns, path='/lecturer')
api.add_namespace(course_ns, path='/course')
api.add_namespace(auth_ns)