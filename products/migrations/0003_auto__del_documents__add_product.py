# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Documents'
        db.delete_table(u'products_documents')

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('product_descrition', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'products', ['Product'])


    def backwards(self, orm):
        # Adding model 'Documents'
        db.create_table(u'products_documents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docFile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'products', ['Documents'])

        # Deleting model 'Product'
        db.delete_table(u'products_product')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_descrition': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['products']