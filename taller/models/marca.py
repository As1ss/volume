

from odoo import models, fields


class marca(models.Model):
     _name = 'taller.marca'
     _description = 'Marcas de vehículos'

     nombre = fields.Char(string="Nombre",required=True)
     logo = fields.Image(string="Logo",required=False)
     