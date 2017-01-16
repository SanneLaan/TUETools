from django.db import models
from django.contrib.auth.models import Permission, User

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    is_current_course = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name + ' (' + self.course_code + ')'

class Document(models.Model):
    user = models.ForeignKey(User, default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    document_file = models.FileField(default='')
    document_name = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.document_name
