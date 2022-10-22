# -*- coding: utf-8 -*-
import string
from importlib.resources import _
from odoo.exceptions import MissingError, UserError, ValidationError, AccessError
from fields.extras import ValidationError
from odoo import models, fields, api


class installment(models.Model):
    _name = 'installment.installment'
    _description = 'Handling Customers'
    name = fields.Char(string='Name', store=True)
    reference = fields.Char(string='Reference', store=True)
    date_today = fields.Date(string='Date', default=fields.Date.today)
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('paid', 'Paid')],
                                string="State", default='open')
    _customers = fields.Many2one('res.partner', ondelete='cascade', index='True', string='Customers', required=True)
    _journal = fields.Many2one('res.partner', ondelete='cascade', index='True', string='Journal', required=True)
    _account = fields.Many2one('res.partner', ondelete='cascade', index='True', string='Account', required=True)
    analytic_account = fields.Many2one('res.users', ondelete='restrict', index='True', string='Analytic account')
    analytic_tags = fields.Many2many('res.partner', ondelete='restrict', index='True', string='Analytic Tags')
    _amount = fields.Float(string='Amount', required=True, index=True)
    note = fields.Text(string='Notes', store=True)
    blank = fields.Char(string="check")
    customers_count = fields.Integer(
        string="Customers Count", compute='_get_customers_count', store=True)
    color = fields.Integer()

    @api.onchange('_amount')
    def check_positive(self):
        x = self._amount
        if x < 0:
            raise ValidationError(_('Amount must be positive'))

    @api.onchange('_customers')
    def _get_customers_count(self):
        for r in self:
            r.customers_count = len(r._customers)

    def action_test1(self):
        print("Button Clicked !!!!!!!!!!!!!!!!!!!!!!!1")
    def action_test2(self):
        print("Button Clicked !!!!!!!!!!!!!!!!!!!!!!!1")
    def action_test3(self):
        print("Button Clicked !!!!!!!!!!!!!!!!!!!!!!!1")
    def action_invoice(self):
        print("Test")




