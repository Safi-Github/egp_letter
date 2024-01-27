from odoo import api, models, fields


class EgpLetterExecution(models.Model):
    _name = 'egp.letter.execution'
    _description = 'Letter Execution'

    letter_id = fields.Many2one('egp.letter', 'Letter')
    name = fields.Char('Description')
    department_id = fields.Many2one('hr.department', 'Department')


