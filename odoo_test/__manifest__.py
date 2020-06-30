{

    'name': "Odoo Test",

    'summary': """Odoo Test Demo""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Akorede Fodilu Olawale",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/access.csv',
    #    'views/odoo_test.xml',
    ],
    # only loaded in demonstration mode
     
    'installable':True,
    'application':True,
    'auto_install':False
}
