from django.shortcuts import render
from .models import *
# Create your views here.


def Home(request):
    blog_data = News.objects.all()
    category_data = Category.objects.all()
    count_job = Job.objects.values('job_category').distinct().count()
    how_works = How_It_Works.objects.all()[:4]
    featured_jobs = Job.objects.all()
    team_content = Team_About.objects.all()
    what_we = What_We_Are_Doing.objects.all()
    


    if request.method == "POST":
        file_resume = request.POST.get('file_resume')
        data_resume = Upload_Resume(file_resume=file_resume)
        data_resume.save()
    context = {
        'category_data': category_data,
        'count_job':count_job,
        'how_works':how_works,
        'featured_jobs':featured_jobs,
        'team_content':team_content,
        'what_we':what_we,
        'blog_data':blog_data
        
    }
    return render(request, 'index.html', context)


def About(request):
    return render(request, 'about.html')


def Blog(request):
    return render(request, 'blog.html')

def Contact(request):
    return render(request, 'contact.html')

def Elements(request):
    return render(request, 'elements.html')

def Job_Detail(request):
    return render(request, 'job_detail.html')

def Job_Listing(request):
    return render(request, 'job_listing.html')

def Main(request):
    return render(request, 'main.html')

def Single_Blog(request):
    return render(request, 'single-blog.html')







