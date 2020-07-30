from django.shortcuts import render
from django.http import HttpResponse
import random

def hello(request):

    text = str(random.randint(1,10000))
    return HttpResponse(text)

    

    
   
