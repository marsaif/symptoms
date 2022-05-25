from django.contrib import admin

from app.models import Answer, Question, Symptom

# Register your models here.
admin.site.register(Symptom)
admin.site.register(Question)
admin.site.register(Answer)
