# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Product.product_descrition'
        db.delete_column(u'products_product', 'product_descrition')

        # Adding field 'Product.product_description'
        db.add_column(u'products_product', 'product_description',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 19, 0, 0), max_length=3000),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Product.product_descrition'
        db.add_column(u'products_product', 'product_descrition',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 19, 0, 0), max_length=2000),
                      keep_default=False)

        # Deleting field 'Product.product_description'
        db.delete_column(u'products_product', 'product_description')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_description': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['products']