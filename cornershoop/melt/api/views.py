# Models
from cornershoop.melt.models import Melt, MeltSelectionUser

from cornershoop.melt.serializers import MeltCreateSerializer, MeltListSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class MeltViewSet(viewsets.ModelViewSet):
    queryset = Melt

    def get_serializer_class(self):
        if self.action in ("update", "partial_update", "create"):
            return MeltCreateSerializer
        elif self.action in ("list", "retrieve"):
            return MeltListSerializer

    def get_queryset(self):
        queryset = Melt.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MeltCreateSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


