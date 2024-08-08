# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class learn_customization(models.Model):
#     _name = 'learn_customization.learn_customization'
#     _description = 'learn_customization.learn_customization'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class EstatePropertyTagInheritance(models.Model):
    _inherit = "estate.property.tag"

    priority = fields.Integer(string="Tag Priority", default=0 )
    # color = fields.Integer(string="Color Index Updated field", required=True) # ga bisa di ganti disini

    # def create(self):
    # 	# put your codes here
    #     return super().create()

class SalesOrderInherited(models.Model):
    _inherit = "sale.order"

    client_doc_number = fields.Char(string="SO Client Number")














