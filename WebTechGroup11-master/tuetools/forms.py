from django import forms
from django.contrib.auth.models import User

from .models import Course, Document


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['course_name', 'course_code']


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['document_name', 'document_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
