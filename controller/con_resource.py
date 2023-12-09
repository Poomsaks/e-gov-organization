# -*- coding: utf-8 -*-
import base64
import json
from odoo import http
from odoo.http import request


class ConResource(http.Controller):

    @http.route('/api/get_resource', type='json', auth='none')
    def get_resource(self, **post):
        request.session.db = post.get('db')
        data_info = request.env['mdm.resource'].sudo().search([])
        if data_info:
            data_s = []
            for rec in data_info:
                # TODO water
                water_rec = request.env['mdm.water'].sudo().search(
                    [('resource_id', '=', rec.id)])
                water_info = []
                for detail in water_rec:
                    water_info.append({
                        'water_id': detail.id or None,
                        'water_select_id': detail.water,
                        'water': dict(detail._fields['water'].selection).get(detail.water),
                        'value_water': detail.value_water or None,
                    })
                # TODO earth
                earth_rec = request.env['mdm.earth'].sudo().search(
                    [('resource_id', '=', rec.id)])
                earth_info = []
                for detail in earth_rec:
                    earth_info.append({
                        'earth_id': detail.id or None,
                        'earth': detail.earth,
                        'breed_ids': [{'id': record.id,
                                       'breed_name': record.breed_name, }
                                      for record in detail.breed_ids],
                    })
                # TODO forest
                forest_rec = request.env['mdm.forest'].sudo().search(
                    [('resource_id', '=', rec.id)])
                forest_info = []
                for detail in forest_rec:
                    forest_info.append({
                        'forest_id': detail.id or None,
                        'forest_select_id': detail.forest,
                        'forest': dict(detail._fields['forest'].selection).get(detail.forest),
                        'species_ids': [{'id': record.id,
                                         'species_name': record.species_name, }
                                        for record in detail.species_ids],
                    })

                # TODO public space
                public_space_rec = request.env['mdm.public.space'].sudo().search(
                    [('resource_id', '=', rec.id)])
                public_space_info = []
                for detail in public_space_rec:
                    public_space_info.append({
                        'public_space_id': detail.id or None,
                        'name': detail.name,
                        'type_public_id': detail.type_public_id.id or None,
                        'type_public_name': detail.type_public_id.name or None,
                        'number_area': detail.number_area,
                        'area_01': detail.area_01,
                        'area_02': detail.area_02,
                        'area_03': detail.area_03,
                        'given_at': detail.given_at
                    })

                vals = {
                    'id': rec.id,
                    'village_id': rec.village_id.id,
                    'village_name': rec.village_id.name,
                    'village_no': rec.village_id.village_no,
                    'water_ids': water_info,
                    'earth_ids': earth_info,
                    'forest_ids': forest_info,
                    'public_space_ids': public_space_info
                }
                data_s.append(vals)
            data = {'status': 200, 'response': data_s, 'message': 'success'}
            return data
        else:
            data = {'status': 500, 'response': 'ไม่พบข้อมูล', 'message': 'success'}
            return data

    @http.route('/api/create_resource', type='json', auth='user')
    def create_resource(self, **post):
        data_model = request.env['mdm.resource'].sudo().search([])
        data_create = data_model.create({
            'village_id': post.get('village_id'),
        })
        # TODO water
        water_list = []
        if post.get('water_ids'):
            water_data = json.loads(json.dumps(post.get('water_ids')))
            for rec in water_data:
                water_list.append((0, 0, {
                    'resource_id': data_create.id,
                    'water': rec['water'],
                    'value_water': rec['value_water']
                }))
            request.env['mdm.resource'].sudo().browse(data_create.id).write({
                'water_ids': water_list,
            })

        # TODO earth
        earth_list = []
        if post.get('earth_ids'):
            earth_data = json.loads(json.dumps(post.get('earth_ids')))
            for rec in earth_data:
                earth_list.append((0, 0, {
                    'resource_id': data_create.id,
                    'earth': rec.get('earth'),
                    'breed_ids': [(6, 0, rec.get('breed_ids'))] if rec.get('breed_ids') else False
                }))
            request.env['mdm.resource'].sudo().browse(data_create.id).write({
                'earth_ids': earth_list,
            })

            # TODO forest
            forest_list = []
            if post.get('forest_ids'):
                forest_data = json.loads(json.dumps(post.get('forest_ids')))
                for rec in forest_data:
                    forest_list.append((0, 0, {
                        'resource_id': data_create.id,
                        'forest': rec.get('forest'),
                        'species_ids': [(6, 0, rec.get('species_ids'))] if rec.get('species_ids') else False
                    }))
                request.env['mdm.resource'].sudo().browse(data_create.id).write({
                    'forest_ids': forest_list,
                })

                # TODO public space
                public_space_list = []
                if post.get('public_space_ids'):
                    public_space_data = json.loads(json.dumps(post.get('public_space_ids')))
                    for rec in public_space_data:
                        public_space_list.append((0, 0, {
                            'resource_id': data_create.id,
                            'name': rec.get('name'),
                            'type_public_id': rec.get('type_public_id'),
                            'number_area': rec.get('number_area'),
                            'area_01': rec.get('area_01'),
                            'area_02': rec.get('area_02'),
                            'area_03': rec.get('area_03'),
                            'given_at': rec.get('given_at')
                        }))
                    request.env['mdm.resource'].sudo().browse(data_create.id).write({
                        'public_space_ids': public_space_list,
                    })

        data = {'status': 200, 'response': data_create.id, 'message': 'success'}
        return json.dumps(data)
