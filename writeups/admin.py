from django.contrib import admin
from writeups.models import Writeup
from writeups.models import Comment
from writeups.models import SessionSummary

# Register your models here.

admin.site.register(Writeup)
admin.site.register(Comment)
admin.site.register(SessionSummary)
