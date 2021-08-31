from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include, path

from cornershoop.users.api.views import UserViewSet
from cornershoop.users.api.views import LoginAPIView, RegisterAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("integrations/", include("cornershoop.integrations.urls", namespace="integrations")),
    path("melt/", include("cornershoop.melt.api_urls", namespace="melt")),
]
