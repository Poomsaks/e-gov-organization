from odoo import models, fields


class MDMTypePublic(models.Model):
    _name = 'mdm.type.public'
    _description = 'พื้นที่สาธารณะประโยขน์'
    _rec_name = 'name'

    name = fields.Char(string='ชื่อประเภทพื้นที่สาธารณะประโยขน์', required=False)

