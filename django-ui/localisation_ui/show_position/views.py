# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from show_position.models import Refpoint, User_position, Users_script
from django.db.models import Q
#from django.http import HttpResponse

# Create your views here.


def index(request):
    users = Users_script.objects.all()
    query = request.GET.get('query')
    if query:
        users = users.filter(
        Q(u_fullname__icontains=query) |
        Q(u_username__icontains=query)
        ).distinct()
    for u in users:
        try:
            u.position = u.users_name.order_by('-u_datetime')[:1][0].u_position
        except IndexError:
            u.position = 'No current position'

    funny_dict = {'user_positions': users,}
    return render(request, 'show_position/index.html', funny_dict)

def layout(request):
    users = Users_script.objects.all()
    query = request.GET.get('query')
    if query:
        users = users.filter(
        Q(u_fullname__icontains=query) |
        Q(u_username__icontains=query)
        ).distinct()
    for u in users:
        try:
            u.position = u.users_name.order_by('-u_datetime')[:1][0].u_position
        except IndexError:
            u.position = 'No current position'

    funny_dict = {'user_positions': users,}
    return render(request, 'show_position/layout.html', funny_dict)
