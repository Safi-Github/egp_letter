from odoo import fields, models, api

class EgpLetterOutbox(models.Model):
    _name = "egp.letter.outbox"
    _description = "Outbox Letter"

    serial_number = fields.Char('Serial Number', required=True)
    date_issue = fields.Datetime('Issue Date', required=True)
    recipients = fields.Many2one('hr.department', 'To')
    carbon_copies = fields.Many2many('res.partner', 'egp_letter_outbox_carbon_copies', 'letter_id', 'partner_id', string="CC")
    name = fields.Char('Subject', required=True)
    content = fields.Html('Content', required=True)
    # source_department_id = fields.Many2one('hr.department', string='Source Department',
    #                                        default=lambda self: self.env.user.department_id.id, required=True)
    state = fields.Selection([('draft', 'Draft'), ('send', 'Sent')],  default='draft')

    execution_ids = fields.One2many('egp.letter.execution', 'letter_id', string='Executions')

    def adding_record_to_inbox_model(self):
        if self.state == 'draft':
            ModelB = self.env['egp.letter.inbox']
            ModelB.create({
            'serial_number': self.serial_number,
            'date_issue': self.date_issue,
            'recipients': self.recipients.id,  # Pass the ID of the hr.department record
            'carbon_copies': [(6, 0, self.carbon_copies.ids)],  # Pass the IDs of the res.partner records
            'name': self.name,
            'content': self.content,
            # 'source_department_id': self.source_department_id.id,
            'state': 'receive',
            'execution_ids': [(6, 0, self.execution_ids.ids)],  # Pass the IDs of the egp.letter.execution records
        })
        self.state = 'send'
        print("adding record to inbox model", self.state)

