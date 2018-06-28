from django.test import TestCase

from quiz.models import Quiz

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class AddQuizPageTest(TestCase):

    def test_uses_add_quiz_template(self):
        response = self.client.get('/addquiz')
        self.assertTemplateUsed(response, 'addquiz.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/addquiz', data={'quiz': 'A new quiz', 'ans': False})

        self.assertEqual(Quiz.objects.count(), 1)
        new_quiz = Quiz.objects.first()
        self.assertEqual(new_quiz.ques, 'A new quiz')
        self.assertEqual(new_quiz.ans, False)

    def test_redirects_after_POST(self):
        response = self.client.post('/addquiz', data={'quiz': 'A new quiz', 'ans': False})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/addquiz/success')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/addquiz')
        self.assertEqual(Quiz.objects.count(), 0)

class QuizModelTest(TestCase):

    def test_saving_and_retrieving_quizs(self):
        first_quiz = Quiz()
        first_quiz.ques = 'The first quiz 1+1=2'
        first_quiz.ans = True
        first_quiz.save()

        second_quiz = Quiz()
        second_quiz.ques = 'The second quiz 2+2=3'
        second_quiz.ans = False
        second_quiz.save()

        saved_quizs = Quiz.objects.all()
        self.assertEqual(saved_quizs.count(), 2)

        first_saved_quiz = saved_quizs[0]
        second_saved_quiz = saved_quizs[1]
        self.assertEqual(first_saved_quiz.ques, 'The first quiz 1+1=2')
        self.assertEqual(first_saved_quiz.ans, True)
        self.assertEqual(second_saved_quiz.ques, 'The second quiz 2+2=3')
        self.assertEqual(second_saved_quiz.ans, False)
