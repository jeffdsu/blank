from django.conf.urls import url, patterns, include

from inspiration import views

from rest_framework_nested import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'media/(?P<type>\w+)', views.MediumViewSet)
router.register(r'contributors', views.ContributorViewSet)
router.register(r'medium-types', views.MediumTypeViewSet)
router.register(r'insights', views.InsightViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'admin/words-to-ignore', views.WordsToIgnoreViewSet)
router.register(r'admin/insights', views.admin.AdminInsightViewSet)



medium_types_router = routers.NestedSimpleRouter(router, r'medium-types', lookup='media', trailing_slash=False)

books_router = routers.NestedSimpleRouter(router, r'media/(?P<type>\w+)', lookup='media', trailing_slash=False)
books_router.register(r'checkouts', views.CheckoutViewSet, base_name='media-checkouts')
books_router.register(r'insights', views.MediumInsightViewSet, base_name='media-insights')
books_router.register(r'keywords', views.KeywordsViewSet, base_name='media-keywords')

insights_router = routers.NestedSimpleRouter(router, r'insights', lookup='insights', trailing_slash=False)

contributor_router = routers.NestedSimpleRouter(router, r'contributors', lookup='contributors', trailing_slash=False)
contributor_router.register(r'works', views.ContributorWorksViewSet, base_name='contributors-works')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='users', trailing_slash=False)
users_router.register(r'insights', views.UserInsightsViewSet, base_name='users-insights')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include(medium_types_router.urls)),
    url(r'^', include(books_router.urls)),
    url(r'^', include(insights_router.urls)),
    url(r'^', include(contributor_router.urls)),
    url(r'^', include(users_router.urls)),
)

