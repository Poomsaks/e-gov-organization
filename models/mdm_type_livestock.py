from odoo import models, fields


class MDMTypeLivestock(models.Model):
    _name = 'mdm.type.livestock'
    _description = 'ประเภทปศุสัตว์'
    _rec_name = 'name'

    name = fields.Char(string="ปศุสัตว์")
