from django.conf.urls import url, patterns, include

from . import views

from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

domains_router = routers.NestedSimpleRouter(router, r'books', lookup='books', trailing_slash=False)
domains_router.register(r'checkouts', views.CheckoutViewSet, base_name='books-checkouts')
domains_router.register(r'lessons-learned', views.InsightViewSet, base_name='books-lessons-learned')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(domains_router.urls)),
)
