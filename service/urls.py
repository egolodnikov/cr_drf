from django.urls import path

from service.views import CsvView

urlpatterns = [
    path('csv/', CsvView.as_view()),
]
