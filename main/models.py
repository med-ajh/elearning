from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    # Ajoutez des related_name personnalisés pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions'
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    courses = models.ManyToManyField('Course', related_name='profiles')

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_teacher': True})

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade = models.FloatField()
    comments = models.TextField(blank=True)

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    subject = models.CharField(max_length=100)
    level = models.IntegerField(choices=[(4, '4e année'), (5, '5e année')])
