from odoo import models, fields


class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _description = 'Library Borrowing'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('library.member', string='Member', required=True)
    borrow_date = fields.Date(string='Borrow Date', default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ], string='Status', default='draft')

    def action_borrow(self):
        for record in self:
            if record.book_id.available_copies <= 0:
                raise ValueError('No available copies of this book.')
            record.book_id.available_copies -= 1
            record.state = 'borrowed'

    def action_return(self):
        for record in self:
            record.book_id.available_copies += 1
            record.state = 'returned'
            record.return_date = fields.Date.today()