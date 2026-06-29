from odoo import models, fields

class Department(models.Model):
    _name = 'hr.simple.department'
    _description = 'Phòng ban'

    name = fields.Char(string='Department Name', required=True)
    active = fields.Boolean(default=True)
