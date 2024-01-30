from odoo import api, models, fields


class EgpLetterExecution(models.Model):
    _name = 'egp.letter.execution'
    _description = 'Letter Execution'

    letter_id = fields.Many2one('egp.letter', 'Letter')
    pathway = fields.Selection([('up', 'Up'), ('down', 'Down')], string='Pathway', default='up')
    name = fields.Char('Description')
    userGet_id = fields.Many2one('res.users', 'User', default=lambda self: self.env.user, invisible=True)

    # parent_id = fields.Many2one('hr.department', string='Parent Department', invisible=True)
    # child_ids = fields.One2many('hr.department', 'parent_id', string='Child Departments')

    department_id = fields.Many2one('hr.department',
                    string='Department',
                    store=True,
                    domain="department_domain")
    department_domain = fields.Char('Department Domain', compute='_compute_department_domain')

    departmentParent_id = fields.Many2one('hr.department', compute='_compute_parent_department')
    employeeGet_id = fields.Many2one('hr.employee', compute='_compute_user_department')
    id_manager = fields.Many2one('hr.department', string='Manager id', compute='_compute_id_manager')

    @api.depends('userGet_id')
    def _compute_user_department(self):
        for record in self:
            employee = self.env['hr.employee'].search([('user_id', '=', record.userGet_id.id)], limit=1)
            record.employeeGet_id = employee.id

    @api.depends('employeeGet_id')
    def _compute_parent_department(self):
        for record in self:
            departments = self.env['hr.department'].search([('manager_id', '=', record.employeeGet_id.id)], limit=1)
            print('department parent id', departments.parent_id.id)
            record.departmentParent_id = departments.parent_id
    @api.depends('employeeGet_id')
    def _compute_id_manager(self):
        for record in self:
            manager = self.env['hr.department'].search([('manager_id', '=', record.employeeGet_id.id)], limit=1)
            record.id_manager = manager.id
            print('this is the manger id of id record',manager.id)
    @api.depends('pathway')
    def _compute_department_domain(self):
        for record in self:
            if record.pathway == 'up':
                record.department_domain = [('parent_id', '=', record.departmentParent_id.id)]
                print('check the domain data', record.department_domain)
            elif record.pathway == 'down':
                record.department_domain = [
                    '|',
                    ('manager_id', '=', record.employeeGet_id.id),
                    ('parent_id', '=', record.id_manager.id)
                ]
                print('check the domain data', record.department_domain)

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
