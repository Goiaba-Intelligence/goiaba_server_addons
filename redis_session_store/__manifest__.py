# (C) 2020 Goiaba Intelligence
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Redis Session Store",
    "version": "12.0",
    "depends": ["base"],
    "author": "Goiaba Intelligence",
    "license": 'AGPL-3',
    "description": """
    Use Redis Session instead of File system
    """,
    "summary": "",
    "website": "",
    "category": 'Tools',
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': ['redis'],
    },
}
