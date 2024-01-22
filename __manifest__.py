# -*- coding: utf-8 -*-
{

    "name": "EGP Letter Management",
    "version": "17.0.1.0.0",
    "summary": "EGP Letter Management Module",
    "category": "Human Resource",
    "description": "",
    "depends": ['base', 'mail', 'hr'],
    "data": [
        'security/ir.model.access.csv',

        'views/main_menus.xml',
        'views/egp_letter.xml',

    ],
    "author": "MCIT_EGP_Team",
    "website": "https://mcit.gov.af/",
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": 'OPL-1',
}
