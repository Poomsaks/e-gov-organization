from odoo import models, fields


class MDMPositionGroup(models.Model):
    _name = 'mdm.position.group'
    _description = 'MDMPositionGroup'
    _rec_name = 'name'

    name = fields.Char(string='ชื่อหมวด', required=False)

