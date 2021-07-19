from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

JOB = {
    ('part time', 'part time'),
    ('full time', 'full time')
}


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_user')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    job_type = models.CharField(choices=JOB, max_length=50)
    vocancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    published_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('job:job_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Apply'
        verbose_name_plural = 'Applies'