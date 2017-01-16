from django.conf.urls import url
from . import views

app_name = 'tuetools'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^documents_list$', views.documents_list, name='documents_list'),
    url(r'^courses_list$', views.courses_list, name='courses_list'),
    url(r'^add_course', views.add_course, name='add_course'),
    url(r'^documents_uploaded$', views.documents_uploaded, name='documents_uploaded'),
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<course_id>[0-9]+)/upload_document/$', views.upload_document, name='upload_document'),
    url(r'^(?P<course_id>[0-9]+)/delete_document/(?P<document_id>[0-9]+)/$', views.delete_document, name='delete_document'),
    url(r'^(?P<course_id>[0-9]+)/make_current_course/$', views.make_current_course, name='make_current_course'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
