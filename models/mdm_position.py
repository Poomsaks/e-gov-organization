from odoo import models, fields


class MDMPosition(models.Model):
    _name = 'mdm.position'
    _description = 'MDMPosition'
    _rec_name = 'name'

    name = fields.Char(string='ชื่อ', required=False)
    position_group = fields.Many2one('mdm.position.group', string='หมวดตำแหน่ง', required=False, ondelete='cascade')
