import requests
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from cornershoop.integrations.utils.client_slack import send_order_to_slack
from rest_framework.response import Response
from rest_framework import status
from cornershoop.melt.models import MeltSelectionUser, Melt


@csrf_exempt
def slack_app(request):
    data = request.POST['payload']
    json_data = json.loads(data)
    value = list(json_data['state']['values'].items())[1]
    description = list(value[1].items())[0][1]['value']
    melt = Melt.objects.filter(name=json_data['state']['values']['actions1']['select_2']['selected_option']['value']).first()
    MeltSelectionUser.objects.create(
        username=json_data['user']['name'],
        description=description,
        melt=melt,
    )
    response_url = json_data["response_url"]
    message = {
        "text": "Ya asignamos tu orden!, sera entregada en un par de minutos!"
    }
    res = requests.post(response_url, json=message)

    assert res.status_code == 200


@api_view(('GET',))
def send_day_order(request):
    send_order_to_slack()
    return Response(status=status.HTTP_200_OK)
