{
    'name': 'My First Module',
    'version': '1.0',
    'summary': 'Module đầu tiên của tôi',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}