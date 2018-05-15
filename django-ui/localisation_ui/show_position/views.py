# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from show_position.models import Refpoint, User_position, Users_script
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
#from django.http import HttpResponse

# Create your views here.


@csrf_protect
def index(request):
    users = User.objects.all().filter(is_staff=0)
    for u in users:
        u.position = u.User.order_by('-u_datetime')[:1][0].u_position
        funny_dict = {'user_positions': users}
    #print users.0.users_script.show_position
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        user = request.POST.get("info", "")
        decs = request.POST.get("decs", "")
        
        u = User.objects.get(username=user)
        u.users_script.u_show_position = decs
        u.save()
        # check whether it's valid:
        render(request, 'show_position/index.html', funny_dict)


    query = request.GET.get('query')
    if query:
        users = users.filter(
        Q(u_fullname__icontains=query) |
        Q(u_username__icontains=query)
        ).distinct()
    return render(request, 'show_position/index.html', funny_dict)

def layout(request):
    users = Users_script.objects.all()
    query = request.GET.get('query')
    if query:
        users = users.filter(
        Q(u_fullname__icontains=query) |
        Q(u_username__icontains=query)
        ).distinct()
