# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MyUser.is_active'
        db.add_column(u'accounts_myuser', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'MyUser.date_of_birth'
        db.alter_column(u'accounts_myuser', 'date_of_birth', self.gf('django.db.models.fields.DateField')())

        # Changing field 'MyUser.email'
        db.alter_column(u'accounts_myuser', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254))

    def backwards(self, orm):
        # Deleting field 'MyUser.is_active'
        db.delete_column(u'accounts_myuser', 'is_active')


        # Changing field 'MyUser.date_of_birth'
        db.alter_column(u'accounts_myuser', 'date_of_birth', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'MyUser.email'
        db.alter_column(u'accounts_myuser', 'email', self.gf('django.db.models.fields.EmailField')(max_length=255, unique=True))

    models = {
        u'accounts.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'agegroup': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'}),
            'fb_access_token': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['accounts.MyUser']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'locale': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'political': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'relationship_status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['accounts']