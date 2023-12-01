from odoo import models, fields,api


class cliente(models.Model):
    _name="taller.cliente"
    _description="Cliente"

    nombre = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    NIF = fields.Char(string="NIF",required=True)
    telefono = fields.Char(string="Teléfono",required=True)
    email =fields.Char(string="Email",required=False)
    