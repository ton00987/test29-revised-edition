from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class AddQuizPageTest(TestCase):

    def test_uses_add_quiz_template(self):
        response = self.client.get('/addquiz')
        self.assertTemplateUsed(response, 'addquiz.html')
