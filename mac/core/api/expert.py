# -*- coding: utf-8 -*-

# rest
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PaginationSerializer

# mac
from core.models import Expert


class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email'
        ]


class ExpertPagination(PaginationSerializer):

    class Meta:
        object_serializer_meta = ExpertSerializer


class ExpertViewSet(ModelViewSet):
    serializer_class = ExpertSerializer
    paginate_by = 20
    queryset = Expert.objects.all()
