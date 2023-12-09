# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConWater(http.Controller):

    @http.route('/api/get_water', type='json', auth='none')
    def get_water(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.water'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'water': rec.water,
                    'value_water': rec.value_water
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data