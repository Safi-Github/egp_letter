from odoo import models, fields

class EgpLetterOpenWindow(models.TransientModel):
    _name = 'egp.letter.open.window'
    _description = 'Open Window Action Wizard'

    # def do_action(self):
    #     print('this is the egp letter inbox wizard')
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Open Letters',
    #         'view_mode': 'tree',
    #         'res_model': 'egp.letter.inbox',
    #         'views': [(self.env.ref('egp_letter.egp_letter_inbox_tree_view').id, 'tree')],
    #         'domain': [],
    #     }