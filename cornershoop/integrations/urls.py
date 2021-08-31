from django.urls import path

from cornershoop.integrations.api.views import (
    slack_app,
    send_day_order
)

app_name = "integrations"
urlpatterns = [
    path("slack/", view=slack_app, name="slack-app"),
    path("order-day/", view=send_day_order, name="slack-order"),
]
