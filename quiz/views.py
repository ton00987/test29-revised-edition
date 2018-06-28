from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def add_quiz(request):
    return render(request, 'addquiz.html')
