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
    state = fields.Selection([('receive', 'Received')],  default='draft')

    execution_ids = fields.One2many('egp.letter.execution', 'letter_id', string='Executions')

    employeeGet_id = fields.Many2one('hr.employee', compute='_compute_user_empid')
    department_id = fields.Many2one('hr.department',compute='_compute_department_id')

    def _compute_user_empid(self):
            employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1)
            self.employeeGet_id = employee.id
            print('the employee gotted id', self.employeeGet_id)
    @api.depends('employeeGet_id')
    def _compute_department_id(self):
            departments = self.env['hr.department'].search([('manager_id', '=', self.employeeGet_id.id)], limit=1)

            self.department_id = departments.id
            print('department gotted id ', self.department_id)


            action = self.env.ref('egp_letter.action_egp_letter_inbox_tree_view')
            computed_value = self.department_id.id
            action.write({'context': {'default_desired_value': computed_value}})


    def open_custom_window(self):
        employee = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)], limit=1)
        print('the employee gotted id', employee.id)

        departments = self.env['hr.department'].search([('manager_id', '=', employee.id)], limit=1)
        print('department gotted id ', departments.id)

        action = self.env.ref('egp_letter.action_egp_letter_inbox_tree_view')
        computed_value = departments.id
        action.write({'context': {'default_desired_value': computed_value}})

        return self.env.ref('egp_letter.action_egp_letter_inbox_tree_view')


