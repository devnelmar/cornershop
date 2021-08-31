from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from cornershoop.melt.models import Melt


class MeltCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melt
        fields = (
            "name",
            "date",
        )


class MeltListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Melt
        fields = (
            "id",
            "name",
            "date",
        )
