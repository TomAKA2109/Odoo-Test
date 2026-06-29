{
    'name': 'HR Simple',
    'version': '1.0',
    'summary': 'Quản lý nhân viên đơn giản',
    'category': 'Human Resources',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/department_views.xml',
        'views/position_views.xml',
        'views/employee_views.xml',
    ],
    'assets': {
    'web.assets_backend': [
        'hr_simple/static/src/components/salary_widget.xml',
        'hr_simple/static/src/components/salary_widget.js',
        'hr_simple/static/src/components/department_badge_widget.xml',
        'hr_simple/static/src/components/department_badge_widget.js',
    ],
},
    'installable': True,
    'auto_install': False,
}