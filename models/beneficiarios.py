from odoo import models, fields

class Beneficiario(models.Model):
    _description = 'Beneficiario'
    _inherit = 'res.partner'

    is_beneficiary = fields.Boolean(string='Is Beneficiary', default=True)
    beneficiary_ids = fields.Many2many(
        'res.partner', 
        relation='partner_beneficiary_rel',  # nombre de la tabla de relación
        column1='partner_id',  # nombre de la columna de la tabla principal
        column2='beneficiary_id',  # nombre de la columna de la tabla relacionada
        string='Beneficiaries'
    )
