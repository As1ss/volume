from odoo import models, fields


class cliente(models.Model):
    _name="taller.cliente"
    _description="taller.cliente"

    nombre = fields.Char("Nombre",required=True)
    apellidos = fields.Char("Apellidos",required=True)
    DNI = fields.Char("DNI",required=True)
    telefono = fields.Char("Teléfono",required=True)
    email =fields.Char("Email",required=False)
    