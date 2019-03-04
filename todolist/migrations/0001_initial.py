# Generated by Django 2.1.5 on 2019-03-04 21:47

from django.db import migrations, models
import django.db.models.deletion
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
            ],
        ),
        migrations.CreateModel(
            name='TagsTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_tagged', models.DateTimeField(auto_now=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.Tags')),
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
                ('completed_at', models.DateTimeField()),
                ('priority', models.CharField(choices=[('imp', 'Important'), ('nd', 'Needed'), ('tyt', 'Take your time')], default='tyt', max_length=3)),
                ('is_active', models.BooleanField(default=False)),
                ('required_revision', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(through='todolist.TagsTodo', to='todolist.Tags')),
            ],
        ),
        migrations.AddField(
            model_name='tagstodo',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.TodoList'),
        ),
    ]
