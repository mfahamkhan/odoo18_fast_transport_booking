from odoo import models, fields


class Route(models.Model):
    _name = 'transport.route'
    _description = 'Transport Route'

    name = fields.Char(required=True)
    from_location = fields.Char(required=True)
    to_location = fields.Char(required=True)
    available_seats = fields.Integer(compute='_compute_available_seats')

    def _compute_available_seats(self):
        for route in self:
            bookings = self.env['transport.booking'].search([('route_id', '=', route.id)])
            total_booked = sum(bookings.mapped('seats'))
            # Assuming one vehicle per route for simplicity; adjust if needed
            vehicle = self.env['transport.vehicle'].search([('id', 'in', bookings.mapped('vehicle_id').ids)], limit=1)
            route.available_seats = vehicle.capacity - total_booked if vehicle else 0
