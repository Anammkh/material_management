from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Supplier(models.Model):
    _name = 'material.management.supplier'
    _description = 'Supplier'

    nama = fields.Char(string='Nama', required=True)
    alamat = fields.Text(string='Alamat')
    phone = fields.Char(string='Phone')

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if record.phone and (len(record.phone) < 10 or len(record.phone) > 15 or not record.phone.isdigit()):
                raise ValidationError("Phone number must be 10-15 digits.")
