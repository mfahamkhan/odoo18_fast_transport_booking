# Transport Booking Fast

Odoo custom module for managing vehicles, routes, and transport bookings.

## Structure
- `models/`: Core models for bookings (`booking.py`), routes (`route.py`), and vehicles (`vehicle.py`).
- `views/`: Menu and UI definitions (`menu.xml`).
- `security/`: Access control rules (`ir.model.access.csv`).
- `static/`: Frontend assets (`src/js`, `src/xml`) and module icon (`description/logoo1.png`).

## Setup
1. Place `transport_booking_fast` inside a directory listed in your Odoo `addons_path`.
2. Restart the Odoo service.
3. Go to **Apps**, update the apps list, and install **Transport Booking Fast**.
