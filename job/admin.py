from django.contrib import admin

from .models import Job , Category , Apply

class JobAdmin(admin.ModelAdmin):
    list_display  = ('user','title', 'job_type', 'salary', 'experince', 'published_at')
    list_filter = ('job_type', 'salary', 'experince')
admin.site.register(Job, JobAdmin)


admin.site.register(Category)
class ApplyAdmin(admin.ModelAdmin):
    list_display  = ('job','name', 'email', 'webiste', 'created_at')
    list_filter = ('job', 'name')

admin.site.register(Apply, ApplyAdmin)
