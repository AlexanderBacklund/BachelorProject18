# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class refpoint(models.Model):
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

class user_position(models.Model):
    u_id = models.AutoField(primary_key = True, unique = True)
    u_position = models.CharField(max_length = 64)
    u_username = models.CharField(max_length = 64)

    def __str__(self):
        return "User: "+(self.u_username)+" Position:"+self.u_position


# Create your models here.
