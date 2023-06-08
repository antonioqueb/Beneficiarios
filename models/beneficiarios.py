from odoo import models, fields

class Beneficiario(models.Model):
    _description = 'Beneficiario'
    _inherit = 'res.partner'

    