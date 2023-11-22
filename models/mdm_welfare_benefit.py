from odoo import models, fields, _


class MDMWelfareBenefit(models.Model):
    _name = 'mdm.welfare.benefit'
    _rec_name = 'village_name'
    _description = 'สวัสดิการ'

    village_id = fields.Many2one(comodel_name='mdm.village', string='หมู่บ้าน', required=False)
    village_name = fields.Char(string=_('หมู่บ้าน'), required=False, related='village_id.name')
    plumbing_ids = fields.One2many(comodel_name='mdm.plumbing', inverse_name='welfare_benefit_id',
                                   string='การประปา', required=False)
    electricity_ids = fields.One2many(comodel_name='mdm.electricity', inverse_name='welfare_benefit_id',
                                      string='การไฟฟ้า', required=False)
    street_ids = fields.One2many(comodel_name='mdm.street', inverse_name='welfare_benefit_id',
                                 string='คมนาคม', required=False)


class MDMPlumbing(models.Model):
    _name = 'mdm.plumbing'
    _description = 'การประปา'

    welfare_benefit_id = fields.Many2one('mdm.welfare.benefit', string='รหัสสวัสดิการ', required=False,
                                         ondelete='cascade')
    type_plumbing_id = fields.Many2one(comodel_name='mdm.type.plumbing', string='ประเภทน้ำประปา', required=False)
    plumbing_value = fields.Char(string='จำนวน', required=False, size=3)


class MDMElectricity(models.Model):
    _name = 'mdm.electricity'
    _description = 'การไฟฟ้า'

    welfare_benefit_id = fields.Many2one('mdm.welfare.benefit', string='รหัสสวัสดิการ', required=False,
                                         ondelete='cascade')
    type_electricity_id = fields.Many2one(comodel_name='mdm.type.electricity', string='ประเภทไฟฟ้า', required=False)
    electricity_value = fields.Char(string='จำนวน', required=False, size=3)


class MDMStreet(models.Model):
    _name = 'mdm.street'
    _description = 'คมนาคม'

    welfare_benefit_id = fields.Many2one('mdm.welfare.benefit', string='รหัสสวัสดิการ', required=False,
                                         ondelete='cascade')
    name = fields.Char(string='ชื่อถนน', required=False)
    type_street_id = fields.Many2one(comodel_name='mdm.type.street', string='ประเภทถนน', required=False)
    street_value = fields.Char(string='ระยะทาง', required=False)
