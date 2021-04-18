from django.db import models
from colorfield.fields import ColorField
from django.core.validators import FileExtensionValidator

# Create your models here.
class Site(models.Model):
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    urlName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.TextField()
    company = models.TextField()
    periode = models.TextField()
    city = models.TextField()
    description = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name='jobs')

    def __str__(self):
        return self.title + ' - ' + self.company

class Training(models.Model):
    title = models.TextField()
    place = models.TextField()
    date = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name='trainings')

    def __str__(self):
        return self.title

class Subject(models.Model):
    LEVEL_CHOICES = [
        (1, 'Main'),
        (2, 'Secondary'),
    ]
    level = models.IntegerField(default=1, choices=LEVEL_CHOICES)
    title = models.TextField()
    training = models.ForeignKey(Training, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.title

class Skillset(models.Model):
    domain = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name='skillsets')

    def __str__(self):
        return self.domain

class Skill(models.Model):
    title = models.TextField()
    skillset = models.ForeignKey(Skillset, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.TextField()
    client = models.TextField()
    summary = models.TextField()
    mission = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.PROTECT, related_name='projects')

    def __str__(self):
        return self.title

class Technology(models.Model):
    title = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='techs')

    def __str__(self):
        return self.title

class Info(models.Model):
    name = models.TextField()
    jobTitle = models.TextField()
    location = models.TextField()
    mail = models.TextField()
    phone = models.TextField()
    github = models.TextField(null=True, blank=True)
    gitlab = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
    site = models.OneToOneField(Site, on_delete=models.PROTECT, related_name='infos')

class SiteSettings(models.Model):
    FONT_CHOICES = [
        ('Lato', 'Lato (sans serif)'),
        ('Oswald', 'Oswald (sans serif)'),
        ('Ubuntu', 'Ubuntu (sans serif)'),
        ('Roboto', 'Roboto (sans serif)'),
        ('Arial', 'Arial (sans serif)'),
        ('Verdana', 'Verdana (sans serif)'),
        ('Times New Roman', 'Times New Roman (serif)'),
        ('Georgia ', 'Georgia  (serif)'),
        ('Courier New', 'Courier New (monospace)'),
        ('Brush Script MT', 'Brush Script MT (cursive)'),
    ]
    primary_background_color = ColorField(default='#FF0000')
    primary_font_color = ColorField(default='#FF0000')
    secondary_background_color = ColorField(default='#FF0000')
    secondary_font_color = ColorField(default='#FF0000')
    ternary_color = ColorField(default='#FF0000')
    nav_background_color = ColorField(default='#FF0000')
    nav_items_color = ColorField(default='#FF0000')
    primary_font = models.CharField(max_length=255, choices=FONT_CHOICES, default='Ubuntu')
    secondary_font = models.CharField(max_length=255, choices=FONT_CHOICES, default='Ubuntu')
    ternary_font = models.CharField(max_length=255, choices=FONT_CHOICES, default='Ubuntu')
    site = models.OneToOneField(Site, on_delete=models.PROTECT, related_name='siteSettings')

    def __str__(self):
        return self.siteTitle
