from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return HttpResponse('<h1>Home</h1>')

def Take_Response(request):
	return HttpResponse('<h1>Take-Response</h1>')
 