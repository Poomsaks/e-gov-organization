# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConVillage(http.Controller):

    @http.route('/api/get_village', type='json', auth='none')
    def get_village(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.village'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                vals = {
                    'id': rec.id,
                    'name': rec.name,
                    'village_no': rec.village_no,
                    'populace': rec.populace,
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/get_village_search', type='json', auth='none')
    def get_village_search(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.village'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                partner_data_list = []
                data_partner = request.env['res.partner'].sudo().search([('village_id', '=', rec.id)])
                for partner in data_partner:
                    # print(partner.name)
                    base64_data = base64.b64encode(partner.image)
                    decoded_data = base64.b64decode(base64_data)
                    partner_data_list.append({
                        'id': partner.id,
                        'name': partner.name,
                        'image': decoded_data
                    })
                vals = {
                    'id': rec.id,
                    'name': rec.name,
                    'partner': partner_data_list,
                    'village_no': rec.village_no,
                    'populace': rec.populace,
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/create_village', type='json', auth='user')
    def create_village(self, **post):
        data_model = request.env['mdm.village'].sudo().search([])
        data_create = data_model.create({
            'name': post.get('name'),
            'village_no': post.get('village_no'),
            'populace': post.get('populace'),
        })
        data = {'status': 200, 'response': data_create.id, 'message': 'success'}
        return json.dumps(data)