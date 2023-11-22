from odoo import models, fields, _


class MDMBreed(models.Model):
    _name = 'mdm.breed'
    _rec_name = 'breed_name'

    breed_code = fields.Char(string='รหัสพันธุ์พืช', required=False)
    breed_abbr_name = fields.Char(string='ชื่อย่อพันธุ์พืช', required=False, size=255)
    breed_name = fields.Char(string='ชื่อพันธุ์พืช', required=True, size=500)
    breed_desc = fields.Text(string='คำอธิบายพันธุ์พืช', required=False)
    breed_remark = fields.Text(string="หมายเหตุพันธุ์พืช", required=False, )
