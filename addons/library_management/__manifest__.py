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
        'views/library_member_views.xml',
        'views/library_borrowing_views.xml',
        'data/library_demo.xml',
    ],
    'installable': True,
    'application': True,
}