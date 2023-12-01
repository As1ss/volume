

from odoo import models, fields

class modelo(models.Model):
     _name = 'taller.modelo'
     _description = 'Modelos de marcas'

     nombre = fields.Char(string="Nombre",required=True)
     marcaAsoc = fields.Many2one(string="Marca",comodel_name="taller.marca",required=True)
    
     