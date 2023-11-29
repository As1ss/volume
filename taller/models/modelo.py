

from odoo import models, fields


class modelo(models.Model):
     _name = 'taller.modelo'
     _description = 'taller.modelo'

     nombre = fields.Char("Nombre",required=True)
    
     