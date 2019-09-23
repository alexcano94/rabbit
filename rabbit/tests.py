# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='John', email='lennon@thebeatles.com', password='johnpassword')

    def test_user_content(self):
        user = User.objects.get(id=1)
        expected_username = f'{user.username}'
        expected_email = f'{user.email}'
        self.assertEquals(expected_username, 'John')
        self.assertEqual(expected_email, 'lennon@thebeatles.com')
