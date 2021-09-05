from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from django.db.utils import IntegrityError


class TestManager(TestCase):

    def __check_user_created_with_valid_data(self, user, credentials):
        self.assertEqual(user.name, credentials['name'])
        self.assertEqual(user.email, credentials['email'])
        self.assertTrue(user.check_password(credentials['password']))

    def setUp(self):
        self.User = get_user_model()

    def test_create_user_successfull(self):
        """Test creating a new user with an email with successfull"""
        credentials = {
            'name': 'Huzaifa',
            'email': "huzaifacf@gmail.com",
            'password':  "12345"    
        }
        
        user = self.User.objects.create_user(**credentials)
        self.__check_user_created_with_valid_data(user, credentials)


    def test_user_email_normalized(self):
        """Tests user email is normalized before saving to db"""

        credentials = {
            'name': 'Huzaifa',
            'email': "huzaifacf@GMAIL.com",
            'password':  "12345"    
        }
        user = self.User.objects.create_user(**credentials)

        self.assertEqual(user.email, BaseUserManager.normalize_email(credentials['email']))

        
    def test_create_superuser_with_email(self):
        """Test that creating user creation with properties is_staff and is_superuser set to true is working"""

        credentials = {
            'name': 'Huzaifa',
            'email': "huzaifacf@gmail.com",
            'password':  "12345"    
        }
        user = self.User.objects.create_superuser(**credentials)
        self.__check_user_created_with_valid_data(user, credentials)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        

    def test_create_user_with_existing_email_fail(self):
        """Test creating multiple accounts with same email fails"""
        credentials = {
            'name': 'Huzaifa',
            'email': "huzaifacf@gmail.com",
            'password':  "12345"    
        }
        user1 = self.User.objects.create_user(**credentials)
        with self.assertRaises(IntegrityError):
            user2 = self.User.objects.create_user(**credentials)