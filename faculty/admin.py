from django.contrib import admin

from django.contrib import admin

from .models import Department, Home, Program, Teacher

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Program)
admin.site.register(Home)
