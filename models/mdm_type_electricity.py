from odoo import models, fields


class MDMTypeElectricity(models.Model):
    _name = 'mdm.type.electricity'
    _description = 'ประเภทไฟฟ้า'
    _rec_name = 'name'

    name = fields.Char(string='ประเภทไฟฟ้า', required=False)

