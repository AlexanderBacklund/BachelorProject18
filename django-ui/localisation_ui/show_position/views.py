# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.


def index(request):
    funny_dict = {'msg': 'Albin kan allt',}
    return render(request, 'show_position/index.html', funny_dict)
