# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.db import models

# Create your models here.
from django.db import models

from django.utils import timezone

class user(models.Model):
    index = models.IntegerField()
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    type=models.CharField(max_length=10)
    level = models.IntegerField()
    create_date = models.DateTimeField(default=django.utils.timezone.now)
    last_login_time = models.DateTimeField()
