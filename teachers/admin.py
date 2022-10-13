from django.contrib import admin
from .models import Teacher


# bunların hepsi course modelinin admin paneline işler

@admin.register(Teacher)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",) # kurs mevcut mu değil mi onu gösterir
    search_fields = ('name',) # arama motoru 