from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):

	return render(request, "generator/home.html")

def password(request):

	characters = list('abcdefghijklmnopqrstuvwxyz')
	thepassword = ''

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('specialchar'):
		characters.extend(list('!@#$%^&*'))

	if request.GET.get('number'):
		characters.extend(list('1234567890'))

	length = int(request.GET.get('length'))

	for i in range(length):

		thepassword+=random.choice(characters)

	return render(request, "generator/password.html", {'password':thepassword})


# def about(request):
# 	gibberish = "This is a password generator website created Tomas Tecle using the django framework!"

# 	return render(request, "generator/about.html", {'gibber': gibberish})
