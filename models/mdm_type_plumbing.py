from odoo import models, fields


class MDMTypePlumbing(models.Model):
    _name = 'mdm.type.plumbing'
    _description = 'ประเภทน้ำประปา'
    _rec_name = 'name'

    name = fields.Char(string='ประเภทน้ำประปา', required=False)

