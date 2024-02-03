from django.shortcuts import render, get_object_or_404
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
    team_content = Team_About.objects.all()
    how_works = How_It_Works.objects.all()[:4]
    blog_data = News.objects.all()
    what_we = What_We_Are_Doing.objects.all()
    if request.method == "POST":
        file_resume = request.POST.get('file_resume')
        data_resume = Upload_Resume(file_resume=file_resume)
        data_resume.save()
    context = {
        'how_works':how_works,
        'team_content':team_content,
        'blog_data':blog_data,
        'what_we':what_we,
    }
    return render(request, 'about.html', context)


def Blog(request):
    featured_jobs = Job.objects.all()

    if request.method == "POST":
        file_resume = request.POST.get('file_resume')
        data_resume = Upload_Resume(file_resume=file_resume)
        data_resume.save()
    context = {
        'featured_jobs':featured_jobs,
        
    }
    return render(request, 'blog.html', context)

def Contact_View(request):
    info = Info_Data.objects.last()
    info_img = Contact_Img.objects.last()
    context = {
        'info' : info,
        'info_img': info_img,
    }
    if request.method=="POST" : 
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        contact_form = Contact(message=message,name=name,email=email,subject=subject)
        contact_form.save()
    return render(request, 'contact.html', context)

def Elements(request):
    return render(request, 'elements.html')







def Job_Detail(request, pk):    
    data_detail = get_object_or_404(Job, pk=pk)
    return render(request, 'job_details.html', {'data_detail': data_detail})

def Job_Listing(request):
    featured_jobs = Job.objects.all()
    count_job = Job.objects.count()
    context = {
        'featured_jobs':featured_jobs, 
        'count_job':count_job,
    }
    return render(request, 'job_listing.html', context)

def Main(request):
    return render(request, 'main.html')

def Single_Blog(request, pk):
    blog_post = get_object_or_404(News, pk=pk)
    comment_data = Comment.objects.all()[:3]
    comment_soni = Comment.objects.count()
    if request.method == "POST":
        text = request.POST.get('text')
        email = request.POST.get('email')
        name = request.POST.get('name')
        web_url = request.POST.get('web_url')
        data_comment = Comment(text=text, email=email, name=name, web_url=web_url)
        data_comment.save()
    context = {
        'blog_post': blog_post,
        'comment_data':comment_data,
        'comment_soni':comment_soni
    }
    
    return render(request, 'single-blog.html', context)







