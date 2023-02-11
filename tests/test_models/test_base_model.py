#!/usr/bin/python3
""" Tests for class BaseModel """

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import uuid
import os
import os.path


class TestBaseModel(unittest.TestCase):
    """ Test class BaseModel """

    def __init__(self, *args, **kwargs):
        """ Initializes test models """

        super().__init__(*args, **kwargs)
        self.test_class = BaseModel
        self.test_name = "BaseModel"

    def test_id(self):
        """ Tests uniwue id """

        base = self.test_class()
        with self.subTest(msg='id is str uuid'):
            self.assertIsInstance(base.id, str)
            self.assertIsInstance(uuid.UUID(base.id), uuid.UUID)

    def test_create_datetime(self):
        """ Tests for datetime: created_at and updated_at """

        base = self.test_class()
        dt = datetime.now()
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertTrue(0 <= (dt - base.created_at).total_seconds() < 1)
        self.assertTrue(0 <= (dt - base.updated_at).total_seconds() < 1)

    def test_update_datetime(self):
        """ Tests for datetime: update datetime """

        base = self.test_class()
        dt = datetime.now
        self.assertIsInstance(base.updated_at, datetime)
        base.updated_at = datetime.now()
        self.assertNotEqual(dt, base.updated_at)

    def test_to_str(self):
        """ Tests __str__ """

        base = self.test_class()
        _pass = '[' + self.test_name + '] ({}) {}'.format(
                base.id, str(base.__dict__))
        self.assertEqual(str(base), _pass)

    def test_save_load(self):
        """ Tests save and reload """

        if os.path.exists('save.json'):
            os.remove('save.json')
        _save = FileStorage()
        _save.reload()
        _object = self.test_class()
        self.assertTrue(self.test_name + '.' + _object.id in _save.all())
