# Generated by Django 5.0.1 on 2024-01-17 10:03

import django.core.validators
import django.db.models.deletion
import djrichtextfield.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/blog/')),
                ('data', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=40)),
                ('category_number', models.PositiveIntegerField()),
                ('category_type', models.CharField(choices=[('Design & Creative', 'Design & Creative'), ('Design & Development', 'Design & Development'), ('Sales & Marketing', 'Sales & Marketing'), ('Mobile Application', 'Mobile Application'), ('Construction', 'Construction'), ('Information Technology', 'Information Technology'), ('Real Estate', 'Real Estate'), ('Content Writer', 'Content Writer')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='How_It_Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='images/works/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="Telefon raqamini to'g'ri kiriting.")])),
                ('working_time', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Team_About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('img', models.ImageField(upload_to='images/team')),
                ('profession', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_resume', models.FileField(upload_to='file_resume/')),
            ],
        ),
        migrations.CreateModel(
            name='What_We_Are_Doing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', djrichtextfield.models.RichTextField()),
                ('img', models.ImageField(upload_to='images/team/')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.PositiveIntegerField()),
                ('job_description', models.TextField()),
                ('skills', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('job_about', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('phone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', message="Telefon raqamini to'g'ri kiriting.")])),
                ('email', models.EmailField(max_length=254)),
                ('company_web_site', models.URLField()),
                ('job_img', models.ImageField(upload_to='images/job_img/')),
                ('job_type', models.CharField(choices=[('full_time', 'full_time'), ('part_time', 'part_time'), ('remote', 'remote'), ('freelance', 'freelance')], max_length=25)),
                ('job_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
        ),
    ]
