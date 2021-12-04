from django.urls import path

from .views import ShortenerlistCreateView, ShortenerUpdateDeleteView
urlpatterns = [
    path('', ShortenerlistCreateView.as_view()),
    path('<int:id>', ShortenerUpdateDeleteView.as_view()),

]
