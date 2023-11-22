from odoo import models, fields


class MDMTypeStreet(models.Model):
    _name = 'mdm.type.street'
    _description = 'ประเภทถนน'
    _rec_name = 'name'

    name = fields.Char(string='ประเภทถนน', required=False)

