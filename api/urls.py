from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("projects/", views.ProjectList.as_view()),
    path("clients/", views.ClientList.as_view()),
    path("licenses/", views.LicenseList.as_view()),
    path("send-message/", views.MessageCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)