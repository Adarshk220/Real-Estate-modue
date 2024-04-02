from odoo import fields, models


class Estate_Property(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _rec_name = 'type'


    type = fields.Char(required=True, string="Property Type")