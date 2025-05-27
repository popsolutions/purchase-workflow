from odoo import api, fields, models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"
    _order = "sequence"

    sequence = fields.Integer(
        sequence=fields.Integer(compute="_compute_sequence", store=True)
    )
    sequence_id = fields.Integer(string="Sequence ID", related="sequence", store=True)

    @api.depends("request_id.line_ids")
    def _compute_sequence(self):
        for line in self:
            line.sequence = 0
            if line.request_id.line_ids:
                line.sequence = list(line.request_id.line_ids).index(line) + 1
