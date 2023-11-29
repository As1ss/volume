

from odoo import models, fields


class vehiculo(models.Model):
     _name = 'taller.vehiculo'
     _description = 'taller.vehiculo'

     marca = fields.Many2many(required=True)
     modelo = fields.Many2many(required=True)
     año = fields.Date(required=True)
     num_bastion = fields.Char("Nº de bastión",size=20,required=True)
     matricula = fields.Char("Matrícula",required=True)
     cliente = fields.Many2one(required=True)
     imagen = fields.Image(required=False)
     tipo_combustible= fields.Selection("Tipo de combustible",["D","Diesel","G","Gasolina"],required=True)
     cilindrada = fields.Char("Color",required=False)
     tipo_vehiculo=fields.Selection("Tipo de vehículo",["T","Turismo","F","Furgoneta","4x4","Todoterreno","C","Caravana"],required=True)
     descripcion = fields.Text("Descripción",required=False)


     



