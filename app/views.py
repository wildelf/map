from django.shortcuts import render

# Create your views here.

def run(req):
    return render(req,'tests.html')
