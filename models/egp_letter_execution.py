from odoo import api, models, fields


class EgpLetterExecution(models.Model):
    _name = 'egp.letter.execution'
    _description = 'Letter Execution'

    letter_id = fields.Many2one('egp.letter', 'Letter')
    name = fields.Char('Description')
    department_id = fields.Many2one('hr.department', 'Department')


    #added by Safiullah Danishjo
    '@api.multi'
    def action_add_line(self):
        view_id = self.env.ref('egp_letter.egp.execution.form.view').id  # Replace with your actual view ID
        return {
            'name': 'Add a Line',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'egp.letter.execution',
            'view_id': view_id,
            'view_id': False,
            'target': 'new',
        }

