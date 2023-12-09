# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConPublicSpace(http.Controller):

    @http.route('/api/get_public_space', type='json', auth='none')
    def get_public_space(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.public.space'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'name': rec.name,
                    'type_public_id': rec.type_public_id.id or None,
                    'number_area': rec.number_area,
                    'area_01': rec.area_01,
                    'area_02': rec.area_02,
                    'area_03': rec.area_03,
                    'given_at': rec.given_at,
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data