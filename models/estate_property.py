from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real Estate"

    name = fields.Char(required=True)
    salesman_id = fields.Many2one("res.users", "Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one("res.partner", "Buyer", copy=False)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False,default=fields.date.today()+relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="select one for garden orientation field")
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=[('new', 'New'), ('received', 'Offer Received'), ('accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],required=True,default='new',copy=False)
    property_type_id = fields.Many2one("estate.property.type", "Property Type")
    property_tag_ids = fields.Many2many("estate.property.tag",string="Property Tag")
    partner_ids = fields.One2many("estate.property.offer", "partner_id", string="Property Tag")
    property_ids = fields.One2many("estate.property.offer", "property_id", string="Property Tag")