from django.contrib import admin

# Register your models here.
from .models import Scores_Out,Course_model,lesson



admin.site.register(Scores_Out)
admin.site.register(Course_model)
admin.site.register(lesson)
