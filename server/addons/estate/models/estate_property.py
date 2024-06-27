from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"


    name = fields.Char(string="name", required=True)
    description = fields.Text(default="You can change this description")
    postcode = fields.Char()
    date_availability = fields.Date(dafault=fields.Datetime.now)
    expected_price = fields.Float()
    selling_price = fields.Float(default=100000000)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [
            ("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")
        ],
        string = "Garden Orientation",
    )
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)