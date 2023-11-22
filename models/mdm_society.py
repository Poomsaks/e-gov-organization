from odoo import models, fields, _


class MDMSociety(models.Model):
    _name = 'mdm.society'
    _rec_name = 'village_name'
    _description = 'สังคม'

    village_id = fields.Many2one(comodel_name='mdm.village', string='หมู่บ้าน', required=False)
    village_name = fields.Char(string=_('หมู่บ้าน'), required=False, related='village_id.name')
    hospital_sub_district_ids = fields.One2many(comodel_name='mdm.hospital.sub_district', inverse_name='society_id',
                                                string='โรงพยาบาลส่งเสริมสุขภาพตำบล', required=False)
    social_worker_ids = fields.One2many(comodel_name='mdm.social.worker', inverse_name='society_id',
                                        string='นักสังคมสงเคราะห์', required=False)
    school_ids = fields.One2many(comodel_name='mdm.school', inverse_name='society_id',
                                 string='โรงเรียน', required=False)


class MDMHospitalSubdistrict(models.Model):
    _name = 'mdm.hospital.sub_district'
    _description = 'โรงพยาบาลส่งเสริมสุขภาพตำบล'

    society_id = fields.Many2one('mdm.society', string='รหัสสังคม', required=False, ondelete='cascade')
    name = fields.Char(string='ชื่อ รพ.สต.', required=False)
    doctor_id = fields.Many2many(comodel_name='res.partner', string='แพทย์')
    osm_Village_id = fields.Many2many(comodel_name='res.partner', string='อสม.')


class MDMSocialWorker(models.Model):
    _name = 'mdm.social.worker'
    _description = 'นักสังคมสงเคราะห์'

    society_id = fields.Many2one('mdm.society', string='รหัสสังคม', required=False, ondelete='cascade')
    social_worker_id = fields.Many2many(comodel_name='res.partner', string='นักสังคมสงเคราะห์')


class MDMSchool(models.Model):
    _name = 'mdm.school'
    _description = 'โรงเรียน'

    society_id = fields.Many2one('mdm.society', string='รหัสสังคม', required=False, ondelete='cascade')
    name = fields.Char(string='ชื่อโรงเรียน', required=False)
    level_no_start = fields.Selection(string="ระดับชั้นเริ่มต้น",
                                      selection=[('1', 'ศูนย์พัฒนาเด็กเล็ก'),
                                                 ('2', 'อนุบาล 1'),
                                                 ('3', 'อนุบาล 2'),
                                                 ('4', 'อนุบาล 3'),
                                                 ('5', 'ประถมศึกษาปีที่ 1'),
                                                 ('7', 'ประถมศึกษาปีที่ 2'),
                                                 ('8', 'ประถมศึกษาปีที่ 3'),
                                                 ('9', 'ประถมศึกษาปีที่ 4'),
                                                 ('10', 'ประถมศึกษาปีที่ 5'),
                                                 ('11', 'ประถมศึกษาปีที่ 6'),
                                                 ('12', 'มัธยมศึกษาปีที่ 1'),
                                                 ('13', 'มัธยมศึกษาปีที่ 2'),
                                                 ('14', 'มัธยมศึกษาปีที่ 3'),
                                                 ('15', 'มัธยมศึกษาปีที่ 4'),
                                                 ('16', 'มัธยมศึกษาปีที่ 5'),
                                                 ('17', 'มัธยมศึกษาปีที่ 6'), ],
                                      required=False, default='1')
    level_no_end = fields.Selection(string="ระดับชั้นสูงสุด",
                                    selection=[('1', 'ศูนย์พัฒนาเด็กเล็ก'),
                                               ('2', 'อนุบาล 1'),
                                               ('3', 'อนุบาล 2'),
                                               ('4', 'อนุบาล 3'),
                                               ('5', 'ประถมศึกษาปีที่ 1'),
                                               ('7', 'ประถมศึกษาปีที่ 2'),
                                               ('8', 'ประถมศึกษาปีที่ 3'),
                                               ('9', 'ประถมศึกษาปีที่ 4'),
                                               ('10', 'ประถมศึกษาปีที่ 5'),
                                               ('11', 'ประถมศึกษาปีที่ 6'),
                                               ('12', 'มัธยมศึกษาปีที่ 1'),
                                               ('13', 'มัธยมศึกษาปีที่ 2'),
                                               ('14', 'มัธยมศึกษาปีที่ 3'),
                                               ('15', 'มัธยมศึกษาปีที่ 4'),
                                               ('16', 'มัธยมศึกษาปีที่ 5'),
                                               ('17', 'มัธยมศึกษาปีที่ 6'), ],
                                    required=False, default='1')
    teacher_value = fields.Char(string='จำนวนครู', required=False, size=3)
    student_value = fields.Char(string='จำนวนนักเรียน', required=False, size=3)
