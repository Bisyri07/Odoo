{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base','mail'],
    'author': 'Bisyri',
    'category': 'App',
    'description': 
                    """
                        This is module is used to learn basic technical Odoo 17
                    """,
    'application': True,
    'data': [
        # security
        'security/ir.model.access.csv',    
        # email template
        'views/templates/email_templates.xml',
        # menu
        'views/menu.xml',
        # estate property CRUD form
        'views/estate_property.xml',
        # dummy data
        'data/estate.property.csv',  
        # scheduler
        'views/estate_property_scheduler.xml',
    ]
}