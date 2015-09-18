# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aftercare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
                ('dangerousness', models.CharField(max_length=10, verbose_name=b'\xe5\x8d\xb1\xe9\x99\xa9\xe6\x80\xa7', choices=[('0\u7ea7', b'0\xe7\xba\xa7'), ('1\u7ea7', b'1\xe7\xba\xa7'), ('2\u7ea7', b'2\xe7\xba\xa7'), ('3\u7ea7', b'3\xe7\xba\xa7'), ('4\u7ea7', b'4\xe7\xba\xa7'), ('5\u7ea7', b'5\xe7\xba\xa7')])),
                ('now_symptom_extra', models.CharField(max_length=100, null=True, verbose_name=b'', blank=True)),
                ('insight', models.CharField(max_length=30, verbose_name=b'\xe8\x87\xaa\xe7\x9f\xa5\xe5\x8a\x9b', choices=[('\u81ea\u77e5\u529b\u5b8c\u5168', b'\xe8\x87\xaa\xe7\x9f\xa5\xe5\x8a\x9b\xe5\xae\x8c\xe5\x85\xa8'), ('\u81ea\u77e5\u529b\u4e0d\u5168', b'\xe8\x87\xaa\xe7\x9f\xa5\xe5\x8a\x9b\xe4\xb8\x8d\xe5\x85\xa8'), ('\u81ea\u77e5\u529b\u7f3a\u5931', b'\xe8\x87\xaa\xe7\x9f\xa5\xe5\x8a\x9b\xe7\xbc\xba\xe5\xa4\xb1')])),
                ('sleep_situation', models.CharField(max_length=10, verbose_name=b'\xe7\x9d\xa1\xe7\x9c\xa0\xe6\x83\x85\xe5\x86\xb5', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('diet_situation', models.CharField(max_length=10, verbose_name=b'\xe9\xa5\xae\xe9\xa3\x9f\xe6\x83\x85\xe5\x86\xb5', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('society_function_individual_life_care', models.CharField(max_length=10, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe7\x94\x9f\xe6\xb4\xbb\xe6\x96\x99\xe7\x90\x86', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('society_function_housework', models.CharField(max_length=10, verbose_name=b'\xe5\xae\xb6\xe5\x8a\xa1\xe5\x8a\xb3\xe5\x8a\xa8', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('society_function_productive_work', models.CharField(max_length=10, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe5\x8a\xb3\xe5\x8a\xa8\xe5\x8f\x8a\xe5\xb7\xa5\xe4\xbd\x9c', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae'), ('\u6b64\u9879\u4e0d\u9002\u7528', b'\xe6\xad\xa4\xe9\xa1\xb9\xe4\xb8\x8d\xe9\x80\x82\xe7\x94\xa8')])),
                ('society_function_learn_ability', models.CharField(max_length=10, verbose_name=b'\xe5\xad\xa6\xe4\xb9\xa0\xe8\x83\xbd\xe5\x8a\x9b', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('society_function_social_interpersonal', models.CharField(max_length=10, verbose_name=b'\xe7\xa4\xbe\xe4\xbc\x9a\xe4\xba\xba\xe9\x99\x85\xe4\xba\xa4\xe5\xbe\x80', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u8f83\u5dee', b'\xe8\xbe\x83\xe5\xb7\xae')])),
                ('disease_family_society_effect_mild_disturbance', models.PositiveSmallIntegerField(verbose_name=b'\xe8\xbd\xbb\xe5\xba\xa6\xe6\xbb\x8b\xe4\xba\x8b')),
                ('disease_family_society_effect_disturbance', models.PositiveSmallIntegerField(verbose_name=b'\xe8\x82\x87\xe4\xba\x8b')),
                ('disease_family_society_effect_accident', models.PositiveSmallIntegerField(verbose_name=b'\xe8\x82\x87\xe7\xa5\xb8')),
                ('disease_family_society_effect_autolesion', models.PositiveSmallIntegerField(verbose_name=b'\xe8\x87\xaa\xe4\xbc\xa4')),
                ('disease_family_society_effect_attempted_suicide', models.PositiveSmallIntegerField(verbose_name=b'\xe8\x87\xaa\xe6\x9d\x80\xe6\x9c\xaa\xe9\x81\x82')),
                ('lock_situation', models.CharField(max_length=30, verbose_name=b'\xe5\x85\xb3\xe9\x94\x81\xe6\x83\x85\xe5\x86\xb5', choices=[('\u65e0\u5173\u9501', b'\xe6\x97\xa0\xe5\x85\xb3\xe9\x94\x81'), ('\u5173\u9501', b'\xe5\x85\xb3\xe9\x94\x81'), ('\u5173\u9501\u5df2\u89e3\u9664', b'\xe5\x85\xb3\xe9\x94\x81\xe5\xb7\xb2\xe8\xa7\xa3\xe9\x99\xa4')])),
                ('hospitalized_situation', models.CharField(max_length=30, verbose_name=b'\xe4\xbd\x8f\xe9\x99\xa2\xe6\x83\x85\xe5\x86\xb5', choices=[('\u4ece\u672a\u4f4f\u9662', b'\xe4\xbb\x8e\xe6\x9c\xaa\xe4\xbd\x8f\xe9\x99\xa2'), ('\u76ee\u524d\u6b63\u5728\u4f4f\u9662', b'\xe7\x9b\xae\xe5\x89\x8d\xe6\xad\xa3\xe5\x9c\xa8\xe4\xbd\x8f\xe9\x99\xa2'), ('\u65e2\u5f80\u4f4f\u9662\uff0c\u73b0\u672a\u4f4f\u9662', b'\xe6\x97\xa2\xe5\xbe\x80\xe4\xbd\x8f\xe9\x99\xa2\xef\xbc\x8c\xe7\x8e\xb0\xe6\x9c\xaa\xe4\xbd\x8f\xe9\x99\xa2')])),
                ('last_hospitalized_date', models.DateField(max_length=10, null=True, verbose_name=b'\xe6\x9c\xab\xe6\xac\xa1\xe5\x87\xba\xe9\x99\xa2\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('laboratory_examination', models.CharField(max_length=10, verbose_name=b'\xe5\xae\x9e\xe9\xaa\x8c\xe5\xae\xa4\xe6\xa3\x80\xe6\x9f\xa5', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('laboratory_examination_yes', models.CharField(max_length=100, null=True, blank=True)),
                ('take_medicine_compliance', models.CharField(max_length=10, verbose_name=b'\xe6\x9c\x8d\xe8\x8d\xaf\xe4\xbe\x9d\xe4\xbb\x8e\xe6\x80\xa7', choices=[('\u89c4\u5f8b', b'\xe8\xa7\x84\xe5\xbe\x8b'), ('\u95f4\u65ad', b'\xe9\x97\xb4\xe6\x96\xad'), ('\u4e0d\u670d\u836f', b'\xe4\xb8\x8d\xe6\x9c\x8d\xe8\x8d\xaf')])),
                ('medicine_untoward_effect', models.CharField(max_length=10, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe4\xb8\x8d\xe8\x89\xaf\xe5\x8f\x8d\xe5\xba\x94', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('medicine_untoward_effect_yes', models.CharField(max_length=100, null=True, blank=True)),
                ('treatment_effect', models.CharField(max_length=10, verbose_name=b'\xe6\xb2\xbb\xe7\x96\x97\xe6\x95\x88\xe6\x9e\x9c', choices=[('\u75ca\u6108', b'\xe7\x97\x8a\xe6\x84\x88'), ('\u597d\u8f6c', b'\xe5\xa5\xbd\xe8\xbd\xac'), ('\u65e0\u53d8\u5316', b'\xe6\x97\xa0\xe5\x8f\x98\xe5\x8c\x96'), ('\u52a0\u91cd', b'\xe5\x8a\xa0\xe9\x87\x8d')])),
                ('transfer_treatment', models.CharField(max_length=5, verbose_name=b'\xe8\xbd\xac\xe8\xaf\x8a', choices=[('\u5426', b'\xe5\x90\xa6'), ('\u662f', b'\xe6\x98\xaf')])),
                ('transfer_treatment_reason', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xbd\xac\xe8\xaf\x8a\xe5\x8e\x9f\xe5\x9b\xa0', blank=True)),
                ('transfer_treatment_institution', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xbd\xac\xe8\xaf\x8a\xe8\x87\xb3\xe6\x9c\xba\xe6\x9e\x84\xe5\x8f\x8a\xe7\xa7\x91\xe5\xae\xa4', blank=True)),
                ('take_medicine_1', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb01', blank=True)),
                ('take_medicine_1_per', models.CharField(default=b'', choices=[('\u5929', b'\xe5\xa4\xa9'), ('\u6708', b'\xe6\x9c\x88')], max_length=10, blank=True, null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f')),
                ('take_medicine_1_time', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('take_medicine_1_mg', models.FloatField(null=True, blank=True)),
                ('take_medicine_2', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb02', blank=True)),
                ('take_medicine_2_per', models.CharField(default=b'', choices=[('\u5929', b'\xe5\xa4\xa9'), ('\u6708', b'\xe6\x9c\x88')], max_length=10, blank=True, null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f')),
                ('take_medicine_2_time', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('take_medicine_2_mg', models.FloatField(null=True, blank=True)),
                ('take_medicine_3', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb03', blank=True)),
                ('take_medicine_3_per', models.CharField(default=b'', choices=[('\u5929', b'\xe5\xa4\xa9'), ('\u6708', b'\xe6\x9c\x88')], max_length=10, blank=True, null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f')),
                ('take_medicine_3_time', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('take_medicine_3_mg', models.FloatField(null=True, blank=True)),
                ('recovery_measure_extra', models.CharField(max_length=30, null=True, verbose_name=b'', blank=True)),
                ('visit_classification', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\xac\xe6\xac\xa1\xe9\x9a\x8f\xe8\xae\xbf\xe5\x88\x86\xe7\xb1\xbb', choices=[('\u4e0d\u7a33\u5b9a', b'\xe4\xb8\x8d\xe7\xa8\xb3\xe5\xae\x9a'), ('\u57fa\u672c\u7a33\u5b9a', b'\xe5\x9f\xba\xe6\x9c\xac\xe7\xa8\xb3\xe5\xae\x9a'), ('\u7a33\u5b9a', b'\xe7\xa8\xb3\xe5\xae\x9a'), ('\u672a\u8bbf\u5230', b'\xe6\x9c\xaa\xe8\xae\xbf\xe5\x88\xb0')])),
                ('next_visit_date', models.DateField(verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
                ('doctor_signature', models.CharField(max_length=30, null=True, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe5\x8c\xbb\xe7\x94\x9f\xe7\xad\xbe\xe5\x90\x8d', blank=True)),
                ('now_symptom', models.ManyToManyField(to='ehr.SymptomChoice', null=True, verbose_name=b'\xe7\x9b\xae\xe5\x89\x8d\xe7\x97\x87\xe7\x8a\xb6', blank=True)),
            ],
            options={
                'db_table': 'psychiatric_aftercare',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PsychiatricInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guardian_name', models.CharField(max_length=20, verbose_name=b'\xe7\x9b\x91\xe6\x8a\xa4\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('guardian_relation', models.CharField(max_length=20, verbose_name=b'\xe4\xb8\x8e\xe6\x82\xa3\xe8\x80\x85\xe5\x85\xb3\xe7\xb3\xbb')),
                ('guardian_address', models.CharField(max_length=100, verbose_name=b'\xe7\x9b\x91\xe6\x8a\xa4\xe4\xba\xba\xe5\x9c\xb0\xe5\x9d\x80')),
                ('guardian_phone', models.CharField(max_length=20, verbose_name=b'\xe7\x9b\x91\xe6\x8a\xa4\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('community_contact_name', models.CharField(max_length=20, verbose_name=b'\xe8\xbe\x96\xe5\x8c\xba\xe6\x9d\x91\xef\xbc\x88\xe5\xb1\x85\xef\xbc\x89\xe5\xa7\x94\xe4\xbc\x9a\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba')),
                ('community_contact_phone', models.CharField(max_length=20, verbose_name=b'\xe8\xbe\x96\xe5\x8c\xba\xe6\x9d\x91\xef\xbc\x88\xe5\xb1\x85\xef\xbc\x89\xe5\xa7\x94\xe4\xbc\x9a\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('assent', models.CharField(max_length=20, choices=[('\u540c\u610f\u53c2\u52a0\u7ba1\u7406', '\u540c\u610f\u53c2\u52a0\u7ba1\u7406'), ('\u4e0d\u540c\u610f\u53c2\u52a0\u7ba1\u7406', '\u4e0d\u540c\u610f\u53c2\u52a0\u7ba1\u7406')])),
                ('signature_date', models.DateField(verbose_name=b'\xe7\xad\xbe\xe5\xad\x97\xe6\x97\xb6\xe9\x97\xb4')),
                ('disease_begin_date', models.DateField(verbose_name=b'\xe5\x88\x9d\xe6\xac\xa1\xe5\x8f\x91\xe7\x97\x85\xe6\x97\xb6\xe9\x97\xb4')),
                ('symptom_other', models.CharField(max_length=20, null=True, blank=True)),
                ('cure_outpatient', models.CharField(max_length=20, choices=[('\u672a\u6cbb', '\u672a\u6cbb'), ('\u95f4\u65ad\u95e8\u8bca\u6cbb\u7597', '\u95f4\u65ad\u95e8\u8bca\u6cbb\u7597'), ('\u8fde\u7eed\u95e8\u8bca\u6cbb\u7597', '\u8fde\u7eed\u95e8\u8bca\u6cbb\u7597')])),
                ('drug_first_date', models.DateField(verbose_name=b'\xe9\xa6\x96\xe6\xac\xa1\xe6\x8a\x97\xe7\xb2\xbe\xe7\xa5\x9e\xe7\x97\x85\xe8\x8d\xaf\xe7\x89\xa9\xe6\xb2\xbb\xe7\x96\x97\xe6\x97\xb6\xe9\x97\xb4')),
                ('cure_hospital', models.IntegerField(verbose_name=b'\xe6\x9b\xbe\xe4\xbd\x8f\xe7\xb2\xbe\xe7\xa5\x9e\xe4\xb8\x93\xe7\xa7\x91\xe5\x8c\xbb\xe9\x99\xa2/\xe7\xbb\xbc\xe5\x90\x88\xe5\x8c\xbb\xe9\x99\xa2\xe7\xb2\xbe\xe7\xa5\x9e\xe4\xb8\x93\xe7\xa7\x91')),
                ('diagnose', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\x8a\xe6\x96\xad')),
                ('diagnose_hospital', models.CharField(max_length=30, verbose_name=b'\xe8\xaf\x8a\xe6\x96\xad\xe5\x8c\xbb\xe9\x99\xa2')),
                ('diagnose_date', models.DateField(verbose_name=b'\xe8\xaf\x8a\xe6\x96\xad\xe6\x97\xa5\xe6\x9c\x9f')),
                ('cure_effect', models.CharField(max_length=10, verbose_name=b'\xe6\x9c\x80\xe8\xbf\x91\xe4\xb8\x80\xe6\xac\xa1\xe6\xb2\xbb\xe7\x96\x97\xe6\x95\x88\xe6\x9e\x9c', choices=[('\u75ca\u6108', '\u75ca\u6108'), ('\u597d\u8f6c', '\u597d\u8f6c'), ('\u65e0\u53d8\u5316', '\u65e0\u53d8\u5316'), ('\u52a0\u91cd', '\u52a0\u91cd')])),
                ('social_effect_minor', models.IntegerField(null=True, verbose_name=b'1 \xe8\xbd\xbb\xe5\xba\xa6\xe6\xbb\x8b\xe4\xba\x8b', blank=True)),
                ('social_effect_trouble', models.IntegerField(null=True, verbose_name=b'2 \xe8\x82\x87\xe4\xba\x8b', blank=True)),
                ('social_effect_disaster', models.IntegerField(null=True, verbose_name=b'3 \xe8\x82\x87\xe7\xa5\xb8', blank=True)),
                ('social_effect_self_injury', models.IntegerField(null=True, verbose_name=b'4 \xe8\x87\xaa\xe4\xbc\xa4', blank=True)),
                ('social_effect_suicide', models.IntegerField(null=True, verbose_name=b'5 \xe8\x87\xaa\xe6\x9d\x80', blank=True)),
                ('lock', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xb3\xe9\x94\x81\xe6\x83\x85\xe5\x86\xb5', choices=[('\u65e0\u5173\u9501', '\u65e0\u5173\u9501'), ('\u5173\u9501', '\u5173\u9501'), ('\u5173\u9501\u5df2\u89e3\u9664', '\u5173\u9501\u5df2\u89e3\u9664')])),
                ('economy', models.CharField(max_length=50, verbose_name=b'\xe7\xbb\x8f\xe6\xb5\x8e\xe7\x8a\xb6\xe5\x86\xb5', choices=[('\u8d2b\u56f0\uff0c\u5728\u5f53\u5730\u8d2b\u56f0\u6807\u51c6\u4ee5\u4e0b', '\u8d2b\u56f0\uff0c\u5728\u5f53\u5730\u8d2b\u56f0\u6807\u51c6\u4ee5\u4e0b'), ('\u975e\u8d2b\u56f0', '\u975e\u8d2b\u56f0'), ('\u4e0d\u7965', '\u4e0d\u7965')])),
                ('doctor_advice', models.CharField(max_length=200, null=True, verbose_name=b'\xe4\xb8\x93\xe7\xa7\x91\xe5\x8c\xbb\xe7\x94\x9f\xe6\x84\x8f\xe8\xa7\x81\xef\xbc\x88\xe5\xa6\x82\xe6\x9e\x9c\xe6\x9c\x89\xe8\xaf\xb7\xe8\xae\xb0\xe5\xbd\x95\xef\xbc\x89', blank=True)),
                ('fill_table_date', models.DateField(verbose_name=b'\xe5\xa1\xab\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('doctor_signature', models.CharField(max_length=10, null=True, verbose_name=b'\xe5\x8c\xbb\xe7\x94\x9f\xe7\xad\xbe\xe5\xad\x97', blank=True)),
                ('symptom', models.ManyToManyField(related_name='choices', verbose_name=b'\xe6\x97\xa2\xe5\xbe\x80\xe4\xb8\xbb\xe8\xa6\x81\xe7\x97\x87\xe7\x8a\xb6', to='ehr.SymptomChoice')),
            ],
            options={
                'db_table': 'ehr_psychiatric_info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecoveryMeasureChoices',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aftercare',
            name='recovery_measure',
            field=models.ManyToManyField(to='psychiatric.RecoveryMeasureChoices', null=True, verbose_name=b'\xe5\xba\xb7\xe5\xa4\x8d\xe6\x8e\xaa\xe6\x96\xbd', blank=True),
            preserve_default=True,
        ),
    ]
