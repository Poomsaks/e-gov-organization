from odoo import models, fields


class MDMTypeLabor(models.Model):
    _name = 'mdm.type.labor'
    _description = 'ประเภทแรงงาน'
    _rec_name = 'name'

    name = fields.Char(string="ประเภทแรงงาน")
