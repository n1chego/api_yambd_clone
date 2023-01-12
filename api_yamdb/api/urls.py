from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import (
    CategoryViewSet, CommentViewSet,
    GenreViewSet, ReviewViewSet, TitleViewSet
)

from users.views import UserSignUpView, TokenView, UserViewSet

app_name = 'api'

router_v1 = SimpleRouter()
router_v1.register(
    'titles',
    TitleViewSet,
    basename='titles'
)
router_v1.register(
    'genres',
    GenreViewSet,
    basename='genres'
)
router_v1.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

router_v1.register('users', UserViewSet, basename='users')


auth_urls = [
    path(
        'auth/token/', TokenView.as_view(),
        name='token'
    ),
    path(
        'auth/signup/', UserSignUpView.as_view(),
        name='sign_up'
    ),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(auth_urls)),
]