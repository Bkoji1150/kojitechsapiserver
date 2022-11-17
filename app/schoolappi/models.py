from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import uuid
 
def upload_to(instance, filename):
    return 'images/api/{filename}'.format(filename=filename)    
              
class Course(models.Model):
    course_name = models.CharField(max_length=100, unique= True)
    description = models.CharField(null =True,  blank= True, max_length=150)
    website = models.URLField(null=True, blank= True, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True, blank=True) 
    avg_rating = models.FloatField(default=0)
    number_of_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name 

class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()  

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = NameField(max_length=100)
    middle_name = NameField(max_length=100, null =True,  blank= True)
    last_name =  NameField(max_length=100)
    nick_name =  NameField(max_length=100, null =True,  blank= True)
    phone_number = models.CharField(max_length=50, unique = True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.CharField(null =True,  blank= True, max_length=150)
    email = models.EmailField(max_length=100, unique = True)
    address_line_1 = models.CharField(max_length=100, blank=True,)
    address_line_2 = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    current_balance = models.FloatField(default=0)
    total_amount_paid = models.IntegerField(default=0)
    number_of_payment = models.IntegerField(default=0)

    def __iter__(self):
        return [field.value_to_string(self) for field in Course._meta.fields]    

    def __str__(self):
        return  self.email 

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
    description = models.CharField(null =True,  blank= True, max_length=150)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number    = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=100, unique = True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="teacher")
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
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + "  |  "   +  self.review  + " |  " + str(self.review_user) 

class Payment(models.Model):
    payment_user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="confirm_user")
    amount_paid = models.PositiveIntegerField(validators=[MinValueValidator(200), MaxValueValidator(1000)])
    description = models.CharField(max_length=200)
    update = models.DateTimeField(auto_now=True)
    payment_id =  models.UUIDField(default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    receipt  = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return str(self.amount_paid) + " | " + str(self.payment_user) 

