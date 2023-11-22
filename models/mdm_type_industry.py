from odoo import models, fields


class MDMTypeIndustry(models.Model):
    _name = 'mdm.type.industry'
    _description = 'ประเภทอุตสาหกรรม'
    _rec_name = 'name'

    name = fields.Char(string="ประเภทอุตสาหกรรม")
