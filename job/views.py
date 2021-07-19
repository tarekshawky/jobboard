from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import ApplyForm, JObForm
from .models import Job
from .filters import JobFilter

def job_list(request):
    job_list = Job.objects.all()

    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs
    paginator = Paginator(job_list, 25)
    page_number = request.GET.get('page')
    job_list = paginator.get_page(page_number)
    context = {'job_list' : job_list , 'myfilter' : myfilter}
    return render(request,'job/job_list.html',context)

@login_required
def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            messages.success(request, 'Send successful')
            return redirect ("job:job_list")
        
    else:
        form = ApplyForm()
    context = {'job_detail':  job_detail, 'form':form}
    return render(request, 'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JObForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            messages.success(request, 'Add Job successfully')
            return redirect(reverse('jobs:job_list'))
    else:
        form = JObForm()

    return render(request,'job/add_job.html',{'form':form})