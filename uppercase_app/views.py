from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):#Main page responder
    return HttpResponse('<h1>UpperCase Convertor Application</h1>')
