from django.contrib import admin
from .models import *

# Register your models here.

class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 3

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 3

class TechnologyInline(admin.StackedInline):
   model = Technology
   extra = 3

class JobAdmin(admin.ModelAdmin):
    model = Job

class TrainingAdmin(admin.ModelAdmin):
    model = Training
    inlines = [SubjectInline]

class SkillsetAdmin(admin.ModelAdmin):
    model = Skillset
    inlines = [SkillInline]

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [TechnologyInline]

admin.site.register(Site)
admin.site.register(Job, JobAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Skillset, SkillsetAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Info)
admin.site.register(SiteSettings)
