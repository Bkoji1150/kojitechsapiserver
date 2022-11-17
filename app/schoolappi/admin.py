from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Course, Review, Teacher, Payment

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Teacher)
admin.site.register(Payment)