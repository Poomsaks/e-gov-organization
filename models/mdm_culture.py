from odoo import models, fields, _


class MDMCulture(models.Model):
    _name = 'mdm.culture'
    _rec_name = 'village_name'
    _description = 'ศาสนา ประเภณี วัฒนธรรม'

    village_id = fields.Many2one(comodel_name='mdm.village', string='หมู่บ้าน', required=False)
    village_name = fields.Char(string=_('หมู่บ้าน'), required=False, related='village_id.name')
    temple_ids = fields.One2many(comodel_name='mdm.temple', inverse_name='culture_id',
                                 string='วัด', required=False)
    wisdom_ids = fields.One2many(comodel_name='mdm.wisdom', inverse_name='culture_id',
                                 string='ภูมิปัญญาท้องถิ่น', required=False)
    tradition_ids = fields.One2many(comodel_name='mdm.tradition', inverse_name='culture_id',
                                    string='ประเภณี', required=False)


class MDMTemple(models.Model):
    _name = 'mdm.temple'
    _description = 'วัด'
    _rec_name = 'name'

    culture_id = fields.Many2one('mdm.culture', string='รหัสประเภณี', required=False, ondelete='cascade')
    name = fields.Char(string='ชื่อวัด', required=False)
    value = fields.Char(string='จำนวนพระ', required=False, siz=3)


class MDMWisdom(models.Model):
    _name = 'mdm.wisdom'
    _description = 'ภูมิปัญญาท้องถิ่น'
    _rec_name = 'name'

    culture_id = fields.Many2one('mdm.culture', string='รหัสประเภณี', required=False, ondelete='cascade')
    name = fields.Char(string='ภูมิปัญญาท้องถิ่น', required=False)
    language = fields.Char(string='ภาษา', required=False)


class MDMTradition(models.Model):
    _name = 'mdm.tradition'
    _description = 'ประเภณี'
    _rec_name = 'name'

    culture_id = fields.Many2one('mdm.culture', string='รหัสประเภณี', required=False, ondelete='cascade')
    name = fields.Char(string='ประเภณี', required=False)
    start_mouth = fields.Selection(string="จากเดือน",
                                   selection=[('1', 'มกราคม'),
                                              ('2', 'กุมภาพันธ์'),
                                              ('3', 'มีนาคม'),
                                              ('4', 'เมษายน'),
                                              ('5', 'พฤษภาคม'),
                                              ('6', 'มิถุนายน'),
                                              ('7', 'กรกฎาคม'),
                                              ('8', 'สิงหาคม'),
                                              ('9', 'กันยายน'),
                                              ('10', 'ตุลาคม'),
                                              ('11', 'พฤศจิกายน'),
                                              ('12', 'ธันวาคม')],
                                   required=False, default='1')
    end_mouth = fields.Selection(string="ถึงเดือน",
                                 selection=[('1', 'มกราคม'),
                                            ('2', 'กุมภาพันธ์'),
                                            ('3', 'มีนาคม'),
                                            ('4', 'เมษายน'),
                                            ('5', 'พฤษภาคม'),
                                            ('6', 'มิถุนายน'),
                                            ('7', 'กรกฎาคม'),
                                            ('8', 'สิงหาคม'),
                                            ('9', 'กันยายน'),
                                            ('10', 'ตุลาคม'),
                                            ('11', 'พฤศจิกายน'),
                                            ('12', 'ธันวาคม')],
                                 required=False, default='1')
