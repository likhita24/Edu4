
from django.test import TestCase
from .models import application

from django.contrib.auth.models import User

# Create your tests here.
class testusercreate(TestCase):
    def setUp(self):
        User.objects.create(username='edu4', password='12345678')

    def check_create_user(self):
        tuser = User.objects.get(username='edu4')
        self.assertEqual(tuser.username, 'edu4')

class applnTs(TestCase):
    def setUp(self):
        application.objects.create(Full_Name = 'edu4', Emailaddress='edu4@gmail.com', phone=754546332, Address='jodhpur', Country='india', University_or_College='IITJ', Year_of_study=2021, Transcript='one.pdf', Sop='two.pdf')

    def test(self):
        edu4 = application.objects.get(Full_Name='edu4')
        self.assertEqual(edu4.Full_Name, 'edu4')