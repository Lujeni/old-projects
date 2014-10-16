# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsletterEmail'
        db.create_table(u'core_newsletteremail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'core', ['NewsletterEmail'])


    def backwards(self, orm):
        # Deleting model 'NewsletterEmail'
        db.delete_table(u'core_newsletteremail')


    models = {
        u'core.auctionhouse': {
            'Meta': {'object_name': 'AuctionHouse'},
            'ad1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'ad2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'contact_phone_number': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diplomat.ISOCountry']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'core.event': {
            'Meta': {'object_name': 'Event'},
            'auction_house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.AuctionHouse']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'event_place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EventPlace']", 'null': 'True'}),
            'expert': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Expert']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sub_themes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Theme']", 'symmetrical': 'False', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'core.eventplace': {
            'Meta': {'object_name': 'EventPlace'},
            'ad1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'ad2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1028'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diplomat.ISOCountry']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'core.expert': {
            'Meta': {'object_name': 'Expert'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'core.newsletteremail': {
            'Meta': {'object_name': 'NewsletterEmail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.theme': {
            'Meta': {'object_name': 'Theme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'diplomat.isocountry': {
            'Meta': {'ordering': "('name',)", 'object_name': 'ISOCountry'},
            'alpha2': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'alpha3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            'numeric': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'official_name': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '75', 'populate_from': "'name'", 'unique_with': '()'})
        }
    }

    complete_apps = ['core']