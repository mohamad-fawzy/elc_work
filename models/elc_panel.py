from odoo import api, fields, models


class ElcPanel(models.Model):
    _name = "elc.panel"
    _description = "Electrical Panel"
    _order = "name"

    name = fields.Char(string="Panel Name - اسم اللوحة ", required=True)
    notes = fields.Text(string="Notes - ملاحظات")
    active = fields.Boolean(default=True)

 