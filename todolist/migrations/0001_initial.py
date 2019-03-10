# Generated by Django 2.1.7 on 2019-03-10 10:21

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('date_tagged', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('imp', 'Important'), ('nd', 'Needed'), ('tyt', 'Take your time')], default='tyt', max_length=3)),
                ('is_active', models.BooleanField(default=True)),
                ('required_revision', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(to='todolist.Tags')),
            ],
        ),
    ]
