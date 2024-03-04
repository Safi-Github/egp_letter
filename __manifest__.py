# -*- coding: utf-8 -*-
{

    "name": "EGP Letter Management",
    "version": "17.0.1.0.0",
    "summary": "EGP Letter Management Module",
    "category": "Human Resource",
    "description": "",
    "sequence": -100,
    "depends": ['base', 'mail', 'hr'],
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/egp_letter_inbox_wizard.xml',
        'views/main_menus.xml',
        'views/egp_letter.xml',
    ],
    "author": "MCIT_EGP_Team",
    "website": "https://mcit.gov.af/",
    "installable": True,
    "application": True,
    'assets': {
        'web.assets_backend': [
            'egp_letter/static/src/custom_css.css',
        ],
    },
    "auto_install": False,
    "license": 'OPL-1',
}
