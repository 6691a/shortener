from django.urls import path


from .views import DateStatView
urlpatterns = [
    path('', DateStatView.as_view()),
]
