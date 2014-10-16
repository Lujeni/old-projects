# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Theme'
        db.create_table(u'core_theme', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'core', ['Theme'])

        # Adding model 'EventPlace'
        db.create_table(u'core_eventplace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=1028)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['diplomat.ISOCountry'], null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ad1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('ad2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal(u'core', ['EventPlace'])

        # Adding field 'Event.short_description'
        db.add_column(u'core_event', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Event.expert'
        db.add_column(u'core_event', 'expert',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Expert'], null=True),
                      keep_default=False)

        # Adding field 'Event.auction_house'
        db.add_column(u'core_event', 'auction_house',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.AuctionHouse'], null=True),
                      keep_default=False)

        # Adding field 'Event.event_place'
        db.add_column(u'core_event', 'event_place',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EventPlace'], null=True),
                      keep_default=False)

        # Adding M2M table for field sub_themes on 'Event'
        m2m_table_name = db.shorten_name(u'core_event_sub_themes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'core.event'], null=False)),
            ('theme', models.ForeignKey(orm[u'core.theme'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'theme_id'])


        # Changing field 'Event.description'
        db.alter_column(u'core_event', 'description', self.gf('django.db.models.fields.CharField')(max_length=500))
        # Adding field 'AuctionHouse.contact_phone_number'
        db.add_column(u'core_auctionhouse', 'contact_phone_number',
                      self.gf('phonenumber_field.modelfields.PhoneNumberField')(default='+330000000000', max_length=128),
                      keep_default=False)


        # Changing field 'AuctionHouse.city'
        db.alter_column(u'core_auctionhouse', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

        # Changing field 'AuctionHouse.ad2'
        db.alter_column(u'core_auctionhouse', 'ad2', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'AuctionHouse.ad1'
        db.alter_column(u'core_auctionhouse', 'ad1', self.gf('django.db.models.fields.CharField')(default='', max_length=64))

        # Changing field 'AuctionHouse.zipcode'
        db.alter_column(u'core_auctionhouse', 'zipcode', self.gf('django.db.models.fields.CharField')(default='', max_length=12))

        # Changing field 'AuctionHouse.longitude'
        db.alter_column(u'core_auctionhouse', 'longitude', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'AuctionHouse.address'
        db.alter_column(u'core_auctionhouse', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=1028))

        # Changing field 'AuctionHouse.latitude'
        db.alter_column(u'core_auctionhouse', 'latitude', self.gf('django.db.models.fields.FloatField')(default=0.0))

    def backwards(self, orm):
        # Deleting model 'Theme'
        db.delete_table(u'core_theme')

        # Deleting model 'EventPlace'
        db.delete_table(u'core_eventplace')

        # Deleting field 'Event.short_description'
        db.delete_column(u'core_event', 'short_description')

        # Deleting field 'Event.expert'
        db.delete_column(u'core_event', 'expert_id')

        # Deleting field 'Event.auction_house'
        db.delete_column(u'core_event', 'auction_house_id')

        # Deleting field 'Event.event_place'
        db.delete_column(u'core_event', 'event_place_id')

        # Removing M2M table for field sub_themes on 'Event'
        db.delete_table(db.shorten_name(u'core_event_sub_themes'))


        # Changing field 'Event.description'
        db.alter_column(u'core_event', 'description', self.gf('django.db.models.fields.CharField')(max_length=200))
        # Deleting field 'AuctionHouse.contact_phone_number'
        db.delete_column(u'core_auctionhouse', 'contact_phone_number')


        # Changing field 'AuctionHouse.city'
        db.alter_column(u'core_auctionhouse', 'city', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

        # Changing field 'AuctionHouse.ad2'
        db.alter_column(u'core_auctionhouse', 'ad2', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'AuctionHouse.ad1'
        db.alter_column(u'core_auctionhouse', 'ad1', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'AuctionHouse.zipcode'
        db.alter_column(u'core_auctionhouse', 'zipcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True))

        # Changing field 'AuctionHouse.longitude'
        db.alter_column(u'core_auctionhouse', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'AuctionHouse.address'
        db.alter_column(u'core_auctionhouse', 'address', self.gf('django.db.models.fields.CharField')(max_length=1028, null=True))

        # Changing field 'AuctionHouse.latitude'
        db.alter_column(u'core_auctionhouse', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True))

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
