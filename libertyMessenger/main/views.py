from django.shortcuts import render
from django.http import HttpResponseRedirect

def registerview(req):
    return render(req, 'register.html')

def loginview(req):
    return render(req, 'login.html')

def logorreg(req):
    return render(req, 'logorreg.html')

def main(req):
    return render(req, 'index.html')


def register(req):
    username = req.POST.get()