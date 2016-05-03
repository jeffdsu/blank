from django.conf.urls import url, patterns, include

from . import views

from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'mediums', views.MediumViewSet)
router.register(r'insights', views.InsightViewSet)
router.register(r'admin/words-to-ignore', views.WordsToIgnoreViewSet)


mediums_router = routers.NestedSimpleRouter(router, r'mediums', lookup='books', trailing_slash=False)

books_router = routers.NestedSimpleRouter(router, r'books', lookup='books', trailing_slash=False)
books_router.register(r'checkouts', views.CheckoutViewSet, base_name='books-checkouts')
books_router.register(r'insights', views.BookInsightViewSet, base_name='books-insights')
books_router.register(r'keywords', views.BookKeywordsViewSet, base_name='books-keywords')

insights_router = routers.NestedSimpleRouter(router, r'insights', lookup='insights', trailing_slash=False)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(mediums_router.urls)),
    url(r'^', include(books_router.urls)),
    url(r'^', include(insights_router.urls)),
)
