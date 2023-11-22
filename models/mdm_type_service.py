from odoo import models, fields


class MDMTypeService(models.Model):
    _name = 'mdm.type.service'
    _description = 'ประเภทการบริการ'
    _rec_name = 'name'

    name = fields.Char(string='ประเภทการบริการ', required=False)

