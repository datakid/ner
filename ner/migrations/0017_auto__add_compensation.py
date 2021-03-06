# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compensation'
        db.create_table('ner_compensation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('injured_person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='injured_party', to=orm['ner.Person'])),
            ('organisation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='injured_partys_employer', to=orm['ner.Organisation'])),
            ('job_performed', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('employment_status', self.gf('django.db.models.fields.CharField')(max_length=2, null='TRUE', blank='TRUE')),
            ('org_department', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('location_of_accident', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_accident', self.gf('django.db.models.fields.DateField')()),
            ('date_accident_reported', self.gf('django.db.models.fields.DateField')()),
            ('date_of_claim', self.gf('django.db.models.fields.DateField')()),
            ('claimant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ner.Person'], null='TRUE', blank='TRUE')),
            ('relationship_to_injured_party', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('witness_1', self.gf('django.db.models.fields.related.ForeignKey')(blank='TRUE', related_name='witness_1', null='TRUE', to=orm['ner.Person'])),
            ('witness_1_relationship', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('witness_2', self.gf('django.db.models.fields.related.ForeignKey')(blank='TRUE', related_name='witness_2', null='TRUE', to=orm['ner.Person'])),
            ('witness_2_relationship', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('doctors_name', self.gf('django.db.models.fields.related.ForeignKey')(blank='TRUE', related_name='doctor', null='TRUE', to=orm['ner.Person'])),
            ('hospital', self.gf('django.db.models.fields.related.ForeignKey')(blank='TRUE', related_name='hospital', null='TRUE', to=orm['ner.Organisation'])),
            ('cause_of_injury', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('doctors_remarks', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('claim_status', self.gf('django.db.models.fields.CharField')(max_length=2, blank='True')),
            ('amount_paid', self.gf('django.db.models.fields.IntegerField')()),
            ('payment_voucher_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=20)),
        ))
        db.send_create_signal('ner', ['Compensation'])

    def backwards(self, orm):
        # Deleting model 'Compensation'
        db.delete_table('ner_compensation')

    models = {
        'ner.certificate': {
            'Meta': {'object_name': 'Certificate'},
            'course_content': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': "'True'", 'blank': "'True'"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': "'True'", 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institute': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'True'", 'related_name': "'certifications'", 'null': "'True'", 'to': "orm['ner.Person']"}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_grad': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': "'True'"})
        },
        'ner.compensation': {
            'Meta': {'object_name': 'Compensation'},
            'amount_paid': ('django.db.models.fields.IntegerField', [], {}),
            'cause_of_injury': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'claim_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': "'True'"}),
            'claimant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'TRUE'", 'blank': "'TRUE'"}),
            'date_accident_reported': ('django.db.models.fields.DateField', [], {}),
            'date_of_accident': ('django.db.models.fields.DateField', [], {}),
            'date_of_claim': ('django.db.models.fields.DateField', [], {}),
            'doctors_name': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'TRUE'", 'related_name': "'doctor'", 'null': "'TRUE'", 'to': "orm['ner.Person']"}),
            'doctors_remarks': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'employment_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': "'TRUE'", 'blank': "'TRUE'"}),
            'hospital': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'TRUE'", 'related_name': "'hospital'", 'null': "'TRUE'", 'to': "orm['ner.Organisation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'injured_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'injured_party'", 'to': "orm['ner.Person']"}),
            'job_performed': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'location_of_accident': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'org_department': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'injured_partys_employer'", 'to': "orm['ner.Organisation']"}),
            'payment_voucher_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'reference_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'relationship_to_injured_party': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '20'}),
            'witness_1': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'TRUE'", 'related_name': "'witness_1'", 'null': "'TRUE'", 'to': "orm['ner.Person']"}),
            'witness_1_relationship': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'witness_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'TRUE'", 'related_name': "'witness_2'", 'null': "'TRUE'", 'to': "orm['ner.Person']"}),
            'witness_2_relationship': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ner.experience': {
            'Meta': {'object_name': 'Experience'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Organisation']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'experiences'", 'to': "orm['ner.Person']"}),
            'reference_contact_email': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': "'True'", 'blank': "'True'"}),
            'reference_contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': "'True'", 'blank': "'True'"}),
            'reference_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': "'True'", 'blank': "'True'"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'ner.ftcqualification': {
            'Meta': {'object_name': 'FTCQualification'},
            'cadet_no': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'True'", 'blank': "'True'"}),
            'year_grad': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': "'True'"})
        },
        'ner.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': "'True'", 'blank': "'True'"}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': "'True'"}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': "'True'"}),
            'contact_phone_1': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': "'True'"}),
            'contact_phone_2': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': "'True'"}),
            'island': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': "'True'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'ner.person': {
            'Meta': {'object_name': 'Person'},
            'birth_place': ('django.db.models.fields.CharField', [], {'default': "'02'", 'max_length': '2', 'blank': "'True'"}),
            'current_address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'discharge_book': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': "'True'"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': "'1'"}),
            'home_island': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'island_represented': ('django.db.models.fields.CharField', [], {'default': "'01'", 'max_length': '2', 'blank': "'True'"}),
            'marital_status': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1', 'blank': "'True'"}),
            'medical_test_date': ('django.db.models.fields.DateField', [], {'null': "'True'", 'blank': "'True'"}),
            'number_of_dependants': ('django.db.models.fields.IntegerField', [], {'null': "'True'", 'blank': "'True'"}),
            'passport_no': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': "'True'"}),
            'phone_home': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': "'True'"}),
            'phone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'phone_other': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': "'True'"}),
            'previous_address': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': "'True'"}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': "'True'"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ner.Requirement']", 'null': "'True'", 'blank': "'True'"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ner.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'req_notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': "'True'"})
        },
        'ner.shipexperience': {
            'Meta': {'object_name': 'ShipExperience'},
            'disembark_date': ('django.db.models.fields.DateField', [], {}),
            'embark_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ner.Person']", 'null': "'True'", 'blank': "'True'"}),
            'recruiting_agency': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'vessel_company': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vessel_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vessel_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ner.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'applicants': ('django.db.models.fields.related.ManyToManyField', [], {'blank': "'True'", 'related_name': "'jobs'", 'null': "'True'", 'symmetrical': 'False', 'to': "orm['ner.Person']"}),
            'closing_date': ('django.db.models.fields.DateField', [], {}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': "'True'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'jobs_at'", 'to': "orm['ner.Organisation']"}),
            'requirements': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ner.Requirement']", 'symmetrical': 'False'}),
            'salary_level_1': ('django.db.models.fields.CharField', [], {'default': "'10'", 'max_length': '2'}),
            'salary_level_2': ('django.db.models.fields.CharField', [], {'default': "'10'", 'max_length': '2'}),
            'salary_level_3': ('django.db.models.fields.CharField', [], {'default': "'10'", 'max_length': '2'}),
            'salary_level_4': ('django.db.models.fields.CharField', [], {'default': "'10'", 'max_length': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ner']