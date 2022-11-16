from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.urls import reverse
 
def upload_to_student(instance, filename):
    return 'images/api/student/photo/{filename}'.format(filename=filename)    

def upload_to(instance, filename):
    return 'images/api/teacher/photo/{filename}'.format(filename=filename)        

def upload_to(instance, filename):
    return 'images/api/payment/{filename}'.format(filename=filename)    


class Course(models.Model):
    GENDER_CHOICES = (
        ('Terraform', 'Terraform'),
        ('Docker', 'Docker'),
        ('Kubernetes', 'kubernetes'),
        ('Python', 'Python'),
    )
    course_name = models.CharField(max_length=10, choices=GENDER_CHOICES)
    description = models.CharField(null = True, max_length=150)
    website = models.URLField(null = True, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True) 
    avg_rating = models.FloatField(default=0)
    number_of_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name 
              
class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50, unique = True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, unique = True)
    address_line_1 = models.CharField(max_length=100, null = True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    image_url = models.ImageField(upload_to=upload_to_student, blank=True, null=True)
    student_balance = models.FloatField(max_length=100, default=10000) 
    number_of_payment = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name +  "    |  " +  self.email + "     |   " + str(self.phone_number)

    def full_address(self):
        return f'{self.Address_line_1} {self.Address_line_2}'


class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number    = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=100, unique = True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    created_date = models.DateTimeField(auto_now_add=True) 
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


    def __str__(self):
        return self.first_name  + "  |  " +  self.email + " | " + str(self.phone_number)
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="review")
    review = models.TextField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + "  |  "   +  self.review  + " |  " + str(self.review_user) 


class Payment(models.Model):
    id  = models.IntegerField(primary_key= True)
    payment_user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payment_info")
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    payment_id =  models.UUIDField(default=uuid.uuid4, editable=False, null=True)
    amount_paid = models.PositiveIntegerField(validators=[MinValueValidator(200), MaxValueValidator(500)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    receipt  = models.ImageField(upload_to=upload_to, blank=True, null=True)
   
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    
    def __iter__(self):
         return [field.value_to_string(self) for field in Student._meta.fields]    

    def __str__(self):
        return  str(self.amount_paid)  +  "  |  " + str(self.updated_at) + "  | " + str(self.payment_method)

