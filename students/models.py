from django.db import models
from django.utils.text import slugify

# Create your models here.
class Parent(models.Model):
    father_name= models.CharField(max_length=100)
    father_ocupation= models.CharField(max_length=100)
    father_mobile= models.CharField(max_length=15)
    father_email= models.EmailField()
    mother_name= models.CharField(max_length=100)
    mother_ocupation= models.CharField(max_length=100)
    mother_mobile= models.CharField(max_length=15)
    mother_email= models.EmailField(max_length=100)
    present_address= models.TextField()
    permanent_address= models.TextField()

    def __str__(self):
        return f"{self.father_name} & {self.mother_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    student_class = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15)
    joining_date = models.DateField()
    religion = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    admission_number = models.CharField(max_length=20)
    image = models.ImageField(upload_to='student_images/', blank=True)
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name} {self.student_id}")
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.student_id}"