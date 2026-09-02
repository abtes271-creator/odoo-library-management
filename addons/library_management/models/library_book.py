from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    total_copies = fields.Integer(string='Total Copies', default=1)
    available_copies = fields.Integer(string='Available Copies', default=1)