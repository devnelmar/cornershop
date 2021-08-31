from django.urls import path

from cornershoop.melt.api.views import (
    MeltViewSet,
)

app_name = "melt"
urlpatterns = [
    path("", view=MeltViewSet.as_view({'post': 'create', 'get': 'list'}), name="melt"),
    path("<str:pk>/", view=MeltViewSet.as_view({'patch': 'update'}), name="melt-update"),
]
