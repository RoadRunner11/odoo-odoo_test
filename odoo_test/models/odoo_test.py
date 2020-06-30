from odoo import fields, models

class OdooTest(models.Model):
	first_name = fields.Char(string="firstname", size=20, required=True)
	last_name = fields.Char(string="lastname", size=20, require=True)
	full_name = str(first_name) + " " + str(last_name)
