# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from management import views


urlpatterns = patterns('',
    #url(r'^index/$', views.index, name='index'),
#
    #url(r'^user/list/$', views.user_list, name='user_list'),
    #url(r'^user/add/$', views.user_add, name='user_add'),
    #url(r'^user/new/$', views.user_new, name='user_new'),
    #url(r'^user/del/(\d+)/$', views.user_del),
    #url(r'^user/edit/(\d+)/$', views.user_edit),
    #url(r'^user/update/$', views.user_update, name='user_update'),
    #url(r'^user/authorize/(\d+)/$', views.user_authorize),
    #url(r'^user/authorization/update/$', views.user_authorization_update,
    #    name='user_authorization_update'),
#
    #url(r'^role/list/$', views.role_list, name='role_list'),
    #url(r'^role/add/$', views.role_add, name='role_add'),
    #url(r'^role/new/$', views.role_new, name='role_new'),
    #url(r'^role/del/(\d+)/$', views.role_del),
    #url(r'^role/edit/(\d+)/$', views.role_edit),
    #url(r'^role/update/$', views.role_update, name='role_update'),
    #url(r'^role/authorize/(\d+)/$', views.role_authorize),
    #url(r'^role/authorization/update/$', views.role_authorization_update,
    #    name='role_authorization_update'),
#
    #url(r'^town_clinic/list/$', views.town_clinic_list, name='town_clinic_list'),
    #url(r'^town_clinic/add/$', views.town_clinic_add, name='town_clinic_add'),
    #url(r'^town_clinic/new/$', views.town_clinic_new, name='town_clinic_new'),
    #url(r'^town_clinic/del/(\d+)/$', views.town_clinic_del),
    #url(r'^town_clinic/edit/(\d+)/$', views.town_clinic_edit),
    #url(r'^town_clinic/update/$', views.town_clinic_update, name='town_clinic_update'),
#
    #url(r'^village_clinic/list/$', views.village_clinic_list, name='village_clinic_list'),
    #url(r'^village_clinic/add/$', views.village_clinic_add, name='village_clinic_add'),
    #url(r'^village_clinic/new/$', views.village_clinic_new, name='village_clinic_new'),
    #url(r'^village_clinic/del/(\d+)/$', views.village_clinic_del),
    #url(r'^village_clinic/edit/(\d+)/$', views.village_clinic_edit),
    #url(r'^village_clinic/update/$', views.village_clinic_update, name='village_clinic_update'),
#
    #url(r'^resident/list/$', views.resident_list, name='resident_list'),
    #url(r'^resident/add/$', views.resident_add, name='resident_add'),
    #url(r'^resident/del/(\d+)/$', views.resident_del),
    #url(r'^resident/edit/(\d+)/$', views.resident_edit),
    #url(r'^resident/update/$', views.resident_update, name='resident_update'),
#
    #url(r'^service_type/list/$', views.service_type_list, name='service_type_list'),
    #url(r'^service_type/add/$', views.service_type_add, name='service_type_add'),
    #url(r'^service_type/new/$', views.service_type_new, name='service_type_new'),
    #url(r'^service_type/del/(\d+)/$', views.service_type_del),
    #url(r'^service_type/edit/(\d+)/$', views.service_type_edit),
    #url(r'^service_type/update/$', views.service_type_update, name='service_type_update'),
    #url(r'^service_item/list/$', views.service_item_list, name='service_item_list'),
    #url(r'^service_item/add/$', views.service_item_add, name='service_item_add'),
    #url(r'^service_item/new/$', views.service_item_new, name='service_item_new'),
    #url(r'^service_item/del/(\d+)/$', views.service_item_del),
    #url(r'^service_item/edit/(\d+)/$', views.service_item_edit),
    #url(r'^service_item/update/$', views.service_item_update, name='service_item_update'),
    #url(r'^special/hypertension/$', views.special_hypertension, name='special_hypertension'),
    #url(r'^special/hypertension/add/$', views.hypertension_add, name='hypertension_add'),
    #url(r'^special/diabetes/$', views.special_diabetes, name='special_diabetes'),
    #url(r'^special/psychiatric/$', views.special_psychiatric, name='special_psychiatric'),
    #url(r'^special/pregnant/$', views.special_pregnant, name='special_pregnant'),
    #url(r'^special/child/$', views.special_child, name='special_child'),
    #url(r'^special/old/$', views.special_old, name='special_old'),
#
    #url(r'^statistics/records/$', views.statistics_records, name='statistics_records'),
    #url(r'^statistics/payment/$', views.statistics_payment, name='statistics_payment'),
    #url(r'^statistics/resident/$', views.statistics_resident, name='statistics_resident'),
    #url(r'^statistics/resident/record/(\d+)/$', views.statistics_record_detail, name='statistics_record_detail'),
#
    #url(r'clinic/(?P<town_clinic_id>\d+)/village_clinics/$', views.get_village_clinics, name='get_village_clinics'),
    #url(r'town/(?P<town_id>\d+)/villages/$', views.get_villages, name='get_villages'),
#
    #url(r'^userprofile_index', views.userprofile_index, name='userprofile_index'),
    #url(r'^user_profile', views.user_profile, name='user_profile'),
    #url(r'^user_password', views.user_password, name='user_password'),
    #url(r'^user_authorized_list', views.user_authorized_list, name='user_authorized_list'),
    #url(r'^user_statistics_records', views.user_statistics_records, name='user_statistics_records'),
#
    #url(r'service/(?P<type_id>\d+)/items/$', views.get_items, name='get_items'),
    #url(r'^resident_service_list', views.resident_service_list, name='resident_service_list'),
    #url(r'service/(?P<type_id>\d+)/user_statistics_items/$', views.user_statistics_get_items,
    # name='user_statistics_get_items'),
#
    ##Town_staff management
    #url(r'^town_staff_village_clinic/list/$', views.town_staff_village_clinic_list,
    # name='town_staff_village_clinic_list'),
    #url(r'^town_staff_village_clinic/add/$', views.town_staff_village_clinic_add,
    # name='town_staff_village_clinic_add'),
    #url(r'^town_staff_user/list/$', views.town_staff_user_list, name='town_staff_user_list'),
    #url(r'^town_staff_user/add/$', views.town_staff_user_add, name='town_staff_user_add'),
    #url(r'^town_staff_user/edit/(\d+)/$', views.town_staff_user_edit),
    #url(r'^town_staff_resident/list/$', views.town_staff_resident_list, name='town_staff_resident_list'),
    #url(r'^town_staff_village_clinic/edit/(\d+)/$', views.town_staff_village_clinic_edit),
    #url(r'^town_staff_resident/add/$', views.town_staff_resident_add, name='town_staff_resident_add'),
    #url(r'^town_staff_resident/edit/(\d+)/$', views.town_staff_resident_edit),
#
    #url(r'^town_staff_statistics/records/$', views.town_staff_statistics_records,
    # name='town_staff_statistics_records'),
    #url(r'^town_staff_statistics/payment/$', views.town_staff_statistics_payment,
    # name='town_staff_statistics_payment'),
    #url(r'^town_staff_statistics/resident/$', views.town_staff_statistics_resident,
    # name='town_staff_statistics_resident'),
#
    #url(r'^town_staff_special/hypertension/$', views.town_staff_special_hypertension,
    # name='town_staff_special_hypertension'),
    #url(r'^town_staff_special/diabetes/$', views.town_staff_special_diabetes, name='town_staff_special_diabetes'),
    #url(r'^town_staff_special/psychiatric/$', views.town_staff_special_psychiatric,
    # name='town_staff_special_psychiatric'),
    #url(r'^town_staff_special/child/$', views.town_staff_special_child, name='town_staff_special_child'),
    #url(r'^town_staff_special/pregnant/$', views.town_staff_special_pregnant, name='town_staff_special_pregnant'),
    #url(r'^town_staff_special/old/$', views.town_staff_special_old, name='town_staff_special_old'),
#
    #url(r'^town_staff_role/list/$', views.town_staff_role_list, name='town_staff_role_list'),
#
    #url(r'^sms_list/$', views.sms_list, name='sms_list'),
    #url(r'^sms_time/list/$', views.sms_time_list, name='sms_time_list'),
    #url(r'service/(?P<type_id>\d+)/sms_items/$', views.sms_get_items, name='sms_get_items'),
    #url(r'^sms_time/add/$', views.sms_time_add, name='sms_time_add'),
    #url(r'^sms_time/edit/(\d+)/$', views.sms_time_edit),
    #url(r'^sms_time/update/$', views.sms_time_update, name='sms_time_update'),
    #url(r'^sms_time/del/(\d+)/$', views.sms_time_del),
#
    #url(r'^special_psychiatric/patient_info_table/$', views.psychiatric_info_table, name='psychiatric_info_table'),
    #url(r'^special_psychiatric/patient_info_table_detail/$', views.psychiatric_info_table_detail,
    #    name='psychiatric_info_table_detail'),
#
    #url(r'^town_clinics_statement', views.town_clinics_statement, name='town_clinics_statement'),
    #url(r'^village_clinics_statement/(\d+)/$', views.village_clinics_statement, name='village_clinics_statement'),
    #url(r'^doctors_statement/(\d+)/$', views.doctors_statement, name='doctors_statement'),
    #url(r'^doctor_work_records/(\d+)/$', views.doctor_work_records, name='doctor_work_records'),
    #url(r'^resident_records/(\d+)/(\d+)/$', views.resident_records, name='resident_records'),
#
    #url(r'^service_details/(.+)/(.+)/(.+)/(\d+)/$', views.service_details, name='service_details'),
    #url(r'^service_details/(.+)/(\d+)/$', views.service_details, name='service_details'),
    #url(r'^resident_records_details/(\d+)/(\d+)/$', views.resident_records_details, name='resident_records_details'),

    #url(r'^resident_records_details/(\d+)/(\d+)/$', views.resident_records_details, name='resident_records_details'),

    url(r'^get_towns/$', views.town_options, name='town_options'),
    url(r'^get_town_villages/(?P<town_id>\d+)/$', views.town_village_options, name='town_village_options'),
    url(r'^get_town_villages_edit/$', views.town_name_village_options, name='town_village_options'),

    url(r'^get_town_clinics/$', views.town_clinic_options, name='town_clinic_options'),
    url(r'^get_town_clinic_edit/$', views.town_clinic_options, name='get_town_clinic_edit'),

    #url(r'^get_towns_edit/$', views.get_towns_edit, name='get_tonws_edit'),
    #url(r'^get_town_villages_edit/(?P<town_id>\d+)/$', views.town_village_options, name='town_village_options'),
    url(r'^resident_add_test/$', views.resident_add_test, name='resident_add_test'),
    url(r'^resident_update_test/$', views.resident_update_test, name='resident_add_test'),
    url(r'^resident_del_test/$', views.resident_del_test, name='resident_del_test'),
    url(r'^resident_query_test/$', views.resident_query_test, name='resident_query_test'),
    url(r'^resident_query_list/$', views.resident_query_list, name='resident_query_list'),
    url(r'^admin_nav/$', views.admin_nav, name='admin_nav'),
    url(r'^residents/$', views.residents_page, name='residents_page'),
    url(r'^town_clinics/$', views.town_clinics, name='town_clinics'),
    url(r'^town_clinic_list_new/$', views.town_clinic_list_new, name='town_clinic_list_new'),
    url(r'^village_clinics/$', views.village_clinics_page, name='village_clinics_page'),
    url(r'^village_clinic_list_new/$', views.village_clinic_list_new, name='village_clinic_list_new'),

    url(r'^village_clinic_add_test/$', views.village_clinic_add_test, name='village_clinic_add_test'),
    url(r'^village_clinic_del_test/$', views.village_clinic_del_test, name='village_clinic_del_test'),
    url(r'^village_clinic_update_test/$', views.village_clinic_update_test, name='village_clinic_update_test'),
    url(r'^users/$', views.users_page, name='users_page'),
    url(r'^user_query_list/$', views.user_query_list, name='user_query_list'),
    url(r'^get_town_village_clinics/(?P<town_clinic_id>\d+)/$', views.get_town_village_clinics,
        name='get_town_village_clinics'),
    url(r'^get_town_clinics_edit/$', views.get_town_clinics_edit, name='get_town_clinics_edit'),
    url(r'^get_town_village_clinics_edit/$', views.get_town_village_clinics_edit, name='get_town_village_clinics_edit'),
    url(r'^get_roles/$', views.get_roles, name='get_roles'),
    url(r'^user_add_test/$', views.user_add_test, name='user_add_test'),
    url(r'^user_del_test/$', views.user_del_test, name='user_del_test'),

    url(r'^service_types/$', views.service_types_page, name='service_types_page'),
    url(r'^service_type_list_new/$', views.service_type_list_new, name='service_type_list_new'),

    url(r'^service_type_options/$', views.service_type_options, name='service_type_options'),
    url(r'^service_item_list_new/$', views.service_item_list_new, name='service_item_list_new'),
    url(r'^service_items/$', views.service_items_page, name='service_items_page'),
    url(r'^service_item_add_test/$', views.service_item_add_test, name='service_item_add_test'),
    url(r'^service_item_del_test/$', views.service_item_del_test, name='service_item_del_test'),
    url(r'^service_item_update_test/$', views.service_item_update_test, name='service_item_update_test'),

    url(r'^records/$', views.records_page, name='records_page'),
    url(r'^record_list_new/$', views.record_list_new, name='record_list_new'),

    url(r'^service_item_options/$', views.service_item_options, name='service_item_options'),
    url(r'^town_clinic_options/$', views.town_clinic_options, name='town_clinic_options'),
    url(r'^village_clinic_options/$', views.village_clinic_options, name='village_clinic_options'),
    url(r'^payment/$', views.payment_page, name='payment_page'),
    url(r'^payment_list_new/$', views.payment_list_new, name='payment_list_new'),

    url(r'^roles/$', views.roles_page, name='roles_page'),
    url(r'^role_list_new/$', views.role_list_new, name='role_list_new'),
    url(r'^get_role_authorize/$', views.get_role_authorize, name='get_role_authorize'),
    url(r'^role_authorize/$', views.role_authorize, name='role_authorize'),
    url(r'^role_add/$', views.role_add, name='role_add'),
    url(r'^role_del/$', views.role_del, name='role_del'),

    url(r'^sms_sent/$', views.sms_sent, name='sms_sent'),
    url(r'^sms_sent_list/$', views.sms_sent_list, name='sms_sent_list'),
    url(r'^sms_setup_page/$', views.sms_setup_page, name='sms_setup_page'),
    url(r'^sms_setup_list/$', views.sms_setup_list, name='sms_setup_list'),
    url(r'^sms_setup_add/$', views.sms_setup_add, name='sms_setup_add'),
    url(r'^sms_setup_update/$', views.sms_setup_update, name='sms_setup_update'),
    url(r'^sms_setup_del/$', views.sms_setup_del, name='sms_setup_del'),
    url(r'^resident_add_hypertension/$', views.resident_add_hypertension, name='resident_add_hypertension'),
    url(r'^resident_add_diabetes/$', views.resident_add_diabetes, name='resident_add_diabetes'),
    url(r'^resident_add_psychiatric/$', views.resident_add_psychiatric, name='resident_add_psychiatric'),
    url(r'^resident_add_pregnant/$', views.resident_add_pregnant, name='resident_add_pregnant'),

    url(r'^excel_file/$', views.excel_file, name='excel_file'),
    url(r'^graphs/$', views.graphs, name='graphs'),
    url(r'^graph_workload/$', views.graph_workload, name='graph_workload'),
    url(r'^graph_payment/$', views.graph_payment, name='graph_payment'),

    # 生成二维统计报表所需要的函数
    url(r'^workload_stat_page/$', views.workload_stat_page, name='workload_stat_page'),  # 统计首页

    url(r'^workload_town_clinics_page/$', views.workload_town_clinics_page, name='workload_town_clinics_page'),
    url(r'^workload_town_clinics_datagrid/$', views.workload_town_clinics_datagrid,
        name='workload_town_clinics_datagrid'),  # 各卫生院各服务类别工作量二维表

    url(r'^workload_village_clinics_page/(?P<town_clinic_id>\d+)/$', views.workload_village_clinics_page,
        name='workload_village_clinics_page'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表的页面
    url(r'^workload_village_clinics_datagrid/(?P<town_clinic_id>\d+)/$', views.workload_village_clinics_datagrid,
        name='workload_village_clinics_datagrid'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表

    url(r'^workload_doctors_page/(?P<clinic_id>\d+)/$', views.workload_doctors_page,
        name='workload_doctors_page'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表的页面
    url(r'^workload_doctors_datagrid/(?P<clinic_id>\d+)/$', views.workload_doctors_datagrid,
        name='workload_doctors_datagrid'),  # 获取指定乡镇卫生院下属村卫生室的工作量二维表
    # 获取指定卫生机构的所有服务记录列表的页面
    url(r'^workload_list_page/(?P<provider_id>\d+)/$', views.workload_list_page, name='workload_list_page'),
    # 获取指定卫生机构的所有服务记录列表
    url(r'^workload_list_datagrid/(?P<provider_id>\d+)/$', views.workload_list_datagrid, name='workload_list_datagrid'),

    url(r'^resident_records_page/(?P<resident_id>\d+)/$', views.resident_records_page, name='resident_records_page'),
    url(r'^resident_records_datagrid/(?P<resident_id>\d+)/$', views.resident_records_datagrid,
        name='resident_records_datagrid'),

    url(r'^payment_stat_page/$', views.payment_stat_page, name='payment_stat_page'),  # 统计首页
    url(r'^payment_town_clinics_page/$', views.payment_town_clinics_page,
        name='payment_town_clinics_page'),  # 各卫生院各服务类别支付金额二维表
    url(r'^payment_town_clinics_datagrid/$', views.payment_town_clinics_datagrid,
        name='payment_town_clinics_datagrid'),  # 各卫生院各服务类别支付金额二维表

    url(r'^payment_village_clinics_page/(?P<town_clinic_id>\d+)/$', views.payment_village_clinics_page,
        name='payment_village_clinics_page'),  # 各卫生院各服务类别支付金额二维表
    url(r'^payment_village_clinics_datagrid/(?P<town_clinic_id>\d+)/$', views.payment_village_clinics_datagrid,
        name='payment_village_clinics_datagrid'),  # 各卫生院各服务类别支付金额二维表

    url(r'^modify_apply_page/$', views.modify_apply_page, name='modify_apply_page'),
    url(r'^modify_apply_list/$', views.modify_apply_list, name='modify_apply_list'),
    url(r'^modify_apply_opinion/$', views.modify_apply_opinion, name='modify_apply_opinion'),


)