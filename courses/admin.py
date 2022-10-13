from django.contrib import admin
from . models import Course,Category, Tag


# bunların hepsi course modelinin admin paneline işler

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "available","teacher") # kurs mevcut mu değil mi onu gösterir
    list_filter =("available",) # kursun yanındaki aktif mi değil mi onu filtreler
    search_fields = ('name', "description") # arama motoru 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    search_fields = ("name","description")
