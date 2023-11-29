

from odoo import models, fields


class marca(models.Model):
     _name = 'taller.marca'
     _description = 'taller.marca'

     nombre = fields.Char("Nombre",required=True)
     logo = fields.Image(required=True)
     