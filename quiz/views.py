from django.shortcuts import render, redirect
from quiz.models import Quiz

def home_page(request):
    return render(request, 'home.html')

def add_quiz(request):
    if request.method == 'POST':
        Quiz.objects.create(ques=request.POST['quiz'], ans=request.POST['ans'])
        return redirect('/addquiz/success')

    return render(request, 'addquiz.html')

def success(request):
    return render(request, 'success.html')

def answer(request):
    # To arrange in descending order. It means your quiz has just been added  will appear at the top.
    quizs = Quiz.objects.all().order_by('-id')
    return render(request, 'answer.html', {'quizs': quizs})
