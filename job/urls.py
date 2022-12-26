from django.urls import path

from job.views import AddJobView

urlpatterns = [
    path('add/', AddJobView.as_view(), name='add-job')
]
