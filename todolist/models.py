from django.db import models
from tinymce.models import HTMLField

class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

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
    tags = models.ManyToManyField(Tags, through='TagsTodo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    completed_at = models.DateTimeField()
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        default=TYT,
    )
    is_active = models.BooleanField(default=False)
    required_revision = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class TagsTodo(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    date_tagged = models.DateTimeField(auto_now=True)