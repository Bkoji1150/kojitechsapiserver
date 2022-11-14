from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
def upload_to(instance, filename):
    return 'images/api/{filename}'.format(filename=filename)    
              
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    description = models.CharField(null = True, max_length=150)
    website = models.URLField(null = True, max_length=100)
    created_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.course_name 
              
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student")
    gender = models.CharField(max_length=100, null = True)
    email = models.EmailField(max_length=100, unique = True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100, null = True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.first_name +  " | " +  self.email

    def full_address(self):
        return f'{self.Address_line_1} {self.Address_line_2}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    created_date = models.DateTimeField(auto_now_add=True) 
    email = models.EmailField(max_length=100, unique = True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.first_name  + "  |  " +  self.email
    
class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="review")
    review = models.TextField(max_length=500, blank=True)
    created_date = models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + "  |  " + self.review
