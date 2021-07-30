from django.contrib import admin
from .models import Polls, Choice, Questions, Answers

admin.site.register(Polls)
admin.site.register(Choice)
admin.site.register(Questions)
admin.site.register(Answers)
