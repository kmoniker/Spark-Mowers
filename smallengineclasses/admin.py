from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)

class StudentInline(admin.TabularInline):
    model = Student

@admin.register(SmallEngineClass)
class SmallEngineClassAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'session_1_date', 'session_2_date', 'students_in_class')
    inlines = [StudentInline,]
