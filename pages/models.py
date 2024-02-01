from django.db import models
from django.core.validators import RegexValidator
from djrichtextfield.models import RichTextField


# Create your models here.

class Category(models.Model):
    category_type_select = (
        ('Design & Creative', 'Design & Creative'),
        ('Design & Development', 'Design & Development'),
        ('Sales & Marketing', 'Sales & Marketing'),
        ('Mobile Application', 'Mobile Application'),
        ('Construction', 'Construction'),
        ('Information Technology', 'Information Technology'),
        ('Real Estate', 'Real Estate'),
        ('Content Writer', 'Content Writer'),
    )
    category_name = models.CharField(max_length=40)
    
    category_type = models.CharField(choices=category_type_select, max_length=50)

    def __str__(self):
        return self.category_name

class Upload_Resume(models.Model):
    file_resume = models.FileField(upload_to='file_resume/')



class Job(models.Model):
    job_type_select = (
        ('full_time', 'full_time'),
        ('part_time', 'part_time'),
        ('remote', 'remote'),
        ('freelance', 'freelance'),
    )
    job_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    salary = models.PositiveIntegerField()
    job_description = models.TextField()
    skills = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    job_about = models.CharField(max_length=255)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamini to'g'ri kiriting.")])
    email = models.EmailField()
    company_web_site = models.URLField()
    job_img = models.ImageField(upload_to='images/job_img/')
    job_type = models.CharField(choices=job_type_select, max_length=25)

    def __str__(self):
        return self.job_name


class How_It_Works(models.Model):
    icon_select = (
        ('search', 'search'),
        ('apply', 'apply'),
        ('get', 'get'),
    )
    icon = models.CharField(choices=icon_select, max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

    
class Team_About(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='images/team')
    profession = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.profession}"
    


class What_We_Are_Doing(models.Model):
    title = models.CharField(max_length=60)
    description = RichTextField()
    img = models.ImageField(upload_to='images/team/')

    def __str__(self):
        return self.title[:25]
    
class News(models.Model):
    img = models.ImageField(upload_to='images/blog/')
    data = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title[:30]
    


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Contact_Img(models.Model):
    back_img = models.ImageField(upload_to='images/back_img/')
class Info_Data(models.Model):
    city_name = models.CharField(max_length=100) 
    street_name = models.CharField(max_length=100) 
    phone_number = models.CharField(max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Telefon raqamini to'g'ri kiriting.")])
    working_time = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.city_name











