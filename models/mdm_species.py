from odoo import models, fields


class MDMSpecies(models.Model):
    _name = 'mdm.species'
    _rec_name = "species_name"
    _description = 'ชื่อพันธุ์ไม้'

    species_code = fields.Char(string='รหัสพันธุ์ไม้', required=False)
    species_abbr_name = fields.Char(string='ชื่อย่อพันธุ์ไม้', required=False, size=255)
    species_name = fields.Char(string='ชื่อพันธุ์ไม้', required=True, size=500)
    species_desc = fields.Text(string='คำอธิบายพันธุ์ไม้', required=False)
    species_remark = fields.Text(string="หมายเหตุพันธุ์ไม้", required=False, )
