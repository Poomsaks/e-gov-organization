from odoo import models, fields


class MDMTypeAgriclture(models.Model):
    _name = 'mdm.type.agriculture'
    _rec_name = 'name'
    _description = 'ประเภทการทำการเกษตร'

    name = fields.Char(stirng="ประเภทการทำการเกษตร", required=False)
