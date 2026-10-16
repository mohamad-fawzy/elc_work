{  # noqa: B018
    "name": "Electrical Work",
    "version": "19.0.1.0.0",
    "category": "Maintenance",
    "summary": "Electrical panels and cable documentation",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/elc_panel_views.xml",
        "views/cable_data_views.xml",
        "views/elc_menus.xml",
    ],
    "installable": True,
    "application": True,
}