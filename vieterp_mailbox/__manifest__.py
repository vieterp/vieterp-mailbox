# -*- coding: utf-8 -*-
{
    'name': "VietERP Mailbox",

    'summary': """
        Simple Odoo mailbox""",

    'description': """
        - Sent email from odoo
        - Receive email from odoo
        - Compose email from odoo
        - Choose odoo email template
    """,

    'author': "VietERP / Sang",
    'website': "http://www.vieterp.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'VietERP',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mail_mail_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}