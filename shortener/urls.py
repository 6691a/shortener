from django.urls import path
from rest_framework import routers
from django.urls import path, include

from .views import ShortenerListCreateView, ShortenerUpdateDeleteView
from .view_set import UrlViewSet

router = routers.DefaultRouter()
router.register(r'', UrlViewSet)

urlpatterns = [
    path('', ShortenerListCreateView.as_view()),
    path('<int:id>', ShortenerUpdateDeleteView.as_view()),
    path('url/', include(router.urls))
]
