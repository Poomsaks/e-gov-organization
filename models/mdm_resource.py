from odoo import models, fields, _


class MDMResource(models.Model):
    _name = 'mdm.resource'
    _rec_name = 'village_name'
    _description = 'ทรัพยากร'

    village_id = fields.Many2one(comodel_name='mdm.village', string='หมู่บ้าน', required=False)
    village_name = fields.Char(string=_('หมู่บ้าน'), required=False, related='village_id.name')
    water_ids = fields.One2many(comodel_name='mdm.water', inverse_name='resource_id',
                                string='ลักษณะแหล่งน้ำ', required=False)
    earth_ids = fields.One2many(comodel_name='mdm.earth', inverse_name='resource_id',
                                string='ลักษณะดิน', required=False)
    forest_ids = fields.One2many(comodel_name='mdm.forest', inverse_name='resource_id',
                                 string='ลักษณะป่าไม้', required=False)
    public_space_ids = fields.One2many(comodel_name='mdm.public.space', inverse_name='resource_id',
                                       string='สถานที่สาธารณะประโยชน์', required=False)


class MDMWater(models.Model):
    _name = 'mdm.water'
    _rec_name = "water"
    _description = "ลักษณะของแหล่งน้ำ"

    resource_id = fields.Many2one('mdm.resource', string='รหัสทรัพยากร', required=False, ondelete='cascade')
    water = fields.Selection(string="แหล่งน้ำ",
                             selection=[('1', 'แหล่งน้ำเพื่ออุปโภคบริโภค'),
                                        ('2', 'แหล่งน้ำเพื่อทำการเกษตร')],
                             required=False,
                             default='1')
    value_water = fields.Char(string=_('จำนวน'), required=False)


class MDMEarth(models.Model):
    _name = 'mdm.earth'
    _rec_name = "earth"
    _description = "ลักษณะของดิน"

    resource_id = fields.Many2one('mdm.resource', string='รหัสทรัพยากร', required=False, ondelete='cascade')
    earth = fields.Char(string=_('ลักษณะดิน'), required=False)

    breed_ids = fields.Many2many(comodel_name='mdm.breed', string='ชื่อพันธุ์พืช', ondelete='cascade')


class MDMForest(models.Model):
    _name = 'mdm.forest'
    _rec_name = "forest"
    _description = "ลักษณะของป่าไม้"

    resource_id = fields.Many2one('mdm.resource', string='รหัสทรัพยากร', required=False, ondelete='cascade')
    forest = fields.Selection(string="ป่าไม้",
                              selection=[('1', 'ป่าผลัดใบ'),
                                         ('2', 'ป่าเบญจพรรณ')],
                              required=False,
                              default='1')
    species_ids = fields.Many2many(comodel_name='mdm.species', string='พันธุ์ไม้', required=False, ondelete='cascade')


class MDMPublicSpace(models.Model):
    _name = 'mdm.public.space'
    _description = 'สถานที่สาธารณะประโยชน์'

    resource_id = fields.Many2one('mdm.resource', string='รหัสทรัพยากร', required=False, ondelete='cascade')
    name = fields.Char(string='สถานที่สาธารณะประโยชน์', required=False)
    type_public_id = fields.Many2one(comodel_name='mdm.type.public', string='ประเภทสถานที่สาธารณะประโยชน์',
                                     required=False)
    number_area = fields.Char(string='ระวางหมายเลข', required=False, size=50)
    area_01 = fields.Char(string='ไร่', required=False, size=10)
    area_02 = fields.Char(string='งาน', required=False, size=10)
    area_03 = fields.Char(string='ตารางวา', required=False, size=10)
    given_at = fields.Date(string='ให้ไว้ ณ วันที่', required=False)
