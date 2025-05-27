# Copyright 2025 PopSolutions
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Request Lines Sequence",
    "summary": "Add sequence numbers to Purchase Request lines for better identification.",
    "version": "16.0.1.0.1",
    "license": "AGPL-3",
    "author": "PopSolutions, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "depends": [
        "purchase_request",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
    "data": [
        "views/purchase_request_line_views.xml",
    ],
    "demo": [],
    "maintainers": ["rafnixg", "navigator"],
}
