from odoo import fields, models, api

class OdooTest(models.Model):
	_name = 'odoo.test'
	first_name = fields.Char(string="firstname", size=20, required=True)
	last_name = fields.Char(string="lastname", size=20, require=True)
	full_name = fields.Char(compute='_compute_name', store= True)

	@api.depends('first_name', 'last_name')	
	def _comput_name(self):
		for record in self:
			record.full_name = str(record.first_name) + " " + str(record.last_name)
