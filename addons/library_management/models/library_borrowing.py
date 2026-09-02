from datetime import timedelta
from odoo import models, fields, api


class LibraryBorrowing(models.Model):
    _name = 'library.borrowing'
    _description = 'Library Borrowing'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    member_id = fields.Many2one('library.member', string='Member', required=True)
    borrow_date = fields.Date(string='Borrow Date', default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
    due_date = fields.Date(string='Due Date', compute='_compute_due_date', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ], string='Status', default='draft')
    is_overdue = fields.Boolean(string='Overdue', compute='_compute_fine', store=True)
    fine_amount = fields.Float(string='Fine', compute='_compute_fine', store=True)

    @api.depends('borrow_date')
    def _compute_due_date(self):
        for record in self:
            if record.borrow_date:
                record.due_date = record.borrow_date + timedelta(days=14)
            else:
                record.due_date = False

    @api.depends('due_date', 'state', 'return_date')
    def _compute_fine(self):
        today = fields.Date.today()
        for record in self:
            if record.state == 'borrowed' and record.due_date and today > record.due_date:
                days_late = (today - record.due_date).days
                record.is_overdue = True
                record.fine_amount = days_late * 5.0
            elif record.state == 'returned' and record.due_date and record.return_date and record.return_date > record.due_date:
                days_late = (record.return_date - record.due_date).days
                record.is_overdue = True
                record.fine_amount = days_late * 5.0
            else:
                record.is_overdue = False
                record.fine_amount = 0.0

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