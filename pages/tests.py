from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class HomePageTests(SimpleTestCase):
	def test_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_name_url(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)

	def test_template_use(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

	username = 'user1'
	email = 'useremail'

	def test_status_code(self):
		response = self.client.get('/users/signup/')
		self.assertEqual(response.status_code, 200)

	def test_name_url(self):
		response = self.client.get(reverse('signup'))
		self.assertEqual(response.status_code, 200)

	def test_template_use(self):
		response = self.client.get(reverse('signup'))
		self.assertTemplateUsed(response, 'signup.html')

	def test_signup_form(self):
		new_user = get_user_model().objects.create_user(self.username, self.email)
		self.assertEqual(get_user_model().objects.all().count(), 1)
		self.assertEqual(get_user_model().objects.all()[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()[0].email, self.email)	
