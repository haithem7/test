# -*- coding: utf-8 -*-
{
    'name': "sale_restrict",

    'summary': """
        Vérifier la redondance""",

    'description': """
Vérifier la redondance    """,

    'author': "Haithem",
    'website': "https://www.haithemdahech.com",

    'category': 'sale',
    'version': '16.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
}
