# -*- coding: utf-8 -*-
from odoo import http

# class VieterpMailbox(http.Controller):
#     @http.route('/vieterp_mailbox/vieterp_mailbox/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vieterp_mailbox/vieterp_mailbox/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vieterp_mailbox.listing', {
#             'root': '/vieterp_mailbox/vieterp_mailbox',
#             'objects': http.request.env['vieterp_mailbox.vieterp_mailbox'].search([]),
#         })

#     @http.route('/vieterp_mailbox/vieterp_mailbox/objects/<model("vieterp_mailbox.vieterp_mailbox"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vieterp_mailbox.object', {
#             'object': obj
#         })