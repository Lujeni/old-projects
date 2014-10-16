# -*- coding: utf-8 -*-

# rest
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PaginationSerializer

# mac
from core.models import AuctionHouse


class AuctionHouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuctionHouse
        fields = [
            "name",
            "address",
            "zipcode",
            "country",
            "city",
            "longitude",
            "latitude",
            "ad1",
            "ad2"
        ]


class AuctionHousePagination(PaginationSerializer):

    class Meta:
        object_serializer_meta = AuctionHouseSerializer


class AuctionHouseViewSet(ModelViewSet):
    serializer_class = AuctionHouseSerializer
    paginate_by = 20
    queryset = AuctionHouse.objects.all()
