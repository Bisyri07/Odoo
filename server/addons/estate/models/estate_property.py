from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    # sql constraints for validation error.
    _sql_constraints = [
        (
            'unique_name',
            'UNIQUE(name)',
            'The name must be unique.'
        ),
        (
            'check_percentage',
            'CHECK(facades >= 0 AND facades <= 10)',
            'The number input should be between 0 and 10.'
        ),      
    ]

    # python constraints for validation error.
    @api.constrains('selling_price', 'expected_price')
    def _checking_price(self):
        for record in self:
            if record.selling_price <= 0:
                raise  ValidationError("The selling price must be positive value.")
            if record.expected_price <= record.selling_price:
                raise ValidationError("The expected value must higher than selling price")

    # computed field using python decorator
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for a in self:
            a.total_area = a.living_area + a.garden_area

    # create decorator for condition
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "N"
        else:
            self.garden_area = 0
            self.garden_orientation = False
            

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

    user_id = fields.Many2one("res.users", 
                              string="salesman", 
                              default=lambda self: self.env.user)
    
    buyer_id = fields.Many2one("res.users",
                               string="buyer", 
                               readonly=True,
                               copy=False)
    
    total_area = fields.Integer(readonly=True,
                                compute="_compute_total_area")
















