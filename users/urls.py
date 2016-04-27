from django.conf.urls import url, patterns, include

from . import views

from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', views.UserViewSet)

urlpatterns = patterns('',
    #url(r'', include(router.urls))
)
