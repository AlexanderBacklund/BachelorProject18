# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from show_position.models import Refpoint, User_position, Users_script
#from django.http import HttpResponse

# Create your views here.


def index(request):
    users = Users_script.objects.all()
    for u in users:
        u.position = u.users_name.all()[0].u_position

    funny_dict = {'user_positions': users,}
    return render(request, 'show_position/index.html', funny_dict)
