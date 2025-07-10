from django.shortcuts import render
from django.http import HttpResponseRedirect

def register(req):
    return render(req, 'register.html')

def login(req):
    return render(req, 'login.html')

def logorreg(req):
    return render(req, 'logorreg.html')

def main(req):
    return HttpResponseRedirect('/logorreg')