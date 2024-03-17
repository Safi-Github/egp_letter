from odoo import models, fields, _

class CallWindowAction(models.TransientModel):
    _name = 'call_window_action'
    _description = 'Call Window Action Wizard'

    model_id = fields.Many2one('ir.model', string='Target Model')
    def open_custom(self):
        # Implement your custom window action logic here
        # This method will be called when a button is clicked in the wizard form view
        #  (you'll need to create a button and link it to this method)
        print("Custom window action triggered!")

        # Example: Open a specific form view of another model
        target_model = 'egp.letter.inbox'  # Replace with the actual model name
        target_view_id = self.env.ref('egp_letter.egp_letter_inbox_tree_view').id
        return {
            'name': _('Open Letter Inbox'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree',  # Adjust view mode as needed
            'res_model': target_model,
            'view_id': target_view_id,
            'target': 'new',
        }