from odoo import models, fields

class MyFirstModel(models.Model):
    _name = 'my.first.model'
    _description = 'My first module'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
