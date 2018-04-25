# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from show_position.models import refpoint, user_position
#from django.http import HttpResponse

# Create your views here.


def index(request):
    users = user_position.objects.all()
    funny_dict = {'user_positions': users,}
    return render(request, 'show_position/index.html', funny_dict)
