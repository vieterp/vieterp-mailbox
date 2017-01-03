# -*- coding: utf-8 -*-
from lxml import etree
from odoo import tools, models, fields, api

class vieterp_mail_inbox(models.Model):
    _inherit = 'mail.mail'
    _name = 'mail.inbox'

    template_id = fields.Many2one('mail.template', string='Mail Template', select=True)
    state = fields.Selection([
        ('inbox', 'Inbox'),
        ('outgoing', 'Outgoing'),
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('exception', 'Delivery Failed'),
        ('cancel', 'Cancelled'),
    ], 'Status', readonly=True, copy=False, default='outgoing')

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        context = self._context
        result = super(vieterp_mail_inbox, self).fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'form':
            current_id = context.get('active_id', False)
            my_state = self.browse(current_id).state
            if my_state in ['inbox', 'outgoing']:
                doc = etree.XML(result['arch'])
                for node in doc.xpath('//form'):
                    node.set('edit', 'true')
                result['arch'] = etree.tostring(doc)
        return result

    @api.onchange('template_id')  # if template are changed, call method
    def check_template_change(self):
        """ - mass_mailing: we cannot render, so return the template values
            - normal mode: return rendered values """
        if self.template_id and self.template_id.id:
            self.subject = self.template_id.subject
            self.body_html = self.template_id.body_html
            self.reply_to = self.template_id.reply_to
            self.mail_server_id = self.template_id.mail_server_id
            if self.template_id.attachment_ids:
                self.attachment_ids = [att.id for att in template.attachment_ids]
            if self.template_id.mail_server_id:
                self.mail_server_id = self.template_id.mail_server_id.id
            if self.template_id.user_signature and self.body_html:
                signature = self.env['res.users'].browse(self._uid).signature
                self.body = tools.append_content_to_html(self.body, signature, plaintext=False)
        else:
            if not self.body_html:
                signature = self.env['res.users'].browse(self._uid).signature
                self.body_html = signature