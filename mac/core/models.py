# -*- coding: utf-8 -*-

# django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# django-phonenumber-field
from phonenumber_field.modelfields import PhoneNumberField


class BasePlace(models.Model):

    name = models.CharField(max_length=50, verbose_name=_(u"Name"))

    address = models.CharField(max_length=1028, verbose_name=_(u"Address"))
    zipcode = models.CharField(max_length=12, verbose_name=_(u"Zip code"))
    country = models.ForeignKey('diplomat.ISOCountry', null=True)
    city = models.CharField(max_length=128, verbose_name=_(u"City"))

    longitude = models.FloatField(blank=True, verbose_name=_(u"Longitude"))
    latitude = models.FloatField(blank=True, verbose_name=_(u"Latitude"))

    ad1 = models.CharField(max_length=64, blank=True, verbose_name=_(u"Administrative level 1"))
    ad2 = models.CharField(max_length=64, blank=True, verbose_name=_(u"Administrative level 2"))

    class Meta:
        abstract = True


class AuctionHouse(BasePlace):

    contact_phone_number = PhoneNumberField(verbose_name=_(u"Contact phone number"))

    def __unicode__(self):
        return u"{} from {}".format(self.name, self.city)


class EventPlace(BasePlace):
    pass


class Expert(models.Model):

    first_name = models.CharField(max_length=30, verbose_name=_(u"First name"))
    last_name = models.CharField(max_length=30, verbose_name=_(u"Last name"))
    phone_number = PhoneNumberField(verbose_name=_(u"Phone number"))
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='expert', blank=True)

    def __unicode__(self):
        return u"{} - {}".format(self.first_name, self.last_name)


class Theme(models.Model):

    name = models.CharField(unique=True, max_length=32, verbose_name=_("Theme"))

    def __unicode__(self):
        return u'{}: {}'.format(_(u"Sub theme"), self.name)


class Event(models.Model):

    EVENT_THEMES = (
        ('africa', _('Africa')),
        ('asian', _('Asian'))
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, verbose_name=_(u"Name"))
    description = models.CharField(max_length=500, verbose_name=_(u"Description"))
    short_description = models.CharField(max_length=100, verbose_name=_(u"Short description"))

    theme = models.CharField(max_length=50, choices=EVENT_THEMES, verbose_name=_("Principal theme"))
    sub_themes = models.ManyToManyField(Theme, blank=True, verbose_name=_("Sub themes"))

    expert = models.ForeignKey("core.Expert", null=True)
    auction_house = models.ForeignKey("core.AuctionHouse", null=True)
    event_place = models.ForeignKey("core.EventPlace", null=True)


class NewsletterEmail(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(blank=True, unique=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.active, self.email)
