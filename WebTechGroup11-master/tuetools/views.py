from django.shortcuts import render, get_object_or_404
from .models import Course, Document
from django.db.models import Q
from django.http import JsonResponse

# for authentication / registering users
from django.contrib.auth import authenticate, login, logout

from .forms import CourseForm, DocumentForm, UserForm

def index(request):
	courses = Course.objects.all()
	documents_result = Document.objects.all()
	query = request.GET.get("q")
	if query:
		courses = courses.filter(
			Q(course_name__icontains=query) |
			Q(course_code__icontains=query)
		).distinct()
		documents_result = documents_result.filter(
			Q(document_name__icontains=query)
		).distinct()
		return render(request, 'tuetools/index.html', {
			'courses': courses,
			'documents': documents_result,
		})
	else:
		return render(request, 'tuetools/index.html', {'courses': courses})


def courses_list(request):
    if not request.user.is_authenticated():
        return render(request, 'tuetools/login.html')
    else:
        courses = Course.objects.all()
        query = request.GET.get("q")
        if query:
            courses = courses.filter(
                Q(course_name__icontains=query) |
                Q(course_code__icontains=query)
            ).distinct()
            return render(request, 'tuetools/courses_list.html', {
                'courses': courses,
            })
        else: return render(request, 'tuetools/courses_list.html', {'courses': courses})


def documents_list(request):
    if not request.user.is_authenticated():
        return render(request, 'tuetools/login.html')
    else:
        courses = Course.objects.all()
        return render(request, 'tuetools/documents_list.html', {'courses': courses})


def make_current_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    try:
        if course.is_current_course:
            course.is_current_course = False
        else:
            course.is_current_course = True
        course.save()
    except (KeyError, Course.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                courses = Course.objects.all()
                return render(request, 'tuetools/index.html', {'courses': courses})
            else:
                return render(request, 'tuetools/login.html', {'error_message': 'Your account has been disabled.'})
        else:
            return render(request, 'tuetools/login.html', {'error_message': 'Invalid username or password. Please try again.'})
    return render(request, 'tuetools/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'tuetools/login.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                documents = Document.objects.filter(user=request.user)
                return render(request, 'tuetools/index.html', {'documents': documents})
    context = {
        "form": form,
    }
    return render(request, 'tuetools/registration.html', context)


def detail(request, course_id):
    if not request.user.is_authenticated():
        return render(request, 'tuetools/login.html')
    else:
        user = request.user
        course = get_object_or_404(Course, pk=course_id)
        return render(request, 'tuetools/detail.html', {'course': course, 'user': user})


def documents_uploaded(request):
    if not request.user.is_authenticated():
        return render(request, 'tuetools/login.html')
    else:
        user = request.user
        courses = Course.objects.all()
        return render(request, 'tuetools/documents_uploaded.html', {'courses': courses, 'user': user})


FILE_TYPES = ['doc', 'docx', 'pdf']

def upload_document(request, course_id):
    form = DocumentForm(request.POST or None, request.FILES or None)
    course = get_object_or_404(Course, pk=course_id)
    if form.is_valid():
        course_documents = course.document_set.all()
        for s in course_documents:
            if s.document_name == form.cleaned_data.get("document_name"):
                context = {
                    'course': course,
                    'form': form,
                    'error_message': 'There already exists a document with that name. Please use another name.',
                }
                return render(request, 'tuetools/upload_document.html', context)
        user = request.user
        document = form.save(commit=False)
        document.course = course
        document.document_file = request.FILES['document_file']
        document.user = user
        file_type = document.document_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in FILE_TYPES:
            context = {
                'course': course,
                'form': form,
                'error_message': 'Document must be a .doc, .docx or .pdf file.',
            }
            return render(request, 'tuetools/upload_document.html', context)

        document.save()
        return render(request, 'tuetools/detail.html', {'course': course})
    context = {
        'course': course,
        'form': form,
    }
    return render(request, 'tuetools/upload_document.html', context)


def add_course(request):
    if not request.user.is_authenticated():
        return render(request, 'tuetools/courses_list.html')
    else:
        form = CourseForm(request.POST or None)
        if form.is_valid():
            course = form.save(commit=False)
            course.course_name = form.cleaned_data['course_name']
            course.course_code = form.cleaned_data['course_code']
            course.save()
            return render(request, 'tuetools/courses_list.html')
        context = {
            "form": form,
        }
        return render(request, 'tuetools/add_course.html', context)


def delete_document(request, course_id, document_id):
    course = get_object_or_404(Course, pk=course_id)
    document = Document.objects.get(pk=document_id)
    document.delete()
    return render(request, 'tuetools/detail.html', {'course': course})
