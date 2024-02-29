from odoo import fields, models, api

class EgpLetterInbox(models.Model):
    _name = "egp.letter.inbox"
    _description = "Inbox Letter"

    serial_number = fields.Char('Serial Number', required=True)
    date_issue = fields.Datetime('Issue Date', required=True)
    recipients = fields.Many2one('hr.department', 'To')
    carbon_copies = fields.Many2many('res.partner', 'egp_letter_inbox_carbon_copies', 'letter_id', 'partner_id', string="CC")
    name = fields.Char('Subject', required=True)
    content = fields.Html('Content', required=True)
    # source_department_id = fields.Many2one('hr.department', string='Source Department',
    #                                        default=lambda self: self.env.user.department_id.id, required=True)
    state = fields.Selection([('draft', 'Draft'), ('send', 'Sent')],  default='draft')

    execution_ids = fields.One2many('egp.letter.execution', 'letter_id', string='Executions')

