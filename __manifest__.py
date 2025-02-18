{
    'name': 'Material Management',
    'version': '1.0',
    'summary': 'Manajemen Material dan Supplier',
    'description': 'Modul untuk mengelola material dan supplier.',
    'author': 'Khoirul Anam',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/supplier_views.xml',
    ],
    'installable': True,
    'application': True,
}
