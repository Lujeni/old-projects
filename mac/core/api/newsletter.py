# -*- coding: utf-8 -*-

# rest
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PaginationSerializer

# mac
from core.models import NewsletterEmail


class NewsletterEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsletterEmail
        fields = [
            'email'
        ]


class NewsletterEmailPagination(PaginationSerializer):

    class Meta:
        object_serializer_meta = NewsletterEmailSerializer


class NewsletterEmailViewSet(ModelViewSet):
    serializer_class = NewsletterEmailSerializer
    paginate_by = 100
    queryset = NewsletterEmail.objects.filter(active=True)
