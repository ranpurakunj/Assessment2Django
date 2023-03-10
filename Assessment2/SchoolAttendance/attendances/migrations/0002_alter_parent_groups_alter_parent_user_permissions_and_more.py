# Generated by Django 4.1.5 on 2023-01-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('attendances', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='parent_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='parent_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='student',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='student_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='student_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='teacher_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='teacher_permissions', to='auth.permission'),
        ),
    ]
