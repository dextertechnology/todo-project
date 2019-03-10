from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Tags(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField()
    date_tagged = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)

class TodoList(models.Model):
    IMP = 'imp'
    ND = 'nd'
    TYT = 'tyt'
    PRIORITY_CHOICES = (
        (IMP, 'Important'),
        (ND, 'Needed'),
        (TYT, 'Take your time'),
    )

    title = models.CharField(max_length=60)
    description = HTMLField()
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=TYT,
    )
    is_active = models.BooleanField(default=True)
    required_revision = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title