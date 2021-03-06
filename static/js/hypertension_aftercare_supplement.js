$(function () {
    $('#hypertension_aftercare').panel({ fit: true });
    var toolbar = $('#toolbar');
    var form = $('#form');
    var panel = $('#table');
    var aftercare = undefined;

    var btn_add_5 = toolbar.find('#add_5').linkbutton({ iconCls: 'icon-add', plain: true });
    var btn_add_6 = toolbar.find('#add_6').linkbutton({ iconCls: 'icon-add', plain: true });

    var btn_save = toolbar.find('#save').linkbutton({ iconCls: 'icon-save', plain: true });
    var btn_undo = toolbar.find('#undo').linkbutton({ iconCls: 'icon-undo', plain: true });
    var btn_print = toolbar.find('#print').linkbutton({ iconCls: 'icon-print', plain: true });

    btn_undo.linkbutton('disable');
    btn_save.linkbutton('disable');

    btn_print.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.find('.print_area').printThis();
        }
    });

    btn_add_5.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/hypertension/aftercare_form/', method: 'POST',
                queryParams: { aftercare: 5 },
                onLoad: function () {}
            });
            aftercare = 'aftercare_5';
        }
        btn_add_5.linkbutton('disable');
        btn_add_6.linkbutton('disable');
        btn_undo.linkbutton('enable');
        btn_save.linkbutton('enable');
        btn_print.linkbutton('disable');
    });

    btn_add_6.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/hypertension/aftercare_form/', method: 'POST',
                queryParams: { aftercare: 6 },
                onLoad: function () {}
            });
            aftercare = 'aftercare_6';
        }
        btn_add_5.linkbutton('disable');
        btn_add_6.linkbutton('disable');
        btn_undo.linkbutton('enable');
        btn_save.linkbutton('enable');
        btn_print.linkbutton('disable');
    });

    btn_save.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            form.form('submit', {
                url: '/hypertension/aftercare_submit/', method: 'POST',
                onSubmit: function (param) {
                    if (!form.find('input[name=visit_way]').is(":checked")) {
                        $.messager.alert('提示', '请选择随访方式', 'info');
                        return false;
                    }
                    if (!form.find('input[name=symptom]').is(":checked")) {
                        $.messager.alert('提示', '请选择症状', 'info');
                        return false;
                    }
                    if (!form.find('input[name=life_style_guide_salt]').is(":checked")) {
                        $.messager.alert('提示', '请选择摄盐情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=life_style_guide_salt_next]').is(":checked")) {
                        $.messager.alert('提示', '请选择摄盐情况下次目标', 'info');
                        return false;
                    }
                    if (!form.find('input[name=life_style_guide_mentality]').is(":checked")) {
                        $.messager.alert('提示', '请选择心理调整情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=life_style_guide_medical_compliance]').is(":checked")) {
                        $.messager.alert('提示', '请选择遵医行为情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=take_medicine_compliance]').is(":checked")) {
                        $.messager.alert('提示', '请选择服药依从性情况', 'info');
                        return false;
                    }
                    if (!form.find('input[name=medicine_untoward_effect]').is(":checked")) {
                        $.messager.alert('提示', '请选择有无药物不良反应', 'info');
                        return false;
                    }
                    if (!form.find('input[name=visit_classification]').is(":checked")) {
                        $.messager.alert('提示', '请选择此次随访分类', 'info');
                        return false;
                    }

                    if (form.form('validate')) {
                        param.csrfmiddlewaretoken = $.cookie('csrftoken');
                        param.aftercare = aftercare;
                        return true;
                    }
                    else {
                        return false;
                    }
                },
                success: function (data) {
                    var data_obj = eval('(' + data + ')');
                    if (data_obj.success) {
                        $.messager.show({title: '提示', msg: '随访记录保存成功', timeout: 1000});
                    } else {
                        $.messager.alert('提示', '随访记录保存失败', 'warning');
                    }
                    panel.panel({
                        href: '/hypertension/aftercare_supplement_review/',
                        onLoad: function () {
                            if ($.trim(panel.find('.aftercare_5').html())) {
                                btn_add_5.linkbutton('disable');
                            } else {
                                btn_add_5.linkbutton('enable');
                            }
                            if ($.trim(panel.find('.aftercare_6').html())) {
                                btn_add_6.linkbutton('disable');
                            } else {
                                btn_add_6.linkbutton('enable');
                            }
                        }
                    });
                    btn_undo.linkbutton('disable');
                    btn_save.linkbutton('disable');
                    btn_print.linkbutton('enable');
                }
            });
        }
    });

    btn_undo.bind('click', function () {
        if ($(this).linkbutton('options').disabled == false) {
            panel.panel({
                href: '/hypertension/aftercare_supplement_review/',
                onLoad: function () {
                    if ($.trim(panel.find('.aftercare_5').html())) {
                        btn_add_5.linkbutton('disable');
                    } else {
                        btn_add_5.linkbutton('enable');
                    }
                    if ($.trim(panel.find('.aftercare_6').html())) {
                        btn_add_6.linkbutton('disable');
                    } else {
                        btn_add_6.linkbutton('enable');
                    }
                }
            });
            btn_save.linkbutton('disable');
            btn_undo.linkbutton('disable');
            btn_print.linkbutton('enable');
        }
    });

    panel.panel({
        href: '/hypertension/aftercare_supplement_review/',
        onLoad: function () {
            if ($.trim(panel.find('.aftercare_5').html())) {
                btn_add_5.linkbutton('disable');
            }
            if ($.trim(panel.find('.aftercare_6').html())) {
                btn_add_6.linkbutton('disable');
            }
        }
    });
});