# -*- coding: utf-8 -*-
# from odoo import http


# class DefaultImage(http.Controller):
#     @http.route('/default_image/default_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_image/default_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_image.listing', {
#             'root': '/default_image/default_image',
#             'objects': http.request.env['default_image.default_image'].search([]),
#         })

#     @http.route('/default_image/default_image/objects/<model("default_image.default_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_image.object', {
#             'object': obj
#         })
