from odoo import models, fields, _


class MDMEconomy(models.Model):
    _name = 'mdm.economy'
    _rec_name = 'village_name'
    _description = 'เศรษฐกิจ'

    village_id = fields.Many2one(comodel_name='mdm.village', string='หมู่บ้าน', required=False)
    village_name = fields.Char(string=_('หมู่บ้าน'), required=False, related='village_id.name')
    agriculture_ids = fields.One2many(comodel_name='mdm.agriculture', inverse_name='economy_id',
                                      string='การเกษตร', required=False)
    fishing_ids = fields.One2many(comodel_name='mdm.fishing', inverse_name='economy_id',
                                  string='การประมง', required=False)
    livestock_ids = fields.One2many(comodel_name='mdm.livestock', inverse_name='economy_id',
                                    string='ปศุสัตว์', required=False)
    service_ids = fields.One2many(comodel_name='mdm.service', inverse_name='economy_id',
                                  string='การบริการ', required=False)
    travel_ids = fields.One2many(comodel_name='mdm.travel', inverse_name='economy_id',
                                 string='การท่องเที่ยว', required=False)
    industry_ids = fields.One2many(comodel_name='mdm.industry', inverse_name='economy_id',
                                   string='อุตสาหกรรม', required=False)
    labor_ids = fields.One2many(comodel_name='mdm.labor', inverse_name='economy_id',
                                string='แรงงาน', required=False)


class MDMWater(models.Model):
    _name = 'mdm.agriculture'
    _rec_name = "type_agriculture_name"
    _description = "การเกษตร"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    type_agriculture_id = fields.Many2one(comodel_name='mdm.type.agriculture', string='ประเภทการทำการเกษตร',
                                          required=False)
    type_agriculture_name = fields.Char(string=_('ประเภทการทำการเกษตร'), required=False,
                                        related='type_agriculture_id.name')


class MDMFishing(models.Model):
    _name = 'mdm.fishing'
    _rec_name = "water"
    _description = "การประมง"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    water = fields.Selection(string="แหล่งน้ำ",
                             selection=[('1', 'ลำห้วย'),
                                        ('2', 'คูคลอง'),
                                        ('3', 'หนองบึง'),
                                        ('4', 'บ่อน้ำ'),
                                        ('5', 'สระน้ำ'),
                                        ('6', 'สาธารณประโยชน์')],
                             required=False, )
    trade = fields.Selection(string="การประมง",
                             selection=[('1', 'เพื่อบริโภค'),
                                        ('2', 'เพื่อค้าขาย'), ],
                             required=False, )


class MDMLivestock(models.Model):
    _name = 'mdm.livestock'
    _rec_name = "type_livestock_name"
    _description = "ปศุสัตว์"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    type_livestock_id = fields.Many2one(comodel_name='mdm.type.livestock', string='ประเภทปศุสัตว์',
                                        required=False)
    type_livestock_name = fields.Char(string=_('ประเภทปศุสัตว์'), required=False,
                                      related='type_livestock_id.name')


class MDMService(models.Model):
    _name = 'mdm.service'
    _rec_name = "type_service_name"
    _description = "การบริการ"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    type_service_id = fields.Many2one(comodel_name='mdm.type.service', string='ประเภทการบริการ',
                                      required=False)
    type_service_name = fields.Char(string=_('ประเภทการบริการ'), required=False,
                                    related='type_service_id.name')


class MDMTravel(models.Model):
    _name = 'mdm.travel'
    _rec_name = "name"
    _description = "การท่องเที่ยว"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    name = fields.Char(string='การท่องเที่ยว', required=False)


class MDMIndustry(models.Model):
    _name = 'mdm.industry'
    _rec_name = "type_industry_name"
    _description = "อุตสาหกรรม"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    type_industry_id = fields.Many2one(comodel_name='mdm.type.industry', string='ประเภทอุตสาหกรรม',
                                       required=False)
    type_industry_name = fields.Char(string=_('ประเภทอุตสาหกรรม'), required=False,
                                     related='type_industry_id.name')
    value = fields.Char(string='จำนวน', required=False, size=3)


class MDMLabor(models.Model):
    _name = 'mdm.labor'
    _rec_name = "type_labor_name"
    _description = "แรงงาน"

    economy_id = fields.Many2one('mdm.economy', string='รหัสเศรษฐกิจ', required=False, ondelete='cascade')
    type_labor_id = fields.Many2one(comodel_name='mdm.type.labor', string='ประเภทแรงงาน',
                                    required=False)
    type_labor_name = fields.Char(string=_('ประเภทแรงงาน'), required=False,
                                  related='type_labor_id.name')
    value = fields.Char(string='จำนวน', required=False, size=3)
