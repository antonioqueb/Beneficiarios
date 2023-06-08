from odoo import models, fields

class Beneficiario(models.Model):
    _name = 'beneficiarios.beneficiario'
    _description = 'Beneficiario'
    _inherit = 'res.partner'

    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    rfc = fields.Char(string='RFC', required=True)
    estado_civil = fields.Selection([
        ('soltero', 'Soltero/a'),
        ('casado', 'Casado/a'),
        ('divorciado', 'Divorciado/a'),
        ('viudo', 'Viudo/a'),
    ], string='Estado Civil', required=True)
