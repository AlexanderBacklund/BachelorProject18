# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Refpoint(models.Model):
    r_id = models.AutoField(primary_key = True, unique = True)
    r_position = models.CharField(max_length = 64)
    r_addr1 = models.CharField(max_length = 64)
    r_addr2 = models.CharField(max_length = 64)
    r_addr3 = models.CharField(max_length = 64)
    r_rssi1 = models.CharField(max_length = 64)
    r_rssi2 = models.CharField(max_length = 64)
    r_rssi3 = models.CharField(max_length = 64)

    def __str__(self):
        return "Position: "+(self.r_position)+" Ref_id:"+str(self.r_id)

class Users_script(models.Model):
    u_id = models.AutoField(primary_key = True, unique = True)
    u_username = models.CharField(max_length = 64)
    u_fullname = models.CharField(max_length = 64)
    u_show_position = models.BooleanField(default=True)

    def __str__(self):
        return "UserID: "+str(self.u_id)+" Username:"+(self.u_username) + " Show position: " +str(self.u_show_position)
class User_position(models.Model):
    u_id = models.ForeignKey(Users_script, related_name = "users_name")
    u_position = models.CharField(max_length = 64)
    u_datetime = models.DateTimeField()

    def __str__(self):
        return "User: "+self.u_id.u_username+" Position:"+(self.u_position)+" Datum:"+str(self.u_datetime)



# Create your models here.
