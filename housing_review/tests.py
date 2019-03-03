from django.test import TestCase

import datetime
import unittest

from django.test import TestCase
from django.utils import timezone

from .models import User, Review

class LoginTest(TestCase):
    def testuserPass(self):
        coocoo = User(first_name='John', last_name='Smith', email='test@test.edu')
        self.assertEqual(coocoo.first_name, 'John')
    def testuserFail(self):
        coco = User(first_name='John', last_name='Smith', email='test@test.edu')
        self.assertNotEqual(coco.first_name, 'Jo')

class ReviewTest(TestCase):
    def testgreatlyrated(self):
        goodHomePass = Review(stars = 5)
        self.assertGreaterEqual(goodHomePass.stars, 4)
    def testLowRated(self):
        badHome = Review(stars = 2)
        self.assertLessEqual(badHome.stars, 2)
