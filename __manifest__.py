# -*- coding: utf-8 -*- 


{
    'name': 'Link Sale,Manufacturing Requests and Prepress management modules',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Sale/Prepress/Manufacturing',
    'demo': [],
    'depends': ['sale_mrp_production_request','mrp_production_request_prepress_management','sale_prepress_management'],
    'data': [
        'views/res_config_settings_views.xml',
        'wizard/production_requests_create_views.xml'
    ],
    'license': 'LGPL-3',
}
