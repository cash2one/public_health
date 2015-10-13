# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyHistoryYesChoices',
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
        migrations.CreateModel(
            name='BodyExam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(null=True, verbose_name=b'\xe4\xbd\x93\xe6\xa3\x80\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('doctor', models.CharField(max_length=10, null=True, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe5\x8c\xbb\xe7\x94\x9f', blank=True)),
                ('body_temperature', models.FloatField(null=True, verbose_name=b'\xe4\xbd\x93\xe6\xb8\xa9', blank=True)),
                ('pulse', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe8\x84\x89\xe7\x8e\x87', blank=True)),
                ('breath_frequency', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe5\x91\xbc\xe5\x90\xb8\xe9\xa2\x91\xe7\x8e\x87', blank=True)),
                ('blood_pressure_left_sbp', models.FloatField(null=True, verbose_name=b'\xe5\xb7\xa6\xe4\xbe\xa7\xe6\x94\xb6\xe7\xbc\xa9\xe5\x8e\x8b', blank=True)),
                ('blood_pressure_left_dbp', models.FloatField(null=True, verbose_name=b'\xe5\xb7\xa6\xe4\xbe\xa7\xe8\x88\x92\xe5\xbc\xa0\xe5\x8e\x8b', blank=True)),
                ('blood_pressure_right_sbp', models.FloatField(null=True, verbose_name=b'\xe5\x8f\xb3\xe4\xbe\xa7\xe6\x94\xb6\xe7\xbc\xa9\xe5\x8e\x8b', blank=True)),
                ('blood_pressure_right_dbp', models.FloatField(null=True, verbose_name=b'\xe5\x8f\xb3\xe4\xbe\xa7\xe8\x88\x92\xe5\xbc\xa0\xe5\x8e\x8b', blank=True)),
                ('height', models.FloatField(null=True, verbose_name=b'\xe8\xba\xab\xe9\xab\x98', blank=True)),
                ('weight', models.FloatField(null=True, verbose_name=b'\xe4\xbd\x93\xe9\x87\x8d', blank=True)),
                ('waistline', models.FloatField(null=True, verbose_name=b'\xe8\x85\xb0\xe5\x9b\xb4', blank=True)),
                ('body_mass_index', models.FloatField(null=True, verbose_name=b'\xe4\xbd\x93\xe8\xb4\xa8\xe6\x8c\x87\xe6\x95\xb0', blank=True)),
                ('mouth_lip', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\x8f\xa3\xe5\x94\x87', choices=[('\u7ea2\u6da6', b'\xe7\xba\xa2\xe6\xb6\xa6'), ('\u82cd\u767d', b'\xe8\x8b\x8d\xe7\x99\xbd'), ('\u53d1\u7ec0', b'\xe5\x8f\x91\xe7\xbb\x80'), ('\u76b2\u88c2', b'\xe7\x9a\xb2\xe8\xa3\x82'), ('\u75b1\u75b9', b'\xe7\x96\xb1\xe7\x96\xb9')])),
                ('mouth_tooth', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe9\xbd\xbf\xe5\x88\x97', choices=[('\u6b63\u5e38', b'\xe6\xad\xa3\xe5\xb8\xb8'), ('\u7f3a\u9f7f', b'\xe7\xbc\xba\xe9\xbd\xbf'), ('\u9f8b\u9f7f', b'\xe9\xbe\x8b\xe9\xbd\xbf'), ('\u4e49\u9f7f\uff08\u5047\u7259\uff09', b'\xe4\xb9\x89\xe9\xbd\xbf\xef\xbc\x88\xe5\x81\x87\xe7\x89\x99\xef\xbc\x89')])),
                ('mouth_tooth_missing_upleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_missing_bottomleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_missing_upright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_missing_bottomright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_decayed_upleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_decayed_bottomleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_decayed_upright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_decayed_bottomright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_denture_upleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_denture_bottomleft', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_denture_upright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_tooth_denture_bottomright', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('mouth_throat', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\x92\xbd\xe9\x83\xa8', choices=[('\u65e0\u5145\u8840', b'\xe6\x97\xa0\xe5\x85\x85\xe8\xa1\x80'), ('\u5145\u8840', b'\xe5\x85\x85\xe8\xa1\x80'), ('\u6dcb\u5df4\u6ee4\u6ce1\u589e\u751f', b'\xe6\xb7\x8b\xe5\xb7\xb4\xe6\xbb\xa4\xe6\xb3\xa1\xe5\xa2\x9e\xe7\x94\x9f')])),
                ('eyesight_left', models.FloatField(null=True, verbose_name=b'\xe5\xb7\xa6\xe7\x9c\xbc', blank=True)),
                ('eyesight_right', models.FloatField(null=True, verbose_name=b'\xe5\x8f\xb3\xe7\x9c\xbc', blank=True)),
                ('eyesight_left_rectified', models.FloatField(null=True, verbose_name=b'\xe7\x9f\xab\xe6\xad\xa3\xe8\xa7\x86\xe5\x8a\x9b\xe5\xb7\xa6\xe7\x9c\xbc', blank=True)),
                ('eyesight_right_rectified', models.FloatField(null=True, verbose_name=b'\xe7\x9f\xab\xe6\xad\xa3\xe8\xa7\x86\xe5\x8a\x9b\xe5\x8f\xb3\xe7\x9c\xbc', blank=True)),
                ('hearing', models.CharField(blank=True, max_length=60, null=True, verbose_name=b'\xe5\x90\xac\xe5\x8a\x9b', choices=[('\u542c\u89c1', b'\xe5\x90\xac\xe8\xa7\x81'), ('\u542c\u4e0d\u6e05\u6216\u65e0\u6cd5\u542c\u89c1', b'\xe5\x90\xac\xe4\xb8\x8d\xe6\xb8\x85\xe6\x88\x96\xe6\x97\xa0\xe6\xb3\x95\xe5\x90\xac\xe8\xa7\x81')])),
                ('movement_function', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'\xe8\xbf\x90\xe5\x8a\xa8\xe5\x8a\x9f\xe8\x83\xbd', choices=[('\u53ef\u987a\u5229\u5b8c\u6210', b'\xe5\x8f\xaf\xe9\xa1\xba\xe5\x88\xa9\xe5\xae\x8c\xe6\x88\x90'), ('\u65e0\u6cd5\u72ec\u7acb\u5b8c\u6210\u5176\u4e2d\u4efb\u4f55\u4e00\u4e2a\u52a8\u4f5c', b'\xe6\x97\xa0\xe6\xb3\x95\xe7\x8b\xac\xe7\xab\x8b\xe5\xae\x8c\xe6\x88\x90\xe5\x85\xb6\xe4\xb8\xad\xe4\xbb\xbb\xe4\xbd\x95\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa8\xe4\xbd\x9c')])),
                ('skin', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe7\x9a\xae\xe8\x82\xa4', choices=[('\u6b63\u5e38', b'\xe6\xad\xa3\xe5\xb8\xb8'), ('\u6f6e\u7ea2', b'\xe6\xbd\xae\xe7\xba\xa2'), ('\u82cd\u767d', b'\xe8\x8b\x8d\xe7\x99\xbd'), ('\u53d1\u7ec0', b'\xe5\x8f\x91\xe7\xbb\x80'), ('\u9ec4\u67d3', b'\xe9\xbb\x84\xe6\x9f\x93'), ('\u8272\u7d20\u6c89\u7740', b'\xe8\x89\xb2\xe7\xb4\xa0\xe6\xb2\x89\xe7\x9d\x80'), ('\u5176\u4ed6', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('skin_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('lymph_node', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe6\xb7\x8b\xe5\xb7\xb4\xe7\xbb\x93', choices=[('\u672a\u89e6\u53ca', b'\xe6\x9c\xaa\xe8\xa7\xa6\xe5\x8f\x8a'), ('\u9501\u9aa8\u4e0a', b'\xe9\x94\x81\xe9\xaa\xa8\xe4\xb8\x8a'), ('\u814b\u7a9d', b'\xe8\x85\x8b\xe7\xaa\x9d'), ('\u5176\u4ed6', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('lymph_node_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('lung_barrel_chested', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe6\xa1\xb6\xe7\x8a\xb6\xe8\x83\xb8', choices=[('\u5426', b'\xe5\x90\xa6'), ('\u662f', b'\xe6\x98\xaf')])),
                ('lung_breath_sound', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\x91\xbc\xe5\x90\xb8\xe9\x9f\xb3', choices=[('\u5426', b'\xe5\x90\xa6'), ('\u662f', b'\xe6\x98\xaf')])),
                ('lung_breath_sound_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('lung_rale', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe7\xbd\x97\xe9\x9f\xb3', choices=[('\u5426', b'\xe5\x90\xa6'), ('\u5e72\u7f57\u97f3', b'\xe5\xb9\xb2\xe7\xbd\x97\xe9\x9f\xb3'), ('\u6e7f\u7f57\u97f3', b'\xe6\xb9\xbf\xe7\xbd\x97\xe9\x9f\xb3'), ('\u5176\u4ed6', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('lung_rale_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('heart_rate', models.IntegerField(null=True, verbose_name=b'\xe5\xbf\x83\xe7\x8e\x87', blank=True)),
                ('heart_rhythm', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\xbf\x83\xe5\xbe\x8b', choices=[('\u9f50', '\u9f50'), ('\u4e0d\u9f50', '\u4e0d\u9f50'), ('\u7edd\u5bf9\u4e0d\u9f50', '\u7edd\u5bf9\u4e0d\u9f50')])),
                ('heart_noise', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe6\x9d\x82\xe9\x9f\xb3', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('heart_noise_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('stomach_tenderness', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\x8e\x8b\xe7\x97\x9b', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('stomach_tenderness_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('stomach_enclosed_mass', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\x8c\x85\xe5\x9d\x97', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('stomach_enclosed_mass_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('stomach_hepatomegaly', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe8\x82\x9d\xe5\xa4\xa7', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('stomach_hepatomegaly_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('stomach_slenauxe', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe8\x84\xbe\xe5\xa4\xa7', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('stomach_slenauxe_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('stomach_shifting_dullness', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe7\xa7\xbb\xe5\x8a\xa8\xe6\x80\xa7\xe6\xb5\x8a\xe9\x9f\xb3', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('stomach_shifting_dullness_extra', models.CharField(max_length=100, null=True, blank=True)),
                ('hemoglobin', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe7\xba\xa2\xe8\x9b\x8b\xe7\x99\xbd', blank=True)),
                ('leucocyte', models.FloatField(null=True, verbose_name=b'\xe7\x99\xbd\xe7\xbb\x86\xe8\x83\x9e', blank=True)),
                ('blood_platelets', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe5\xb0\x8f\xe6\x9d\xbf', blank=True)),
                ('blood_routine_test_extra', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True)),
                ('urine_protein', models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xb0\xbf\xe8\x9b\x8b\xe7\x99\xbd', blank=True)),
                ('urine_glucose', models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xb0\xbf\xe7\xb3\x96', blank=True)),
                ('ketone_bodies', models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xb0\xbf\xe9\x85\xae\xe4\xbd\x93', blank=True)),
                ('occult_blood', models.CharField(max_length=10, null=True, verbose_name=b'\xe5\xb0\xbf\xe6\xbd\x9c\xe8\xa1\x80', blank=True)),
                ('routine_urine_test_extra', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True)),
                ('blood_glucose_mmol', models.FloatField(null=True, blank=True)),
                ('blood_glucose_mg', models.FloatField(null=True, blank=True)),
                ('electr_gram', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'', choices=[('\u6b63\u5e38', b'\xe6\xad\xa3\xe5\xb8\xb8'), ('\u5f02\u5e38', b'\xe5\xbc\x82\xe5\xb8\xb8')])),
                ('electr_gram_abnormal', models.CharField(max_length=50, null=True, verbose_name=b'', blank=True)),
                ('alt', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe6\xb8\x85\xe8\xb0\xb7\xe4\xb8\x99\xe8\xbd\xac\xe6\xb0\xa8\xe9\x85\xb6', blank=True)),
                ('ast', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe6\xb8\x85\xe8\xb0\xb7\xe8\x8d\x89\xe8\xbd\xac\xe6\xb0\xa8\xe9\x85\xb6', blank=True)),
                ('tbil', models.FloatField(null=True, verbose_name=b'\xe6\x80\xbb\xe8\x83\x86\xe7\xba\xa2\xe7\xb4\xa0', blank=True)),
                ('scr', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe6\xb8\x85\xe8\x82\x8c\xe9\x85\x90', blank=True)),
                ('bun', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe5\xb0\xbf\xe7\xb4\xa0\xe6\xb0\xae', blank=True)),
                ('tc', models.FloatField(null=True, verbose_name=b'\xe6\x80\xbb\xe8\x83\x86\xe5\x9b\xba\xe9\x86\x87', blank=True)),
                ('tg', models.FloatField(null=True, verbose_name=b'\xe7\x94\x98\xe6\xb2\xb9\xe4\xb8\x89\xe8\x84\x82', blank=True)),
                ('ldl_c', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe6\xb8\x85\xe4\xbd\x8e\xe5\xaf\x86\xe5\xba\xa6\xe8\x84\x82\xe8\x9b\x8b\xe7\x99\xbd\xe8\x83\x86\xe5\x9b\xba\xe9\x86\x87', blank=True)),
                ('hdl_c', models.FloatField(null=True, verbose_name=b'\xe8\xa1\x80\xe6\xb8\x85\xe9\xab\x98\xe5\xaf\x86\xe5\xba\xa6\xe8\x84\x82\xe8\x9b\x8b\xe7\x99\xbd\xe8\x83\x86\xe5\x9b\xba\xe9\x86\x87', blank=True)),
                ('b_ultrasonic', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xbd\xa9\xe8\xb6\x85', blank=True)),
                ('pinghe', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe5\xb9\xb3\xe5\x92\x8c\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u57fa\u672c\u662f', b'\xe5\x9f\xba\xe6\x9c\xac\xe6\x98\xaf')])),
                ('qixu', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe6\xb0\x94\xe8\x99\x9a\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('yangxu', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe9\x98\xb3\xe8\x99\x9a\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('yinxu', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe9\x98\xb4\xe8\x99\x9a\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('tanshi', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe7\x97\xb0\xe6\xb9\xbf\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('shire', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe6\xb9\xbf\xe7\x83\xad\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('xueyu', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe8\xa1\x80\xe7\x98\x80\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('qiyu', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe6\xb0\x94\xe9\x83\x81\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('tebing', models.CharField(blank=True, max_length=15, null=True, verbose_name=b'\xe7\x89\xb9\xe7\xa6\x80\xe8\xb4\xa8', choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DisabilityChoices',
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
        migrations.CreateModel(
            name='DiseaseHistoryChoices',
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
        migrations.CreateModel(
            name='ExposeHistoryYesChoices',
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
        migrations.CreateModel(
            name='FamilyHistoryChoices',
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
        migrations.CreateModel(
            name='PaymentWayChoices',
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
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=30, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('\u672a\u77e5\u7684\u6027\u522b', b'\xe6\x9c\xaa\xe7\x9f\xa5\xe7\x9a\x84\xe6\x80\xa7\xe5\x88\xab'), ('\u7537', b'\xe7\x94\xb7'), ('\u5973', b'\xe5\xa5\xb3'), ('\u672a\u8bf4\u660e\u7684\u6027\u522b', b'\xe6\x9c\xaa\xe8\xaf\xb4\xe6\x98\x8e\xe7\x9a\x84\xe6\x80\xa7\xe5\x88\xab')])),
                ('birthday', models.DateField(max_length=10, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('identity', models.CharField(max_length=30, null=True, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7', blank=True)),
                ('work_company', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x8d\x95\xe4\xbd\x8d', blank=True)),
                ('phone', models.CharField(max_length=11, null=True, verbose_name=b'\xe6\x9c\xac\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('contact_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
                ('contact_phone', models.CharField(max_length=11, null=True, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('residence_type', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe5\xb8\xb8\xe4\xbd\x8f\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u6237\u7c4d', b'\xe6\x88\xb7\xe7\xb1\x8d'), ('\u975e\u6237\u7c4d', b'\xe9\x9d\x9e\xe6\x88\xb7\xe7\xb1\x8d')])),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe6\xb0\x91\xe6\x97\x8f', choices=[('\u6c49\u65cf', b'\xe6\xb1\x89\xe6\x97\x8f'), ('\u5c11\u6570\u6c11\u65cf', b'\xe5\xb0\x91\xe6\x95\xb0\xe6\xb0\x91\xe6\x97\x8f')])),
                ('nation_extra', models.CharField(max_length=20, null=True, verbose_name=b'', blank=True)),
                ('blood_type', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe8\xa1\x80\xe5\x9e\x8b', choices=[('A\u578b', b'A\xe5\x9e\x8b'), ('B\u578b', b'B\xe5\x9e\x8b'), ('O\u578b', b'O\xe5\x9e\x8b'), ('AB\u578b', b'AB\xe5\x9e\x8b'), ('\u4e0d\u8be6', b'\xe4\xb8\x8d\xe8\xaf\xa6')])),
                ('blood_rh', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'RH\xe9\x98\xb4\xe6\x80\xa7', choices=[('\u5426', b'\xe5\x90\xa6'), ('\u662f', b'\xe6\x98\xaf'), ('\u4e0d\u8be6', b'\xe4\xb8\x8d\xe8\xaf\xa6')])),
                ('education', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe6\x96\x87\xe5\x8c\x96\xe7\xa8\x8b\xe5\xba\xa6', choices=[('\u6587\u76f2\u53ca\u534a\u6587\u76f2', b'\xe6\x96\x87\xe7\x9b\xb2\xe5\x8f\x8a\xe5\x8d\x8a\xe6\x96\x87\xe7\x9b\xb2'), ('\u5c0f\u5b66', b'\xe5\xb0\x8f\xe5\xad\xa6'), ('\u521d\u4e2d', b'\xe5\x88\x9d\xe4\xb8\xad'), ('\u9ad8\u4e2d/\u6280\u6821/\u4e2d\u4e13', b'\xe9\xab\x98\xe4\xb8\xad/\xe6\x8a\x80\xe6\xa0\xa1/\xe4\xb8\xad\xe4\xb8\x93'), ('\u5927\u5b66\u4e13\u79d1\u53ca\u4ee5\u4e0a', b'\xe5\xa4\xa7\xe5\xad\xa6\xe4\xb8\x93\xe7\xa7\x91\xe5\x8f\x8a\xe4\xbb\xa5\xe4\xb8\x8a'), ('\u4e0d\u8be6', b'\xe4\xb8\x8d\xe8\xaf\xa6')])),
                ('occupation', models.CharField(blank=True, max_length=200, null=True, verbose_name=b'\xe8\x81\x8c\xe4\xb8\x9a', choices=[('\u56fd\u5bb6\u673a\u5173\u3001\u515a\u7fa4\u7ec4\u7ec7\u3001\u4f01\u4e1a\u3001\u4e8b\u4e1a\u5355\u4f4d\u8d1f\u8d23\u4eba', b'\xe5\x9b\xbd\xe5\xae\xb6\xe6\x9c\xba\xe5\x85\xb3\xe3\x80\x81\xe5\x85\x9a\xe7\xbe\xa4\xe7\xbb\x84\xe7\xbb\x87\xe3\x80\x81\xe4\xbc\x81\xe4\xb8\x9a\xe3\x80\x81\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba'), ('\u4e13\u4e1a\u6280\u672f\u4eba\u5458', b'\xe4\xb8\x93\xe4\xb8\x9a\xe6\x8a\x80\xe6\x9c\xaf\xe4\xba\xba\xe5\x91\x98'), ('\u529e\u4e8b\u4eba\u5458\u548c\u6709\u5173\u4eba\u5458', b'\xe5\x8a\x9e\xe4\xba\x8b\xe4\xba\xba\xe5\x91\x98\xe5\x92\x8c\xe6\x9c\x89\xe5\x85\xb3\xe4\xba\xba\xe5\x91\x98'), ('\u5546\u4e1a\u3001\u670d\u52a1\u4e1a\u4eba\u5458', b''), ('\u519c\u3001\u6797\u3001\u7267\u3001\u6e14\u3001\u6c34\u5229\u4e1a\u751f\u4ea7\u4eba\u5458', b'\xe5\x86\x9c\xe3\x80\x81\xe6\x9e\x97\xe3\x80\x81\xe7\x89\xa7\xe3\x80\x81\xe6\xb8\x94\xe3\x80\x81\xe6\xb0\xb4\xe5\x88\xa9\xe4\xb8\x9a\xe7\x94\x9f\xe4\xba\xa7\xe4\xba\xba\xe5\x91\x98'), ('\u751f\u4ea7\u3001\u8fd0\u8f93\u8bbe\u5907\u64cd\u4f5c\u4eba\u5458\u53ca\u6709\u5173\u4eba\u5458', b'\xe7\x94\x9f\xe4\xba\xa7\xe3\x80\x81\xe8\xbf\x90\xe8\xbe\x93\xe8\xae\xbe\xe5\xa4\x87\xe6\x93\x8d\xe4\xbd\x9c\xe4\xba\xba\xe5\x91\x98\xe5\x8f\x8a\xe6\x9c\x89\xe5\x85\xb3\xe4\xba\xba\xe5\x91\x98'), ('\u519b\u4eba', b'\xe5\x86\x9b\xe4\xba\xba'), ('\u4e0d\u4fbf\u5206\u7c7b\u7684\u5176\u4ed6\u4ece\u4e1a\u4eba\u5458', b'\xe4\xb8\x8d\xe4\xbe\xbf\xe5\x88\x86\xe7\xb1\xbb\xe7\x9a\x84\xe5\x85\xb6\xe4\xbb\x96\xe4\xbb\x8e\xe4\xb8\x9a\xe4\xba\xba\xe5\x91\x98')])),
                ('marriage', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'\xe5\xa9\x9a\xe5\xa7\xbb\xe7\x8a\xb6\xe5\x86\xb5', choices=[('\u672a\u5a5a', b'\xe6\x9c\xaa\xe5\xa9\x9a'), ('\u5df2\u5a5a', b'\xe5\xb7\xb2\xe5\xa9\x9a'), ('\u4e27\u5076', b'\xe4\xb8\xa7\xe5\x81\xb6'), ('\u79bb\u5a5a', b'\xe7\xa6\xbb\xe5\xa9\x9a'), ('\u672a\u8bf4\u660e\u7684\u5a5a\u59fb\u72b6\u51b5', b'\xe6\x9c\xaa\xe8\xaf\xb4\xe6\x98\x8e\xe7\x9a\x84\xe5\xa9\x9a\xe5\xa7\xbb\xe7\x8a\xb6\xe5\x86\xb5')])),
                ('payment_way_extra', models.CharField(max_length=100, null=True, verbose_name=b'', blank=True)),
                ('allergy_history_yes_extra', models.CharField(max_length=100, null=True, verbose_name=b'', blank=True)),
                ('disease_history_cancer', models.CharField(max_length=50, null=True, verbose_name=b'', blank=True)),
                ('disease_history_occupational', models.CharField(max_length=50, null=True, verbose_name=b'', blank=True)),
                ('disease_history_extra', models.CharField(max_length=50, null=True, verbose_name=b'', blank=True)),
                ('diagnose_date_2', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_3', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_4', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_5', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_6', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_7', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_8', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_9', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_10', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_11', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_12', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('diagnose_date_13', models.DateField(null=True, verbose_name=b'\xe7\xa1\xae\xe8\xaf\x8a\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('surgery_history', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xaf', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('surgery_1_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb01', blank=True)),
                ('surgery_1_date', models.DateField(null=True, blank=True)),
                ('surgery_2_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb02', blank=True)),
                ('surgery_2_date', models.DateField(null=True, blank=True)),
                ('injury_history', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe5\xa4\x96\xe4\xbc\xa4', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('injury_1_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb01', blank=True)),
                ('injury_1_date', models.DateField(null=True, blank=True)),
                ('injury_2_name', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb02', blank=True)),
                ('injury_2_date', models.DateField(null=True, blank=True)),
                ('transfusion_history', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe8\xbe\x93\xe8\xa1\x80', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('transfusion_1_reason', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x8e\x9f\xe5\x9b\xa01', blank=True)),
                ('transfusion_1_date', models.DateField(null=True, blank=True)),
                ('transfusion_2_reason', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\x8e\x9f\xe5\x9b\xa02', blank=True)),
                ('transfusion_2_date', models.DateField(null=True, blank=True)),
                ('family_history_father_extra', models.CharField(max_length=30, null=True, blank=True)),
                ('family_history_mother_extra', models.CharField(max_length=30, null=True, blank=True)),
                ('family_history_sibling_extra', models.CharField(max_length=30, null=True, blank=True)),
                ('family_history_children_extra', models.CharField(max_length=30, null=True, blank=True)),
                ('genetic_disease', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe9\x81\x97\xe4\xbc\xa0\xe7\x97\x85\xe5\x8f\xb2', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('genetic_disease_yes', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x96\xbe\xe7\x97\x85\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('disability_extra', models.CharField(max_length=50, null=True, verbose_name=b'', blank=True)),
                ('surroundings_kitchen_exhaust', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe5\x8e\xa8\xe6\x88\xbf\xe6\x8e\x92\xe9\xa3\x8e\xe8\xae\xbe\xe5\xa4\x87', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6cb9\u70df\u673a', b'\xe6\xb2\xb9\xe7\x83\x9f\xe6\x9c\xba'), ('\u6362\u6c14\u6247', b'\xe6\x8d\xa2\xe6\xb0\x94\xe6\x89\x87'), ('\u70df\u56f1', b'\xe7\x83\x9f\xe5\x9b\xb1')])),
                ('surroundings_fuel_type', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe7\x87\x83\xe6\x96\x99\xe7\xb1\xbb\xe5\x9e\x8b', choices=[('\u6db2\u5316\u6c14', b'\xe6\xb6\xb2\xe5\x8c\x96\xe6\xb0\x94'), ('\u7164', b'\xe7\x85\xa4'), ('\u5929\u7136\u6c14', b'\xe5\xa4\xa9\xe7\x84\xb6\xe6\xb0\x94'), ('\u6cbc\u6c14', b'\xe6\xb2\xbc\xe6\xb0\x94'), ('\u67f4\u706b', b'\xe6\x9f\xb4\xe7\x81\xab'), ('\u5176\u4ed6', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('surroundings_water', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe9\xa5\xae\xe6\xb0\xb4', choices=[('\u81ea\u6765\u6c34', b'\xe8\x87\xaa\xe6\x9d\xa5\xe6\xb0\xb4'), ('\u7ecf\u51c0\u5316\u8fc7\u6ee4\u7684\u6c34', b'\xe7\xbb\x8f\xe5\x87\x80\xe5\x8c\x96\xe8\xbf\x87\xe6\xbb\xa4\xe7\x9a\x84\xe6\xb0\xb4'), ('\u4e95\u6c34', b'\xe4\xba\x95\xe6\xb0\xb4'), ('\u6cb3\u6e56\u6c34', b'\xe6\xb2\xb3\xe6\xb9\x96\xe6\xb0\xb4'), ('\u5858\u6c34', b'\xe5\xa1\x98\xe6\xb0\xb4'), ('\u5176\u4ed6', b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('surroundings_toilet', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'\xe5\x8e\x95\xe6\x89\x80', choices=[('\u536b\u751f\u5395\u6240', b'\xe5\x8d\xab\xe7\x94\x9f\xe5\x8e\x95\xe6\x89\x80'), ('\u4e00\u683c\u6216\u4e8c\u683c\u7caa\u6c60\u5f0f', b'\xe4\xb8\x80\xe6\xa0\xbc\xe6\x88\x96\xe4\xba\x8c\xe6\xa0\xbc\xe7\xb2\xaa\xe6\xb1\xa0\xe5\xbc\x8f'), ('\u9a6c\u6876', b'\xe9\xa9\xac\xe6\xa1\xb6'), ('\u9732\u5929\u7caa\u5751', b'\xe9\x9c\xb2\xe5\xa4\xa9\xe7\xb2\xaa\xe5\x9d\x91'), ('\u7b80\u6613\u68da\u5395', b'\xe7\xae\x80\xe6\x98\x93\xe6\xa3\x9a\xe5\x8e\x95')])),
                ('surrounding_livestock_fence', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe7\xa6\xbd\xe7\x95\x9c\xe6\xa0\x8f', choices=[('\u5355\u8bbe', b'\xe5\x8d\x95\xe8\xae\xbe'), ('\u5ba4\u5185', b'\xe5\xae\xa4\xe5\x86\x85'), ('\u5ba4\u5916', b'\xe5\xae\xa4\xe5\xa4\x96')])),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('allergy_history', models.ManyToManyField(to='ehr.AllergyHistoryYesChoices', null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe8\xbf\x87\xe6\x95\x8f\xe5\x8f\xb2', blank=True)),
                ('disability', models.ManyToManyField(to='ehr.DisabilityChoices', null=True, verbose_name=b'\xe6\xae\x8b\xe7\x96\xbe\xe6\x83\x85\xe5\x86\xb5', blank=True)),
                ('disease_history', models.ManyToManyField(to='ehr.DiseaseHistoryChoices', null=True, verbose_name=b'\xe7\x96\xbe\xe7\x97\x85', blank=True)),
                ('expose_history', models.ManyToManyField(to='ehr.ExposeHistoryYesChoices', null=True, verbose_name=b'\xe6\x9a\xb4\xe9\x9c\xb2\xe5\x8f\xb2', blank=True)),
                ('family_history_children', models.ManyToManyField(related_name='children_disease', null=True, to='ehr.FamilyHistoryChoices', blank=True)),
                ('family_history_father', models.ManyToManyField(related_name='father_disease', null=True, to='ehr.FamilyHistoryChoices', blank=True)),
                ('family_history_mother', models.ManyToManyField(related_name='mother_disease', null=True, to='ehr.FamilyHistoryChoices', blank=True)),
                ('family_history_sibling', models.ManyToManyField(related_name='sibling_disease', null=True, to='ehr.FamilyHistoryChoices', blank=True)),
                ('payment_way', models.ManyToManyField(to='ehr.PaymentWayChoices', null=True, verbose_name=b'\xe5\x8c\xbb\xe7\x96\x97\xe8\xb4\xb9\xe7\x94\xa8\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f', blank=True)),
            ],
            options={
                'db_table': 'ehr_personal_info',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SymptomChoice',
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
    ]
