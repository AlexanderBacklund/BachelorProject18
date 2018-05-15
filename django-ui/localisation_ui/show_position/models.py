# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    u_user = models.OneToOneField(User, on_delete=models.CASCADE)
    u_show_position = models.BooleanField(default=True)

    def __str__(self):
        return " Username:"+(self.u_user.username) + " Show position: " +str(self.u_show_position)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Users_script.objects.create(u_user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.users_script.save()


class User_position(models.Model):
    u_id = models.ForeignKey(User, related_name="User")
    u_position = models.CharField(max_length = 64, default="No Current Position")
    u_datetime = models.DateTimeField()

    def __str__(self):
        return "User: "+self.u_id.username+" Position:"+(self.u_position)+" Datum:"+str(self.u_datetime)



# Create your models here.
