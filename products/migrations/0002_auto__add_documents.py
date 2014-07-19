# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Documents'
        db.create_table(u'products_documents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docFile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'products', ['Documents'])


    def backwards(self, orm):
        # Deleting model 'Documents'
        db.delete_table(u'products_documents')


    models = {
        u'products.documents': {
            'Meta': {'object_name': 'Documents'},
            'docFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['products']