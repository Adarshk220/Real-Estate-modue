from odoo import fields, models


class Estate_Property_Tag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _rec_name = 'tag'

    tag = fields.Char(required=True, string="Property Tags")