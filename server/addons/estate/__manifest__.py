{
    'name': 'Estate',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Bisyri',
    'category': 'App',
    'description': 
                    """
                        This is module is used to learn basic technical Odoo 17
                    """,
    'application': True,
    'data': [
        'security/ir.model.access.csv',    
        'views/menu.xml',
        'views/estate_property.xml',
        'data/estate.property.csv'      # dummy data
    ]
}