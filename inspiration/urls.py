from django.conf.urls import url, patterns, include

from . import views

from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'mediums', views.MediumViewSet)


mediums_router = routers.NestedSimpleRouter(router, r'mediums', lookup='books', trailing_slash=False)

books_router = routers.NestedSimpleRouter(router, r'books', lookup='books', trailing_slash=False)
books_router.register(r'checkouts', views.CheckoutViewSet, base_name='books-checkouts')
books_router.register(r'insights', views.InsightViewSet, base_name='books-insights')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(mediums_router.urls)),
    url(r'^', include(books_router.urls)),
)
