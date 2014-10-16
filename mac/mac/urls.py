# -*- coding: utf-8 -*-

# django
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

# rest
from rest_framework.routers import DefaultRouter

# mac
from core.views import HomeView
from core.api import (
    AuctionHouseViewSet, ExpertViewSet, NewsletterEmailViewSet
)

admin.autodiscover()

router = DefaultRouter()
router.register(r'auctionhouse', AuctionHouseViewSet)
router.register(r'expert', ExpertViewSet)
router.register(r'newsletter', NewsletterEmailViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    (r'^', HomeView.as_view()),
)
