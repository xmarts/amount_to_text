# -*- coding: utf-8 -*-
{
    'name': "amount_text",
    'summary': """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """ Long description of module's purpose""",
    'author': "Xmarts",
    'contributors': "victoralonso@xmarts.com, javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
