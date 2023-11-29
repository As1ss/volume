# -*- coding: utf-8 -*-

from odoo import models, fields

class Brand(models.Model):
    _name = 'fashion.brand'
    name = fields.Char()
    description = fields.Text()

   
  

    

