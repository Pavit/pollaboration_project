# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'questions_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='submissions', null=True, blank=True, to=orm['accounts.MyUser'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'questions', ['Question'])

        # Adding M2M table for field answered_by on 'Question'
        m2m_table_name = db.shorten_name(u'questions_question_answered_by')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'questions.question'], null=False)),
            ('myuser', models.ForeignKey(orm[u'accounts.myuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'myuser_id'])

        # Adding model 'Answer'
        db.create_table(u'questions_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['questions.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('modified', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'questions', ['Answer'])

        # Adding M2M table for field selected_by on 'Answer'
        m2m_table_name = db.shorten_name(u'questions_answer_selected_by')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('answer', models.ForeignKey(orm[u'questions.answer'], null=False)),
            ('myuser', models.ForeignKey(orm[u'accounts.myuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['answer_id', 'myuser_id'])

        # Adding model 'Vote'
        db.create_table(u'questions_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('voter', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='votes', null=True, blank=True, to=orm['accounts.MyUser'])),
            ('answer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votes', to=orm['questions.Answer'])),
            ('created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'questions', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'questions_question')

        # Removing M2M table for field answered_by on 'Question'
        db.delete_table(db.shorten_name(u'questions_question_answered_by'))

        # Deleting model 'Answer'
        db.delete_table(u'questions_answer')

        # Removing M2M table for field selected_by on 'Answer'
        db.delete_table(db.shorten_name(u'questions_answer_selected_by'))

        # Deleting model 'Vote'
        db.delete_table(u'questions_vote')


    models = {
        u'accounts.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'agegroup': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'fb_access_token': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fb_username': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['accounts.MyUser']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        },
        u'questions.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['questions.Question']"}),
            'selected_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'answer_selections'", 'default': 'None', 'to': u"orm['accounts.MyUser']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'questions.question': {
            'Meta': {'object_name': 'Question'},
            'answered_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'questions_answered'", 'default': 'None', 'to': u"orm['accounts.MyUser']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'blank': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'submissions'", 'null': 'True', 'blank': 'True', 'to': u"orm['accounts.MyUser']"})
        },
        u'questions.vote': {
            'Meta': {'object_name': 'Vote'},
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votes'", 'to': u"orm['questions.Answer']"}),
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'votes'", 'null': 'True', 'blank': 'True', 'to': u"orm['accounts.MyUser']"})
        }
    }

    complete_apps = ['questions']