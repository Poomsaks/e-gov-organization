# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConEarth(http.Controller):

    @http.route('/api/get_earth', type='json', auth='none')
    def get_earth(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.earth'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'earth': rec.earth,
                    'breed_ids': rec.breed_ids.id or None,
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data