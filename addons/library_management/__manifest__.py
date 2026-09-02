{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books, members, and borrowing',
    'description': 'A simple library management system built to learn Odoo.',
    'author': 'Abenet Tesfaye Haile',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'installable': True,
    'application': True,
}