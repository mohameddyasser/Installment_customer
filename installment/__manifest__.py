# -*- coding: utf-8 -*-
{
    'name': "Customer handling",

    'summary': """
    Module ith Odoo version 15 which handles customer installments and payments.
        """,

    'description': """
        Module ith Odoo version 15 which handles customer installments and payments.
    """,

    'author': "Mohamed Yasser",
    'website': "https://www.linkedin.com/in/mohamedd-yasser/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/view2.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
