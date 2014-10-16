# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Expert'
        db.create_table(u'core_expert', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone_number', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'core', ['Expert'])


    def backwards(self, orm):
        # Deleting model 'Expert'
        db.delete_table(u'core_expert')


    models = {
        u'core.auctionhouse': {
            'Meta': {'object_name': 'AuctionHouse'},
            'ad1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'ad2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1028', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['diplomat.ISOCountry']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'})
        },
        u'core.event': {
            'Meta': {'object_name': 'Event'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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