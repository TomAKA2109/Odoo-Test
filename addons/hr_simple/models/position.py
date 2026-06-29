from odoo import models, fields

class Position(models.Model):
    _name = 'hr.simple.position'
    _description = 'Chức vụ'

    name = fields.Char(string='Position Name', required=True)
    department_id = fields.Many2one('hr.simple.department', string='Department')
