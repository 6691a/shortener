from django.urls import path

from .views import DateStatView, BrowserStatView

urlpatterns = [
    path('date', DateStatView.as_view()),
    path('browser', BrowserStatView.as_view()),

]
