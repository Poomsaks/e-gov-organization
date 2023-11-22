from odoo import models, fields


class CustomResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'CustomResPartner'

    position_id = fields.Many2one(
        comodel_name='mdm.position',
        string='ตำแหน่ง',
        required=False)
    village_id = fields.Many2one(
        comodel_name='mdm.village',
        string='หมู่บ้าน',
        required=False)
