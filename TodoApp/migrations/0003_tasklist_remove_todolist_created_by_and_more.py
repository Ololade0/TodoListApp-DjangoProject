# Generated by Django 4.1.5 on 2023-04-23 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TodoApp', '0002_remove_todoitem_due_date_remove_todoitem_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('memo', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dateCompleted', models.DateTimeField(null=True)),
                ('important', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]