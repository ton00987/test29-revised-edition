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
