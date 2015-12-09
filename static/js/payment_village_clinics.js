$(function () {

    var panel = $('.payment_village_clinics').last();
    var town_clinic_id = panel.find('input[name=town_clinic_id]').last().val();
    var datagrid = $('.payment_village_clinics_datagrid').last();

    datagrid.datagrid({
        url: '/management/payment_village_clinics_datagrid/',
        rownumbers: true, singleSelect: true, fitColumns: true,
        columns: [[
            { field: 'id', title: '编号', hidden: true },
            { field: 'clinic', title: '卫生机构', width: 30 },
            { field: 'education', title: '健康教育', width: 20 },
            { field: 'vaccine', title: '预防接种', width: 20 },
            { field: 'child', title: '0-6岁儿童', width: 20 },
            { field: 'pregnant', title: '孕产妇', width: 20 },
            { field: 'old', title: '老年人', width: 20 },
            { field: 'hypertension', title: '高血压', width: 20 },
            { field: 'diabetes', title: '2型糖尿病', width: 20 },
            { field: 'psychiatric', title: '重性精神病', width: 20 },
            { field: 'tcm', title: '中医药', width: 20 },
            { field: 'infection', title: '传染病报告', width: 20 },
            { field: 'supervision', title: '卫生监督', width: 20 },
            { field: 'total', title: '合计', width: 20 }
        ]],
        queryParams: { town_clinic_id: town_clinic_id }
    });
});