from odoo import api, fields, models


class ElcCableData(models.Model):
    _name = "elc.cable.data"
    _description = "Cable Data"
    _order = "cable_no"

    cable_no = fields.Char(string="Cable No - رقم الكابل", required=True, index=True)

    from_panel_id = fields.Many2one(
        "elc.panel", string="From Panel - من ", required=True, ondelete="restrict"
    )
    to_panel_id = fields.Many2one(
        "elc.panel", string="To Panel - الى ", ondelete="restrict"
    )
    terminal_numbers = fields.Char(
        string="Terminal Numbers",
        help="Terminals the cable comes from, e.g. X1:1-4",
    )
    destination_box = fields.Char(string="Destination Box")

    cross_section = fields.Selection(
        [
            ("1.5", "1.5 mm²"),
            ("2.5", "2.5 mm²"),
            ("4", "4 mm²"),
            ("6", "6 mm²"),
            ("10", "10 mm²"),
            ("16", "16 mm²"),
            ("25", "25 mm²"),
            ("35", "35 mm²"),
            ("50", "50 mm²"),
        ],
        string="Cross Section",
    )

    notes = fields.Text(string="Notes")
    active = fields.Boolean(default=True)

    _cable_no_uniq = models.Constraint(
        "UNIQUE(cable_no)", "Cable number must be unique!"
    )

    # @api.depends("cores", "cross_section")
    # def _compute_size_display(self):
    #     for rec in self:
    #         if rec.cores and rec.cross_section:
    #             rec.size_display = f"{rec.cores}×{rec.cross_section} mm²"
    #         else:
    #             rec.size_display = False

    # @api.depends("cable_no", "name")
    # def _compute_display_name(self):
    #     for rec in self:
    #         rec.display_name = (
    #             f"{rec.cable_no} - {rec.name}" if rec.cable_no else rec.name
    #         )