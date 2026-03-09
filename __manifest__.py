# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management By odoomates',
    'version': '2603.0',
    'category': 'Health',
    'summary': 'Manage patients and appointments',
    'description': """
        Hospital Management module for Odoo 18.
        - Patient management (name, age, gender, notes, image)
        - Appointment management with statusbar and priority
    """,
    'author': 'Odoo Mates',
    'website': 'https://www.odoomates.com',
    'depends': ['mail', 'base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': -100,
}
