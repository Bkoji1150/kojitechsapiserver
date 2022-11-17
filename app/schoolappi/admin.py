
from django.contrib import admin
from .models import Student, Course, Review, Teacher, Payment

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['id', 'first_name', 'last_name', 'email', 'current_balance','total_amount_paid'] 
    list_filter = ['first_name', 'email']   

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['id', 'first_name', 'last_name', 'email','course_name', 'image_url'] 
    list_filter = ['first_name', 'email']  

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['course_name', 'description', 'avg_rating']
    list_display = ['course_name', 'description','avg_rating','website']
    list_filter = ['course_name']

class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['payment_id', 'payment_user', 'payment_method','amount_paid']
    list_display = ['payment_id', 'payment_user', 'update','payment_method','amount_paid'] 
    list_filter =['payment_user'] 
  
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['review_user', 'course', 'review','created_date']
    list_display = ['review_user', 'course', 'review','created_date','status']
    list_filter =['review_user']

    list_editable = ['status']    

admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Payment,PaymentAdmin)