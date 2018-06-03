from django.contrib import admin
from pols.models import Question, Choice, Comment
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Comment)