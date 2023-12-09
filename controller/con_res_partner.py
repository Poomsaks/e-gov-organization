# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConResPartner(http.Controller):

    @http.route('/api/get_partner_executive', type='json', auth='none')
    def get_partner_executive(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['res.partner'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                data_position = request.env['mdm.position'].sudo().search(
                    [('id', '=', rec.position_id.id)])
                for rec_po in data_position:
                    base64_data = base64.b64encode(rec.image)
                    decoded_data = base64.b64decode(base64_data)
                    if rec_po.position_group.id == 2:
                        vals = {
                            'id': rec.id,
                            'name': rec.name,
                            'position_id': rec_po.id or '',
                            'position_name': rec_po.name or '',
                            'village_id': rec.village_id.id or '',
                            'village_no': rec.village_id.village_no or '',
                            'phone': rec.phone,
                            'image': decoded_data,
                        }
                        data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/get_partner_council_member', type='json', auth='none')
    def get_partner_council_member(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['res.partner'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                data_position = request.env['mdm.position'].sudo().search(
                    [('id', '=', rec.position_id.id)])
                for rec_po in data_position:
                    base64_data = base64.b64encode(rec.image)
                    decoded_data = base64.b64decode(base64_data)
                    if rec_po.position_group.id == 3:
                        vals = {
                            'id': rec.id,
                            'name': rec.name,
                            'position_id': rec_po.id or '',
                            'position_name': rec_po.name or '',
                            'village_id': rec.village_id.id or '',
                            'village_no': rec.village_id.village_no or '',
                            'phone': rec.phone,
                            'image': decoded_data,
                        }
                        data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/get_partner_government', type='json', auth='none')
    def get_partner_government(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['res.partner'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                data_position = request.env['mdm.position'].sudo().search(
                    [('id', '=', rec.position_id.id)])
                for rec_po in data_position:
                    base64_data = base64.b64encode(rec.image)
                    decoded_data = base64.b64decode(base64_data)
                    vals = {
                        'id': rec.id,
                        'name': rec.name,
                        'position_id': rec_po.id or '',
                        'position_name': rec_po.name or '',
                        'village_id': rec.village_id.id or '',
                        'village_no': rec.village_id.village_no or '',
                        'phone': rec.phone,
                        'image': decoded_data,
                    }
                    data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data
