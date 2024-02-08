from odoo import fields, models, api


class EgpLetter(models.Model):
    _name = "egp.letter"
    _description = "Letter"

    serial_number = fields.Char('Serial Number', required=True)
    date_issue = fields.Datetime('Issue Date', required=True)
    recipients = fields.Many2one('hr.department', 'To')
    carbon_copies = fields.Many2many('res.partner', 'egp_letter_carbon_copies', 'letter_id', 'partner_id', string="CC")
    name = fields.Char('Subject', required=True)
    content = fields.Html('Content', required=True)
    source_department_id = fields.Many2one('hr.department', string='Source Department',
                                           default=lambda self: self.env.user.department_id.id, required=True)
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent')], string='Status', default='draft')
    mail = fields.Selection([('inbox', 'Inbox'), ('outbox', 'Outbox')], string='Email', default='outbox')

    execution_ids = fields.One2many('egp.letter.execution', 'letter_id', string='Executions')

    # sent_records = fields.Integer(string='Sent Records', compute='_compute_sent_records')
    #
    # def _compute_sent_records(self):
    #     for record in self:
    #         sent_records = self.env['egp.letter'].search_count([('create_uid', '=', self.env.user.id)])
    #         record.sent_records = sent_records


    # letter_id = fields.Many2one('egp.letter', 'Letter ID',domain=[('recipients','=',[7])])
    # department_id_test = fields.One2many(string='Letter', compute='_compute_letter_records')
    # @api.depends('department_id_test')
    # def _compute_letter_records(self):
    #     for record in self:
    #         letter_records = self.env['egp.letter'].search([('recipients', '=', 7)])
    #         record.department_id_test = letter_records


#     state_description = fields.Many2one('egp.letter', compute='_compute_state_get')
# @api.depends('state')
# def _compute_state_get(self):
#     for record in self:
#         fn_result = self.env['egp.letter'].search([('state', '=', 'draft')])
#         record.state_description = fn_result