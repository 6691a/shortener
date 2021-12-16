from django.urls import path

from .views import ShortenerListCreateView, ShortenerUpdateDeleteView
urlpatterns = [
    path('', ShortenerListCreateView.as_view()),
    path('<int:id>', ShortenerUpdateDeleteView.as_view()),

]
