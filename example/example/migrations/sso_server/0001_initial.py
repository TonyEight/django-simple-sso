# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Consumer'
        db.create_table('sso_server_consumer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('private_key', self.gf('django.db.models.fields.CharField')(default='gMM41GG14tA4G3MK5fkD6JwgI6oYcvrFkiC3hZvmITprkfYnqwydKqSrS6pTXfMF', unique=True, max_length=64)),
            ('public_key', self.gf('django.db.models.fields.CharField')(default='lmQiZaB2JmcQLdRQAlzBppYIfi0ajB5s9zDBFCb02PdpUcE8Fyof9UpKKFBT6GvQ', unique=True, max_length=64)),
        ))
        db.send_create_signal('sso_server', ['Consumer'])

        # Adding model 'Token'
        db.create_table('sso_server_token', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('consumer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tokens', to=orm['sso_server.Consumer'])),
            ('request_token', self.gf('django.db.models.fields.CharField')(default='zl0VgmwkBkYncwntdJsHiAuP0WVBO3P5ieRey2kIBL2Vqhr4hW19XDLsoTwYsUIm', unique=True, max_length=64)),
            ('access_token', self.gf('django.db.models.fields.CharField')(default='CZqpOerQQBL7uBuFrr9q6pRO38CVOD1X0szRgX9lb1vGtb24lton3ryIXQ5WroAV', unique=True, max_length=64)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 5, 16, 0, 0))),
            ('redirect_to', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal('sso_server', ['Token'])

    def backwards(self, orm):
        # Deleting model 'Consumer'
        db.delete_table('sso_server_consumer')

        # Deleting model 'Token'
        db.delete_table('sso_server_token')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sso_server.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'private_key': ('django.db.models.fields.CharField', [], {'default': "'KCwWe5PrdxoQdFDdukysYOCjbcS2tHfBImYKWbUevq9Xqe5GH4bXaeONhCKIa85W'", 'unique': 'True', 'max_length': '64'}),
            'public_key': ('django.db.models.fields.CharField', [], {'default': "'MLVg93GHvjZ9uINXbBVwvlPEZBNMfOZKY6z5mTigf1OJLq9F2Z0PnbuEyd4ZfIBh'", 'unique': 'True', 'max_length': '64'})
        },
        'sso_server.token': {
            'Meta': {'object_name': 'Token'},
            'access_token': ('django.db.models.fields.CharField', [], {'default': "'kqb56qhtyB6KvpiM8fbQnJ6243Sr7OfRMlJcQFyPeBBnRaARiiY3SCHItRgkpwM5'", 'unique': 'True', 'max_length': '64'}),
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tokens'", 'to': "orm['sso_server.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'request_token': ('django.db.models.fields.CharField', [], {'default': "'F7iu0pSdQOa1rt09JyMMvBQSYmgNcoRPBURyqpRoc7PTmjFHoHp7OymGxMSjOHKd'", 'unique': 'True', 'max_length': '64'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 16, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        }
    }

    complete_apps = ['sso_server']