from encodings import utf_8
coding: utf_8

from odoo import models, fields


class vehiculo(models.Model):
     _name = 'taller.vehiculo'
     _description = 'Vehículo'


     matricula = fields.Char(string="Matrícula",required=True)
     num_bastidor = fields.Char(string="Nº de bastidor",required=True)
     cliente = fields.Many2one(string="Cliente",comodel_name="taller.cliente",required=True)
     marca = fields.Many2one(string="Marca",comodel_name="taller.marca",required=True)
     modelo = fields.Many2one(string="Modelo",comodel_name="taller.modelo",required=True)
  
     ano = fields.Date(string="Año",required=True)

     imagen = fields.Image(string="Imagen",required=False)
     tipo_combustible= fields.Selection([("D","Diesel"),("G","Gasolina"),("E","Eléctrico")], string="Tipo de combustible", required=True)
     cilindrada = fields.Char(string="Cilindrada",required=False)
     cv = fields.Char(string="Caballos de vapor",required=False)
     #campo calculado kw = fields.Char(string="Kilovatios")
     tipo_vehiculo=fields.Selection([("T","Turismo"),("F","Furgoneta"),("4x4","Todoterreno"),("C","Caravana")], string="Tipo de vehículo", required=True)
     descripcion = fields.Text(string="Descripción",required=False)
     color = fields.Char(string="Color")
     


     



