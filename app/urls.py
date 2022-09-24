from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', ResumeViews.as_view(), name='contacts'),
    path('about/', AboutViews.as_view(), name='about'),
    path('work/', WorkViews.as_view(), name='work'),
    path('contact/', ContactViews.as_view(), name='contact'),
    path("accounts/profile/", ProfileView.as_view(), name="profile"),
    path("submit/", FormSubmited.as_view(), name="submit"),


]
