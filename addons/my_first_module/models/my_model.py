from odoo import models, fields

class MyFirstModel(models.Model):
    _name = 'my.first.model'
    _description = 'Model đầu tiên của tôi'

    name = fields.Char(string='Tên', required=True)
    description = fields.Text(string='Mô tả')
    active = fields.Boolean(string='Đang hoạt động', default=True)
