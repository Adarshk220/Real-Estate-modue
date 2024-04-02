from odoo import fields, models


class Estate_Property_Offer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(string="Property Type")
    status = fields.Selection([("accepted","Accepted"), ("refused", "Refused")], string="Status")
    partner_id = fields.Many2one(required=True, string="Partner")
    property_id = fields.Many2one(required=True, string="Property")