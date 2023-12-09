from odoo import models, fields


class Village(models.Model):
    _name = 'mdm.village'
    _description = 'village'
    _rec_name = 'name'

    name = fields.Char(string='ชื่อหมู่บ้าน', required=False)
    village_no = fields.Char(string='หมู่ที่', required=False, size=3)
    populace = fields.Char(string='ประชากร', required=False, size=3)
