from django.test import TestCase
from django.contrib.auth.models import User


class UsersTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create 5 users
        users_count = 5
        for id in range(users_count):
            User.objects.create(
                username=f"user-{id}",
                password=f"password-{id}")
        user = User.objects.get(id=1)
        user.first_name = 'Vasya'
        user.save()

    def test_create_user(self):
        # range count from zero,  user-0
        user = User.objects.get(id=1)
        print(user)
        self.assertTrue(user.username == 'user-0')

    def test_update_user(self):
        user_firstname = User.objects.get(id=1).first_name
        self.assertTrue(user_firstname == 'Vasya')

    def test_delete_user(self):
        user = User.objects.get(id=3)
        user.delete()
        users_id = User.objects.all().values_list('id', flat=True)
        self.assertFalse(3 in users_id)

    def test_users_list(self):
        users = User.objects.all()
        self.assertEqual(len(users), 5)
