# Slack
from slack_sdk.webhook import WebhookClient
from cornershoop.melt.models import Melt

from datetime import date
import calendar


def send_order_to_slack():
    url = 'https://hooks.slack.com/services/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'
    my_date = date.today()
    day_of_the_week = calendar.day_name[my_date.weekday()]
    melts = Melt.objects.filter(date=str(day_of_the_week).upper())
    webhook = WebhookClient(url)
    block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Orden del dia"
            }
        },
        {
            "type": "actions",
            "block_id": "actions1",
            "elements": [
                {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Que deseas comer hoy?"
                    },
                    "action_id": "select_2",
                    "options": []
                },
            ]
        },
        {
            "type": "input",
            "element": {
                "type": "plain_text_input"
            },
            "label": {
                "type": "plain_text",
                "text": "Recomendaciones",
                "emoji": True
            },
            "dispatch_action": False,

        }
    ]
    options = []

    for melt in melts:
        empty_json = {}
        text = {}
        text['type'] = "plain_text"
        text['text'] = melt.name

        empty_json['text'] = text
        empty_json['value'] = melt.name
        options.append(empty_json)
    block[1]['elements'][0]['options'] = options
    blocks = block

    response = webhook.send(
        text="Orden del dia",
        blocks=blocks
    )
    assert response.status_code == 200
    assert response.body == "ok"
