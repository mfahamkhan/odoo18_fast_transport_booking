from odoo import models, fields


class Vehicle(models.Model):
    _name = 'transport.vehicle'
    _description = 'Transport Vehicle'

    name = fields.Char(required=True)
    capacity = fields.Integer(required=True)
    fleet_vehicle_id = fields.Many2one('fleet.vehicle', string='Fleet Vehicle', required=True)
