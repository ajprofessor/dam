# -*- coding: utf-8 -*-
# from odoo import http


# class Dam(http.Controller):
#     @http.route('/dam/dam', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dam/dam/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dam.listing', {
#             'root': '/dam/dam',
#             'objects': http.request.env['dam.dam'].search([]),
#         })

#     @http.route('/dam/dam/objects/<model("dam.dam"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dam.object', {
#             'object': obj
#         })

