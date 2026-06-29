from odoo import models, fields

class Employee(models.Model):
    _name = 'hr.simple.employee'
    _description = 'Nhân viên'

    name = fields.Char(string='Employee Name', required=True)
    department_id = fields.Many2one('hr.simple.department', string='Department')
    position_id = fields.Many2one('hr.simple.position', string='Position')
    salary = fields.Float(string='Salary')
    join_date = fields.Date(string='Join Date')
    active = fields.Boolean(default=True)
