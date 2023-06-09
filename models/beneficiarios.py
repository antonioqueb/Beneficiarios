from odoo import models, fields, api

class Beneficiario(models.Model):
    _description = 'Beneficiario'
    _inherit = 'res.partner'

    is_beneficiary = fields.Boolean(string='Is Beneficiary', default=False)
    beneficiary_ids = fields.Many2many(
        'res.partner', 
        relation='partner_beneficiary_rel',  # nombre de la tabla de relación
        column1='partner_id',  # nombre de la columna de la tabla principal
        column2='beneficiary_id',  # nombre de la columna de la tabla relacionada
        string='Beneficiaries'
    )
    
    @api.model
    def create(self, vals):
        if 'is_beneficiary' not in vals and self.env.context.get('from_beneficiary'):
            vals['is_beneficiary'] = True
        vals['is_company'] = False  # forzar a que siempre sea una persona
    
        return super(Beneficiario, self).create(vals)
