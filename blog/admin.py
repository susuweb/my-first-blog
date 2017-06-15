# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys;

reload(sys);
sys.setdefaultencoding("utf8")

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
