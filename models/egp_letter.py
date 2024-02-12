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
    state = fields.Selection([('inbox', 'Inbox'), ('outbox', 'Outbox')], string='Receives', default='inbox')
    mail = fields.Selection([('inbox', 'Inbox'), ('outbox', 'Outbox')], string='Sent', default='outbox')

    execution_ids = fields.One2many('egp.letter.execution', 'letter_id', string='Executions')






    filtered_record = fields.Many2one('egp.letter', compute='_compute_filtered_record', string='Filtered Record', store=True)
    #
    # @api.depends('recipients')
    # def _compute_filtered_record(self):
    #     for record in self:
    #         filtered_records = self.env['egp.letter'].search([('recipients', '=', 4)], limit=1)
    #         record.filtered_record = filtered_records





#     state_description = fields.Many2one('egp.letter', compute='_compute_state_get')
# @api.depends('state')
# def _compute_state_get(self):
#     for record in self:
#         fn_result = self.env['egp.letter'].search([('state', '=', 'draft')])
#         record.state_description = fn_result