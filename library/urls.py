from django.conf.urls import url

from . import views

from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'books', views.BookViewSet)
urlpatterns = router.urls
