import unittest

import datetime

from app.main import db
from app.main.model.student import Student
from app.test.base import BaseTestCase


class TestStudentModel(BaseTestCase):

    def test_encode_auth_token(self):
        student = Student(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(student)
        db.session.commit()
        auth_token = Student.encode_auth_token(student.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        student = Student(
            email='test@test.com',
            password='test',
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(student)
        db.session.commit()
        auth_token = Student.encode_auth_token(student.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(Student.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()

