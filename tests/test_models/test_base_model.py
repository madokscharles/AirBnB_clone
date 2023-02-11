#!/usr/bin/python3
""" Tests for class BaseModel """

import unittest
from models.base_model import BaseModel
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
