from odoo import models, fields

class Beneficiario(models.Model):
    _description = 'Beneficiario'
    _inherit = 'res.partner'

    is_beneficiary = fields.Boolean(string='Is Beneficiary', default=False)
    beneficiary_ids = fields.Many2many('res.partner', string='Beneficiaries')

