# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'lessons_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('flag', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('gmap', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'lessons', ['Country'])

        # Adding model 'GeoMap'
        db.create_table(u'lessons_geomap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lessons.Country'], to_field='gmap')),
        ))
        db.send_create_signal(u'lessons', ['GeoMap'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'lessons_country')

        # Deleting model 'GeoMap'
        db.delete_table(u'lessons_geomap')


    models = {
        u'lessons.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'gmap': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'lessons.geomap': {
            'Meta': {'object_name': 'GeoMap'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lessons.Country']", 'to_field': "'gmap'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['lessons']