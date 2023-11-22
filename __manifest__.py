# -*- coding: utf-8 -*-
{
    'name': "E-Gov-Organization",
    'author': "Dev",
    'description': '',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/custom_res_partner_view.xml',
        'views/mdm_position_view.xml',
        'views/mdm_village_view.xml',
        'views/mdm_breed_view.xml',
        'views/mdm_species_view.xml',
        'views/mdm_resource_view.xml',
        'views/mdm_type_public_view.xml',
        'views/mdm_culture_view.xml',
        'views/mdm_type_agriculture_view.xml',
        'views/mdm_type_livestock_view.xml',
        'views/mdm_type_service_view.xml',
        'views/mdm_type_industry_view.xml',
        'views/mdm_type_labor_view.xml',
        'views/mdm_economy_view.xml',
        'views/mdm_society_view.xml',
        'views/mdm_type_plumbing_view.xml',
        'views/mdm_type_electricity_view.xml',
        'views/mdm_type_street_view.xml',
        'views/mdm_welfare_benefit_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/icon.png'],
}
