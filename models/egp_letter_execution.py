from odoo import api, models, fields


class EgpLetterExecution(models.Model):
    _name = 'egp.letter.execution'
    _description = 'Letter Execution'

    letter_id = fields.Many2one('egp.letter', 'Letter')
    pathway = fields.Selection([('up', 'Up'), ('down', 'Down')], string='Pathway', default='up')
    name = fields.Char('Description')
    userGet_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user, invisible=True)
    # employeeGet_id = fields.Many2one('hr.employee', 'Employee',domain="[('user_id', '=', userGet_id)]")

    parent_id = fields.Many2one('hr.department', string='Parent Department', invisible=True)
    child_ids = fields.One2many('hr.department', 'parent_id', string='Child Departments',domain="[('manager_id', '=', userGet_id)]")

    department_id = fields.Many2one('hr.department',
                                    string='Department',
                                    compute='_compute_user_department'
                                    )
    #
    # sub_departments = fields.Many2one('hr.department',
    #                                  string='sub departments Departments',
    #                                  compute='_compute_sub_department'
    #                                  )
    #
    # @api.onchange('basic_evaluation_id')

    @api.depends('userGet_id')
    def _compute_user_department(self):
        for record in self:
            user_department = self.env['hr.department'].search([('manager_id', '=', record.userGet_id.id)])
            if user_department:
                record.department_id = user_department.id
            else:
                record.department_id = False
    #
    # @api.depends('department_id')
    # def _compute_sub_department(self):
    #     domain=[]
    #     print("test",self.department_id)
    #     for rec in self:
    #         print(rec.department_id)
    #         domain = [('parent_id', '=', rec.department_id)]
    #
    #     return {'domain': {'sub_departments': domain}}

    # @api.depends('user_id')
    # def _compute_user_department(self):
    #     for record in self:
    #         user = self.env.user
    #         user_department = self.env['hr.department'].search([('manager_id', '=', user.id)], limit=1)
    #         record.department_id = user_department.id if user_department else False
    #
    # @api.depends('department_id')
    # def _compute_sub_department(self):
    #     for rec in self:
    #         rec.sub_departments = False  # Ensure it's set to False if no sub-department found
    #         if rec.department_id:
    #             sub_department = self.env['hr.department'].search([('parent_id', '=', rec.department_id.id)], limit=1)
    #             rec.sub_departments = sub_department.id if sub_department else False



# added by Safiullah Danishjo
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
