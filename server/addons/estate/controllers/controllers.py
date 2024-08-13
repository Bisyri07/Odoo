from odoo import http

class EstateProperty(http.Controller):
    @http.route('/estate_property_menu', auth='public', methods=['GET', 'POST'])
    def estateMenu(self, **kw):
        return "This Is Estate Property Menu Page!"
    
    @http.route('/user_login', auth='user')  # disini bakal disuruh login dulu
    def login(self, **kw):
        return 'welcome to odoo'