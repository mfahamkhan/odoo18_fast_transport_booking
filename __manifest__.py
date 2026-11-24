{
    'name': 'Transport Booking Fast',
    'version': '18.0.1.0.0',
    'category': 'Operations',
    'summary': 'High-speed transport booking system (POS-style)',
    'author': 'faham-khan',
    'depends': ['base', 'web', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'transport_booking_fast/static/src/js/booking_screen.js',
            'transport_booking_fast/static/src/xml/booking_screen.xml',
        ],
    },
    'icon': '/transport_booking_fast/static/description/logoo1.png',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
