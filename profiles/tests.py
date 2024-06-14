from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_profile_update(self):
        profile = self.user.userprofile
        profile.bio = 'Updated bio'
        profile.save()
        self.assertEqual(profile.bio, 'Updated bio')


from django.test import TestCase

# Create your tests here.
