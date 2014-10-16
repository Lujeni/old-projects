# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'core_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('theme', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['Event'])

        # Adding model 'AuctionHouse'
        db.create_table(u'core_auctionhouse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1028, null=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diplomat.ISOCountry'], null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ad1', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('ad2', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
        ))
        db.send_create_signal(u'core', ['AuctionHouse'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'core_event')

        # Deleting model 'AuctionHouse'
        db.delete_table(u'core_auctionhouse')


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