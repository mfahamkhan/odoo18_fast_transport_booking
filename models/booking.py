from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Booking(models.Model):
    _name = 'transport.booking'
    _description = 'Transport Booking'

    # Fixed to point to Fleet models for data fetching
    route_id = fields.Many2one('fleet.vehicle.model', required=True)
    vehicle_id = fields.Many2one('fleet.vehicle', required=True)
    booking_date = fields.Date(required=True, default=fields.Date.context_today)
    customer_name = fields.Char(required=True)
    seats = fields.Integer(required=True)
    amount = fields.Float(required=True)

    @api.model
    def create_booking(self, data):
        if not data.get('customer_name'):
            raise ValidationError("Customer name is required.")
        if data.get('seats', 0) <= 0:
            raise ValidationError("Seats must be positive.")
        if data.get('amount', 0) < 0:
            raise ValidationError("Amount cannot be negative.")

        record = self.create({
            'route_id': data['route_id'],
            'vehicle_id': data['vehicle_id'],
            'booking_date': data['booking_date'],
            'customer_name': data['customer_name'],
            'seats': data['seats'],
            'amount': data['amount'],
        })
        return {'id': record.id, 'success': True}

    @api.model
    def get_routes_data(self):
        # Fetches existing records from fleet.vehicle.model to act as routes
        routes = self.env['fleet.vehicle.model'].search([])
        return [{'id': r.id, 'name': r.name} for r in routes]

    @api.model
    def get_vehicles_data(self):
        # Fetches existing records directly from fleet.vehicle
        vehicles = self.env['fleet.vehicle'].search([])
        return [{'id': v.id, 'name': v.display_name, 'capacity': getattr(v, 'seats', 5)} for v in vehicles]