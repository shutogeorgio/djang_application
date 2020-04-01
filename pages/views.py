# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # args
    print(*args, **kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs): # args
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs): # args
    my_context = {
        "my_text": "This is about us" ,
        "my_number": 123,
        "my_list": [767, "Yes Man", "Nice Django", "About"]
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs): # args
    return render(request, "social.html", {})